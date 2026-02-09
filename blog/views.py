from django.shortcuts import render

def home(request):
    context = {
        'name': 'Python',
        'age': 30,
        'skills' : ['Python', 'Django', 'Docker']
    }
    return render(request, 'blog/home.html', context)
