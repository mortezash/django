from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)   # عنوان پست
    body = models.TextField()                  # متن پست
    slug = models.SlugField(unique=True, blank=True)  # ← حتما اضافه کن
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)      # تاریخ آخرین ویرایش

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            n = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # بعد از ایجاد یا ویرایش پست، redirect میشه به صفحه جزئیات خودش
        return reverse("blog:post_detail", args=[self.slug])

