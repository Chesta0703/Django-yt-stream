import subprocess
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  # subprocess.call(["script.sh"], shell=True)
  return render(request,'index.html');