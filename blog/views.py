from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.utils.text import slugify
from .forms import PostForm

class PostListView(ListView):
    model = Post
    fields = ['title', 'slug', 'body']
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


    def get_context_data(self, **kwargs): # فرستادن پارامتر اضافی به view
        context = super().get_context_data(**kwargs)  # ← context اصلی رو می‌گیری
        context['title'] = 'All Blog Posts'           # ← یک متغیر اضافی به context اضافه می‌کنیم
        return context

    def get_queryset(self):
        return Post.objects.order_by('-created_at')[:10]  # آخرین‌ها اول , ۱۰ پست آخر


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # ساخت slug خودکار
        form.instance.slug = slugify(form.cleaned_data['title'])
        return super().form_valid(form)



class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_form.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
