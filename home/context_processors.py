from .models import Service ,About, ContactPersonal, Contact

def AboutContext(request):
    data = About.objects.all().last()
    context = {
        'about' : data
    }
    return context


def ServiceContext(request):
    data = Service.objects.all()[:4]
    context = {
        'service' : data
    }
    return context

def ContactPersonalContext(request):
    data = ContactPersonal.objects.all()
    context = {
        'contact_personal' : data
    }
    return context

def ContactContext(request) :
    data = Contact.objects.all()
    context = {
        'contact' : data 
    }
    
    return context
    