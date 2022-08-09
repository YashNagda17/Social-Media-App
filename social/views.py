from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from social import models,forms
from django.db.models import Q
# Create your views here.
class Wall(LoginRequiredMixin,ListView):
    
    context_object_name= 'posts'
    template_name = 'social/wall.html'
    login_url = 'auth/login'
    def get_queryset(self):
        friendId = [friends.person2 for friends in models.Friends.objects.filter(person1 = self.request.user)]
        friendId = friendId + [friends.person1 for friends in models.Friends.objects.filter(person2 = self.request.user)]
        return models.Post.objects.filter(user__in = friendId).order_by('-created_at')

        
class Home(LoginRequiredMixin,ListView):
    context_object_name= 'posts'
    template_name = 'social/home.html'
    login_url = 'auth/login'
    def get_queryset(self):
        return models.Post.objects.filter(user = self.request.user).order_by('-created_at')
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['post_form'] = forms.PostForm()
        return data
    
class Post(View):
    def get(self, request):
        return redirect('/home/')
    
    def post(self, request):
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
        return redirect('/home/')
        
        
class PostLike(View):
    model = models.Post
    def post(self,request,pk):
        post = self.model.objects.get(pk=pk)
        models.Likes.objects.create(user = request.user, post = post)
        return HttpResponse(status = 204)

class PostComment(View):
    model = models.Post
    
    def post(self,request,pk):
        post = self.model.objects.get(pk=pk)
        form =forms.PostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponse(status = 204)
        print(form.errors)
        return HttpResponse(status = 400)
        

    
    
    
    