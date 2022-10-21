from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def index(request):
      return render(request,'index.html')

def contact(request):

      if request.method=='POST':
            try:
                  name=request.POST.get('name')
                  email=request.POST.get('email')
                  subject=request.POST.get('subject')
                  message=request.POST.get('message')

                  form_data={
                        'name':name,
                        'email':email,
                        'subject':subject,
                        'message':message,
                  }
                  message = '''
                  From:\n\t\t{}\n
                  Email:\n\t\t{}\n
                  Subject:\n\t\t{}\n
                  Message:\n\t\t{}\n
                  '''.format(form_data['name'],form_data['email'],form_data['subject'],form_data['message'])
                  send_mail('You got a Mail ', message, '' , ['daboyakouba22@gmail.com']) #this will give you a persion info
                  messages.info(request, 'Your message has been sent. Thank you!')
            except :
                  messages.info(request,'Message not sent')
      return render(request,'index.html', {})