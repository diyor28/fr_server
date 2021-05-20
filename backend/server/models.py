import os

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.db import models

from server import settings
from server.helpers import RandomFileName

GENDER_CHOICES = (("Male", "Male"),
				  ("Female", "Female"))


class UserManager(BaseUserManager):
	"""Define a model manager for User model with no username field."""

	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""Create and save a User with the given email and password."""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		"""Create and save a regular User with the given email and password."""
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		"""Create and save a SuperUser with the given email and password."""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)


class UserModel(AbstractUser):
	username = None
	email = models.EmailField(verbose_name='email address', unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	class Meta:
		db_table = 'users'


class ClientsModel(models.Model):
	gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER_CHOICES)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='clients')

	class Meta:
		db_table = 'clients'


class VectorsModel(models.Model):
	image = models.ImageField(upload_to=RandomFileName(settings.USER_IMAGES), blank=True, null=True)
	vector = ArrayField(models.FloatField(), default=list, null=True)
	confidence = models.FloatField(blank=True, null=True)
	client = models.ForeignKey(ClientsModel, on_delete=models.CASCADE, blank=True, null=True, related_name="vectors")

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		return super().save(force_insert=force_insert, force_update=force_update,
							using=using, update_fields=update_fields)

	def delete(self, using=None, keep_parents=False):
		if os.path.exists(self.image.path):
			os.remove(self.image.path)
		return super().delete(using=using, keep_parents=keep_parents)

	class Meta:
		db_table = 'vectors'


class TasksModel(models.Model):
	vector = ArrayField(models.FloatField(blank=True, null=True), blank=True, default=list)
	camera_id = models.IntegerField(blank=True, null=True)
	date = models.DateTimeField(blank=True, null=True)
	active = models.BooleanField(default=False)
	confidence = models.FloatField(blank=True, null=True)
	image = models.ImageField(upload_to=RandomFileName(settings.TASKS_IMAGES))
	gender = models.CharField(max_length=30, blank=True, null=True)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='tasks')

	def delete(self, using=None, keep_parents=False, delete_file=False):
		if os.path.exists(self.image.path) and delete_file:
			os.remove(self.image.path)
		return super().delete(using=using, keep_parents=keep_parents)

	class Meta:
		db_table = 'tasks'


class LogsModel(models.Model):
	workers = models.IntegerField(null=True, blank=True)

	class Meta:
		db_table = 'logs'
