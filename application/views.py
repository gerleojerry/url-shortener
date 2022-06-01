from calendar import prmonth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
import uuid
import json
from .forms import LinkForm
from .models import Links

# Create your views here.

def homepage(request):
  form  = LinkForm()

  return render(request, 'index.html', {'form': form})

def generate(request): 
  if(request.headers.get('x-requested-with') == 'XMLHttpRequest'): 
    link = json.load(request)['link']
    #generating a unique shortened link with the UUID.
    uid = str(uuid.uuid4())[:5]
    #Inserting the uid and the link in the database
    url = Links.objects.create(link=link, shortened_link = uid)
    url.save()
    response = {'data' : uid}
    return JsonResponse(response, status = 200)

def load(request, pk): 
  link = Links.objects.get(shortened_link = pk)
  original_link = link.link
  return  redirect(f'https://{original_link}')