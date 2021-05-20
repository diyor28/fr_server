import os

from server import settings
from server.settings import config
from ml.model import WideResNet


class GenderModel:
	def __init__(self):
		self._gender_model = WideResNet(os.path.join(settings.BASE_DIR, config.weights_gendernet))

	def predict_gender(self, images):
		if type(images) == list:
			return self._gender_model.predict([image.bgr for image in images])
		return self._gender_model.predict([images.bgr])[0]
