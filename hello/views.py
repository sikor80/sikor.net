from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from google.appengine.api import mail

from hello.forms import ContactForm

from views_secret import *


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message_and_email = "From: " + cd['email'] + " Message: " + cd['message']
            mail.send_mail(sender=SENDER_ADDR,
                          to=TO_ADDR,
                          subject="Message from sikor.net",
                          body=
                          "From: " + cd['email'] 
                          + "\n" +
                          "Subject: " + cd['subject'] 
                          + "\n" + 
                          "Message: " + cd['message'])
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent. Thank You!')

            return HttpResponseRedirect('/#contact')
    else:
        form = ContactForm()
    return render(request, 'hello/index.html', {'form': form})


# def home(request):
#     return http.HttpResponse('Hello World!')

# def index(request):
#     a = ""
#     context = {
#             'a': a,
#             }
#     return render(request, 'hello/index.html', context)


