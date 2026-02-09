from django.shortcuts import render

def home(request):
    context = {
        'name': 'پایتون',
        'age': 30,
    }
    return render(request, 'blog/home.html', context)
