from django.shortcuts import render
from django.http import HttpResponse 

posts=[
    {
        'author':'Kshitij ',
        'title':'Blog Post 1',
        'Content':'First Post by Kshitij',
        'date_posted':'August 30,2019'
        
        },
    
    {
        'author':'Kshitij Kumar ',
        'title':'Blog Post 2',
        'Content':'Second Post by Kshitij',
        'date_posted':'August 28,2019'
        
        }
    
    ]


def home(request):
    context={
        'posts':posts
        }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})



    

