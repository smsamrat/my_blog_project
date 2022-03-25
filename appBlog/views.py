import uuid
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView,View,ListView,DetailView,TemplateView,UpdateView,DeleteView
from appBlog.models import Blog,Comment,Likes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from appBlog.forms import CommentForm


# Create your views here.

class CreateBlogs(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'app_blog/create_blogs.html'
    fields =('blog_title','blog_content','blog_images',)
    
    def form_valid(self, form):
        obj_Blog = form.save(commit=False)
        obj_Blog.user = self.request.user
        title = obj_Blog.blog_title
        obj_Blog.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())# here title name replace with slug as same name of title
        obj_Blog.save()
        return HttpResponseRedirect(reverse('index'))

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'app_blog/blog.html'


def blogs_details(request,slug):
    blog_details_page= Blog.objects.get(slug = slug)
    comment_form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog_details_page, user=request.user)
    if already_liked:
        liked =True
    else:
        liked=False
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_obj = comment_form.save(commit=False)
            comment_obj.user = request.user
            comment_obj.blog=blog_details_page
            comment_form.save()
            return HttpResponseRedirect(reverse('blog_details', kwargs={'slug':slug}))
    context ={
        'blog_details_page':blog_details_page,
        'comment_form':comment_form,
        'liked':liked ,
    }
    
    return render(request,'app_blog/blog_details.html',context)

def blog_likes(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_post = Likes(blog=blog, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('blog_details', kwargs={'slug':blog.slug}))

def blog_unlikes(request, pk):
    blog=Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user = user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog_details', kwargs={'slug':blog.slug}))







