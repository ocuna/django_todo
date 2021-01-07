from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

	# Create your views here.
def about(request):
	context = {
		'first_name':'Nathanael',
		'last_name':'Armstrong'
	}
	return render(request, 'about.html', context)
