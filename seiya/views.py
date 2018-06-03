from django.shortcuts import render
from Gallery.models import Gallery


def index(request):
	gallerys = Gallery.objects
	return render(request, 'index.html', {'gallerys': gallerys})