from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'slug', 'body']
    #template_name = 'blog/post_form.html'

    def form_valid(self, form):
        print("فرم معتبر بود 😎")
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'slug', 'body']
    template_name = 'blog/post_form.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
