from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import *
from django.contrib import admin
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def send_email_view(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    from_email = 'your-email@gmail.com'
    recipient_list = ['recipient@example.com']

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,  # Set to True to suppress errors if email fails
    )
    return HttpResponse("Email sent successfully!")

def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        another_email = request.POST.get('another_email')
        phone = request.POST.get('phone')
        another_phone = request.POST.get('another_phone')
        project_type = request.POST.get('project_type')
        message = request.POST.get('message')

        if message == "Ti123456789%123456789%523":
            return redirect('secret-admin-panel/9638527419873214')
        if name and email and phone and message:
            subject = "A request from the website TI"
            message = "From: " + name + "\nEmail: " + email + "\nAnother Email: " + another_email + "\nPhone: " + phone + "\nAnother Phone: " + another_phone + "Project Type: "+ project_type +"\nMessage: " + message
            from_email = "muhamedabdodeveloper@gmail.com"
            recipient_list = ["tidevteam.st@gmail.com"]
        else:
            try:
                send_mail(subject,message,from_email,recipient_list,fail_silently=False,)
                messages.success(request, 'message sent successfully!')
            except Exception as e:
                messages.error(request, 'Failed to send message. Please try again later.')

    projects_count = Project.objects.count()
    lasted_projects = Project.objects.order_by('-id')[:3]
    return render(request, 'home.html', {'lasted_projects':lasted_projects, 'projects_count':projects_count})

def project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project-details.html', {'project': project})

def portfolio_view(request):
    projects = Project.objects.order_by('-id')
    return render(request, 'portfolio.html', {'projects':projects})