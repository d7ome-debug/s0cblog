from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text) 
    return render(request, 'base/counter.html', {'amount': amount_of_words})

