from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.permissions import UsersPermissions, CsrfExemptSessionAuthentication
from server.models import TasksModel, VectorsModel, ClientsModel, LogsModel
from server.settings import config
from ml import TaskManager
from ml.utils import cosine_similarity, Image


class ClearTablesAPI(APIView):
	authentication_classes = (CsrfExemptSessionAuthentication, TokenAuthentication, JWTAuthentication)
	permission_classes = (UsersPermissions,)
	tables = {"tasks": TasksModel,
			  "vectors": VectorsModel,
			  "users": ClientsModel,
			  "logs": LogsModel}

	def get(self, request):
		data = [{"name": key, "count": table.objects.count()} for key, table in self.tables.items()]
		return Response(data)

	def post(self, request):
		print('data::', request.data)
		for table in request.data['tables']:
			if table in self.tables:
				self.tables[table].objects.all().delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class CompareTwoFacesAPI(APIView):
	authentication_classes = (CsrfExemptSessionAuthentication, TokenAuthentication, JWTAuthentication)
	permission_classes = (UsersPermissions,)

	def post(self, request):
		vector1 = TaskManager.extract_vector(Image(request.data['image1']), single=True).vector
		vector2 = TaskManager.extract_vector(Image(request.data['image2']), single=True).vector
		similarity = cosine_similarity(vector1, vector2)
		data = {"similarity": similarity}
		return Response(data)


class ExtractVectorAPI(APIView):
	authentication_classes = (CsrfExemptSessionAuthentication, TokenAuthentication, JWTAuthentication)
	permission_classes = (UsersPermissions,)

	def post(self, request):
		detection = TaskManager.extract_vector(request.data['image'])
		if request.data.get("gender", False):
			detection.gender = TaskManager.predict_gender(detection.image)

		data = {"gender": detection.gender,
				"vector": detection.vector,
				"confidence": detection.confidence}
		return Response(data)


class ConfigAPI(APIView):
	authentication_classes = (CsrfExemptSessionAuthentication, TokenAuthentication, JWTAuthentication)
	permission_classes = (UsersPermissions,)

	def get(self, request):
		data = config.config.copy()
		data.pop('database')
		return Response(data)

	def post(self, request):
		try:
			data = config.save(request.data)
		except Exception as e:
			raise ValidationError(e.__str__())
		return Response(data)
