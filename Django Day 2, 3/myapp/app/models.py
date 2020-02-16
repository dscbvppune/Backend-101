from django.db import models
# Create your models here.
class Question(models.Model):
	question = models.CharField(max_length=200)
	answer = models.CharField(max_length=32)

	def publish(self):
		self.save()

	def __str__(self):
		return self.question