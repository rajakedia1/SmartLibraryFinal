from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=20, help_text="Enter your name")
	branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True)
	admission_no = models.CharField(max_length=10)

	class Meta:
		ordering = ["-name"]

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('model-detail-view',args=[str(self.id)])

class Branch(models.Model):
	branch_name = models.CharField(max_length=30,null=True)
	HOD = models.CharField(max_length=20)
	representative = models.CharField(max_length=20)
	def get_absolute_url(self):
		return reverse('representative-detail',args=[str(self.id)])

	def __str__(self):
		return self.branch_name

class Info(models.Model):
	about = models.CharField(max_length=1000)
	from_branch = models.ForeignKey('Branch',on_delete=models.SET_NULL,null=True)

	def __str__(self):
		return self.about





