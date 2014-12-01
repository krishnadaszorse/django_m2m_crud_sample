from django.contrib import admin
from .models import Skill,Category,Job



class JobAdmin(admin.ModelAdmin):
	model = Job
	fields = ('title','description','skill','category')
	list_display = ('title','description','created_at','updated_at')
	search_fields = ['title','skill__name','category__name']
admin.site.register(Job,JobAdmin)

class SkillAdmin(admin.ModelAdmin):
	model = Skill
	fields = ('name',)
	list_display = ('name','created_at','updated_at')
	search_fields = ['name']
admin.site.register(Skill,SkillAdmin)

class CategoryAdmin(admin.ModelAdmin):
	model = Category
	fields = ('name',)
	list_display = ('name','created_at','updated_at')
admin.site.register(Category,CategoryAdmin)