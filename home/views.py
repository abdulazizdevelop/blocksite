from django.shortcuts import render ,redirect
from .models import Banner, ContactPersonal, Testimonial 
from .forms import Contact_form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
# from templates import register
# Create your views here.

def Homepage(request):
    # if request.POST:
    #     name = request.POST['nname'],
    #     email = request.POST['email'],
    #     message = request.POST['message'],
    #     contact = Contact(name=name , email=email , message=message)
    #     contact.save
    contactForm = Contact_form(request.POST)
    if request.POST and contactForm.is_valid():
        contactForm.save()
    banner= Banner.objects.all()
    salom = Testimonial.objects.all()
    # con = Contact1.objects.all()
    
    if len(banner) ==1:
        banner_cler=banner  
    else:
        banner_cler =banner[len(banner)-2:] 
    context={
        'banner' :banner_cler, 
        'salom' : salom, 
     }
    return render(request, 'index.html' ,context)
    
def Aboutpage(request):
    context={}
    return render(request ,'about.html' ,context)


def Servecepage(request):
    context={}
    return render(request ,'service.html' ,context)


def Contactpage(request):
    contactForm = Contact_form(request.POST)
    if request.POST and contactForm.is_valid():
        contactForm.save()
    contact_personal = ContactPersonal.objects.all()
    context={
        'contact_personal' : contact_personal
    }
    return render(request, 'contact.html' ,context)

def register(request):
    if request.method=="POST" :
   
        first_name = request.POST.grt('firstname')
        last_name = request.POST.grt('laststname')
        phone = request.POST.grt('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        user = User.objects.filter(username = phone )

        if user :
            messages.warning( request , 'the user  alredy exists  ' )
        else :
            if password==password2 :
                instance = User.objects.create_user(user=phone,first_name=first_name ,last_name=last_name ,  password=password)
                user = authenticate(first_name=first_name ,last_name=last_name , user=phone, password=password)
                
            else :
                messages.warning(request, 'this is incorrect password , please recheck it')
                return redirect('/')
    return render(request, 'register.html' , {}) 