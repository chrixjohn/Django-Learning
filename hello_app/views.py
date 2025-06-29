from django.shortcuts import render
from django.http import HttpResponse
from .models import movieinfo
from .forms import movieform

# Create your views here
def print_hello(request):
    # return HttpResponse("Hello, world!")

    # movie_details={
    #     "name": "Spiderman",
    #     "year":1990,
    #     "summary":"good movie in marvel",
    #     'sucess':False,
    # }
    # return render(request,'hello.html',movie_details)
    
    movie_data={'movies':  [{
        "name": "Spiderman",
        "year":1990,
        
        'sucess':False,
    },{
        "name": "Spider",
        "year":1990,
        "summary":"good movie in marvel",
        'sucess':True,
    },{
        "name": "man",
        "year":1990,
        "summary":"good movie in marvel",
        'sucess':False,
    }]}
    return render(request,'hello.html',movie_data)


def create(request):
    # frm=movieform()
    if request.POST:
        # print(request.POST)
        # print(request.POST.get('title'))
        # print(request.POST.get('year'))
        frm=movieform(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
    else:
        frm=movieform()
        # title=request.POST.get('title')
        # year=request.POST.get('year')
        # # desc=request.POST.get('summary')
        # desc=request.POST.get('description')
        # movie_obj=movieinfo(title=title,year=year,description=desc)
        # movie_obj.save()


    return render(request,'create.html',{'frm':frm})

def list(request):
    # movie_data={'movies':  [{
    #     "name": "Spiderman",
    #     "year":1990,
        
    #     'sucess':False,
    #     'img':'logo.png'
    # },{
    #     "name": "Spider",
    #     "year":1990,
    #     "summary":"good movie in marvel",
    #     'sucess':True,
    #     'img':'logo.png'
    # },{
    #     "name": "man",
    #     "year":1990,
    #     "summary":"good movie in marvel",
    #     'sucess':False,
    #     'img':'logo.png'
    # }]}
    # return render(request,'list.html',movie_data)
    movie_data=movieinfo.objects.all()
    print(movie_data)
    return render(request,'list.html',{'movies':movie_data})
    

def edit(request):
    return render(request,'edit.html')
    
