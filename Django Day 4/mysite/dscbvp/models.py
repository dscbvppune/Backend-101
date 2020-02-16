from django.db import models
from django.utils import timezone
# Create your models here.
class Attendee(models.Model):
	name = models.CharField(max_length=32)
	email = models.CharField(max_length=256)
	mobileNum = models.CharField(max_length=12)
	login_Date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name