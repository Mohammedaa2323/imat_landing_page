from django.shortcuts import render,redirect

from django.core.mail import send_mail

from django.contrib import messages


# Create your views here.

def index(request):

    context = {}

    return render(request,'index.html',context)


def message(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        
        try:
            send_mail(
                subject=f"Requesting for Contact from {name}",
                message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nCourse: {course}",
                from_email=email,
                recipient_list=['mohammedaa8610@gmail.com'],  
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, "There was an error sending your message. Please try again.")

    return redirect('index')


def privacy(request):

    context = {}

    return render(request,'privacy.html',context)