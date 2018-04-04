from django.db import models
from django.utils import timezone
# Create your models here.
#syntax my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

class Article(models.Model):
	#syntax my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def __str__(self):
		return self.title

# class Student_obj(models.Model):
# 	created_date = models.DateTimeField(
# 			default=timezone.now)
# 	name = models.CharField(max_length=200)
# 	roll_no = models.IntegerField()
# 	resume = models.FileField(upload_to='documents/')
# 	def __str__(self):
# 		return self.name

class Schools(models.Model):
	name = models.CharField(max_length=30)
	estd = models.DateField(null=True, blank=True)
	student_count = models.IntegerField()

	def __str__(self):
		return self.name

class Classes(models.Model):
	school = models.ForeignKey(Schools, on_delete=models.CASCADE)
	name_of_class = models.CharField(max_length=30)

	def __str__(self):
		return self.name_of_class

class Sections(models.Model):
	name_of_section = models.CharField(max_length=100)
	
	school = models.ForeignKey(Schools, on_delete=models.SET_NULL, null=True)
	std = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name_of_section

class Student(models.Model):
	name_of_student = models.CharField(max_length=100)
	gender = models.CharField(max_length=100)
	
	school = models.ForeignKey(Schools, on_delete=models.SET_NULL, null=True)
	std = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
	section = models.ForeignKey(Sections, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name_of_student
