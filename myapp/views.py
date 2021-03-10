from django.shortcuts import render, redirect
from .models import *
from .forms import *

def homepage(request):

	tasks = ModelTask.objects.all()
	form = ModelForm()

	if request.method == 'POST':
		form = ModelForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'tasks': tasks, 'form': form}
	return render(request, 'myapp/homepage.html', context)

def update(request, pk):

	tasks = ModelTask.objects.get(id=pk)
	form = ModelForm(instance=tasks)

	if request.method == 'POST':
		form = ModelForm(request.POST, instance=tasks)
		if form.is_valid():
			form.save()

			return redirect('/')

	context = {'form': form}
	return render(request, 'myapp/update.html', context)

def delete(request, pk):
	item = ModelTask.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item': item}
	return render(request, 'myapp/delete.html', context)