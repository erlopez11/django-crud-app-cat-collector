from django.shortcuts import render
#Import HttpResponse to send text-based responses
from django.http import HttpResponse

#Define the home view function
#Controlle code in python
# we call these view functions
def home(request):
    #each view function or "view"
    #recieves a request object
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
    #to send a response, we return it!

def about(request):
    contact_details = 'You can reach support at support@catcollector.com'
    return render(request, 'about.html',{
        'contact': contact_details
    }) #this is the same as res.render()
