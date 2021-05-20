import os

from server import settings
from server.settings import config
from ml.detection import FaceDetector
from ml.model import FaceNetModel
from ml.utils import Image, Detection


class FaceRecognition:
	def __init__(self):
		self._facenet_model = FaceNetModel(weights_dir=os.path.join(settings.BASE_DIR, config.weights_facenet))

	def extract_vector(self, image, single=False):
		assert isinstance(image, Image)
		detections = FaceDetector.detect(image=image)
		result = []
		if not detections:
			return []

		if single:
			cropped_face = image.crop(bbox=detections[0].bbox)
			vector = self.face2vector(cropped_face, return_list=True)
			return Detection(confidence=detections[0].confidence, vector=vector, image=cropped_face)

		for detection in detections:
			cropped_face = image.crop(bbox=detection.bbox)
			vector = self.face2vector(cropped_face, return_list=True)
			result.append(Detection(confidence=detection.confidence, vector=vector, image=cropped_face))
		return result

	def face2vector(self, images, return_list=False):
		"""
		:param images: in BGR color space
		:param return_list: If True return type "list" else return type "np.ndarray"
		:return: 128 dimensional vector
		"""
		if type(images) == list:
			vectors = self._facenet_model.predict([image.rgb for image in images])
			if return_list:
				return list([vector.astype(float) for vector in vectors])
			return vectors

		vectors = self._facenet_model.predict([images.rgb])
		if return_list:
			return list(vectors.astype(float)[0])
		return vectors[0]
