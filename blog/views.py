from django.shortcuts import render,redirect
from django.views.generic import (DeleteView,
 ListView, DetailView,CreateView,UpdateView)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,UserPassesTestMixin)

from .models import Post




def home(request):
    context={
        'posts':Post.objects.all()
        
        }

    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by= 2


class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    success_url='/'
    def form_valid(self,form):   #redirects to blog just created
        form.instance.author=self.request.user
        return super().form_valid(form)
        return True



class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):   #redirects to blog just created
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()#post that we are updtating
        if self.request.user==post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()#post that we are updtating
        if self.request.user==post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':'About'})



    

