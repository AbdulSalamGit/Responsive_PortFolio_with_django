from django.shortcuts import render, redirect
from .models import ContactMessage
from django.http import HttpResponseRedirect


def home(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def skills(request):
    return render(request, "skills.html")


def projects(request):
    return render(request, "projects.html")


def about(request):
    return render(request, "about.html")


def view_contact(request):
    messages = ContactMessage.objects.all()
    return render(request, "view_contact.html", {"messages": messages})


def contact(request):
    n = ""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("text")
        message = request.POST.get("msg")
        try:
            contact_message = ContactMessage(
                sender_name=name,
                sender_email=email,
                subject=subject,
                message=message,
            )
            contact_message.save()
            n = "Data Successfully Inserted"
        except Exception as e:
            n = "Not Inserted: {}".format(str(e))

    return render(request, "contact.html", {"n": n})
