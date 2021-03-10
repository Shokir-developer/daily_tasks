from django.contrib import admin
from .models import *

class AdminModel(admin.ModelAdmin):
	list_filter = ['title']
	search_fields = ['title']
	class Meta:
		model = ModelTask
		fields = '__all__'


admin.site.register(ModelTask, AdminModel)
