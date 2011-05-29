from django.db import models

class Subscription (models.Model):
	name = models.CharField(max_length=100)
	cpf = models.CharField(max_length=11, unique=True)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ["create_at"]
		verbose_name = u"Inscricao"
		verbose_name_plural = u"Incricoes"