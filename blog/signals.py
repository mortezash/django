from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def notify_new_post(sender, instance, created, **kwargs):
    if created:
        print(f"پست جدید ایجاد شد: {instance.title}")
