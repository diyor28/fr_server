import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName(object):
	def __init__(self, path):
		self.path = path

	def __call__(self, instance, filename):
		extension = os.path.splitext(filename)[1]
		return os.path.join(self.path, uuid.uuid4().hex + extension)
