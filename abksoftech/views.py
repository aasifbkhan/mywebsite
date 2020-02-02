from django.shortcuts import render
from .models import Banner, Profile

# Create your views here.
def index(request):
	banners = Banner.objects.all()
	profile = Profile.objects.all()
	print(profile)
	print(banners)
	n = len(banners)
	params = {'no_of_slide':n, 'range':range(1, n),'banner':banners, 'profile':profile}
	return render(request, 'abksoftech/index.html', params)


# admin
def dashboard(request):
	return render(request, 'account/dashboard.html')

def profile(request):
	profile = Profile.objects.all()
	print(profile)
	params = {'profile':profile}
	return render(request, 'account/profile.html',params)

def inbox(request):
	return render(request, 'account/inbox.html')