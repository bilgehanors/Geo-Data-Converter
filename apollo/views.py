from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def time(request):
  return render(request, 'time.html')

def cartesian(request):
  return render(request, 'cartesian.html')

def coordinate(request):
  return render(request, 'coordinate.html')


