from django.contrib import admin
from .models import Article ,Student, Schools , Classes , Sections 

# Register your models here.
admin.site.register(Article)
admin.site.register(Schools)
admin.site.register(Classes)
admin.site.register(Sections)
admin.site.register(Student)