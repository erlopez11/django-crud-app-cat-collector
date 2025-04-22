from django.shortcuts import render
from .models import Cat

#Define the home view function
#Controlle code in python
# we call these view functions
def home(request):
    #each view function or "view"
    #recieves a request object
    return render(request, 'home.html')
    #to send a response, we return it!

def about(request):
    contact_details = 'You can reach support at support@catcollector.com'
    return render(request, 'about.html',{
        'contact': contact_details
    }) #this is the same as res.render()

def cat_index(request):
    cats = Cat.objects.all() #similar to what we used in shell in ORM (previous module)
    return render(request, 'cats/index.html', {
        'cats': cats
    }) #context dictionary {'cats', cats}

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {
        'cat': cat
    })
