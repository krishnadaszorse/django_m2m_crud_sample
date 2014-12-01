from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Job
from .forms import JobForm
def job_list(request):# for update the task 
	success = False
	success_message = 'Task added successfully'
	if 'success' in request.session:
		success_message = request.session['success']
		success = True
		del request.session['success']
	jobs = Job.objects.all()
	variables = RequestContext(request, {
        'jobs':jobs,
        'success':success,
        'success_message':success_message,
        })
	return render_to_response('job_list.html',variables)

def post_job(request):# for post job
	form = JobForm()
	if request.POST:
		form = JobForm(request.POST)
		if form.is_valid():
			job = form.save()
			request.session['success']	= 'job '+job.title+' was added successfully'
			return HttpResponseRedirect('/')
	variables = RequestContext(request, {
        'form':form,
        })
	return render_to_response('post_job.html',variables)

def update_job(request,id):# for post job
	job = get_object_or_404(Job,id=id)
	form = JobForm(instance=job)
	if request.POST:
		form = JobForm(request.POST,instance=job)
		if form.is_valid():
			job = form.save()
			request.session['success']	= 'job '+job.title+' was updated successfully'
			return HttpResponseRedirect('/')
	variables = RequestContext(request, {
        'job':job,
        'form':form,
        })
	return render_to_response('update_job.html',variables)

def delete_job(request,id):# for post job
	job = get_object_or_404(Job,id=id)
	request.session['success']	= 'job '+job.title+' was deleted successfully'
	job.delete()
	return HttpResponseRedirect('/')