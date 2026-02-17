from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm

@login_required
def my_dashboard(request):
    return render(request, 'dashboard.html')

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')  # بعد از ثبت‌نام به صفحه ورود هدایت می‌شود