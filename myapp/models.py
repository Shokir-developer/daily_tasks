from django.db import models

class ModelTask(models.Model):
	title = models.CharField(max_length=100)
	complated = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title