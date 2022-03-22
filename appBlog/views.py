import uuid
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView,View,ListView,DetailView,TemplateView,UpdateView,DeleteView
from appBlog.models import Blog,Comment,Likes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



class CreateBlogs(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'app_blog/create_blogs.html'
    fields =('blog_title','slug','blog_content','blog_images',)
    
    def form_valid(self, form):
        obj_Blog = form.save(commit=False)
        obj_Blog.user = self.request.user
        title = obj_Blog.blog_title
        obj_Blog.slug = title.replace('','_')+ "_" + str(uuid.uuid4())# here title name replace with slug as same name of title
        obj_Blog.save()
        return HttpResponseRedirect(reverse('index'))


def Blog(request):
    return render(request,'app_blog/blog.html',context={})

