from django.db import models

class Category(models.Model):
	name = models.CharField(verbose_name = 'Category Name', max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return self.name

class Skill(models.Model):
	name = models.CharField(verbose_name = 'Skill Name', max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name = 'Skill'
		verbose_name_plural = 'Skills'

	def __unicode__(self):
		return self.name 

class Job(models.Model):
	title = models.CharField(verbose_name = 'Job Title', max_length=50)
	description = models.TextField(verbose_name = 'Job Description')
	skill = models.ManyToManyField(Skill,verbose_name = 'Required skills')
	category = models.ManyToManyField(Category,verbose_name = 'Job Categories')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name = 'Job'
		verbose_name_plural = 'Jobs'

	def __unicode__(self):
		return self.title 