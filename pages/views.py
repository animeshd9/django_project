from django.http import HttpResponse

from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def home_view(request,*arg,**kwargs):
    # return HttpResponse("<h1> Hello world</>")
    return render(request,"home.html",{})

def contact_view(request,*arg,**kwargs):
    my_context={
        'text':"This is interesting",
        "number":1223,
        "list":[34,645,66,3,3]
    }
    return render(request,"contact.html",my_context)
