from django.shortcuts import render
import requests
API_KEY = 'd0b69496c18e463f888a273cb521ea9f'
# Create your views here.
def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)

    articles = data['articles']
    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)
