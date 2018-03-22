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