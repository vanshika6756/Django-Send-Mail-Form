from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email_from = settings.EMAIL_HOST_USER
        org_mail = ['vanshika2115471@akgec.ac.in',]

        subject_user = "Concern Recieved Sucessfully"
        message_user = f"Hello {name}, Your concern has been recieved."
        recipient_list = [email]

        send_mail(subject, message, email_from, org_mail)
        send_mail(subject_user, message_user, email_from, recipient_list)
        # third param is the email address we send mail from , leaveblank (optional) ''
        return HttpResponse('Thank you for subnmitting the from, check email for confirmation')

    return render(request, 'contactform/index.html', {})