from django.db import models
from django.utils.text import slugify

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
            # اتوماتیک slug ایجاد می‌کنه از عنوان
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
