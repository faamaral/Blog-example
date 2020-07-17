from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from . models import Post
from . forms import Postform
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def hello(request):
    return HttpResponse('Hello World')

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    #context_object_name = 'custom'

class BlogCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    #fields = '__all__'
    #fields = ('title', 'content', 'author')
    form_class = Postform
    success_message = "%(field)s - has sucessfully created!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = Postform
    #fields = ('title', 'content')
    success_message = "%(field) - has sucessfully updated!"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )

class BlogDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "%(field) - has been deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(
            BlogDeleteView, self
        ).delete(request, *args, **kwargs)
