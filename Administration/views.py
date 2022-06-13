
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from .models import Whatsapp


@csrf_exempt
def message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    data = Whatsapp(user = user,message= message)
    data.save()
    
    response = MessagingResponse()
    response.message('What do you think of my Whatsapp Questions application?')
    return HttpResponse(str(response))

def Index(request):
    context = Whatsapp.objects.all()
    return render(request,'index.html',{'context ':context })


