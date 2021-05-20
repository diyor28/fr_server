from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from api.apiviews import ConfigAPI, ExtractVectorAPI, ClearTablesAPI, CompareTwoFacesAPI
from ml import TaskManager

urlpatterns = [
	path('config/', ConfigAPI.as_view(), name="config"),
	path('extract_vector/', ExtractVectorAPI.as_view(), name="extract_vector"),
	path('clear/', ClearTablesAPI.as_view(), name="clear"),
	path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
	path('compare/', CompareTwoFacesAPI.as_view(), name='token_refresh'),
]

# TODO: turn back on later
TaskManager.setup()
