from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import NewsArticle
from .serializers import NewsArticleSerializer

def convert_json_to_python(data):
    news_article_data = {
        'source_id': "Unknown" if data['source']['id'] is None else data['source']['id'],
        'source_name': "Unknown" if data['source']['name'] is None else data['source']['name'],
        'author': "Unknown" if data['author'] is None else data['author'],
        'title': "Unknown" if data['title'] is None else data['title'],
        'description': "Unknown" if data['description'] is None else data['description'],
        'url': data['url'],
        'url_to_image': "https://images.pexels.com/photos/3856050/pexels-photo-3856050.jpeg" if data['urlToImage'] is None else data['urlToImage'],
        'published_at': "Unknown" if data['publishedAt'] is None else data['publishedAt'],
        'content': "Unknown" if data['content'] is None else data['content']
    }
    return news_article_data


@api_view(['POST'])
def add_news(request):
    # Process the POST request data and create a new news article
    request_data = request.data
    articles = request_data.get('articles')
    serialized_articles = []
    validation_errors = []
    for article in articles:
        converted_data = convert_json_to_python(article)  
        # print("Data received:", converted_data)
        serializer = NewsArticleSerializer(data=converted_data)
        if serializer.is_valid():
            try:
                serializer.save()
                serialized_articles.append(serializer.data)
            except IntegrityError as e:
                # Handle UNIQUE constraint violations for 'url_to_image' or 'content' fields
                if 'UNIQUE constraint failed: News_newsarticle.url_to_image' in str(e) or 'UNIQUE constraint failed: News_newsarticle.content' in str(e):
                    continue
                else:
                    validation_errors.append(str(e))
        else:
            for field, errors in serializer.errors.items():
                if field not in ['url_to_image', 'content', 'url']:
                    print(f"Validation errors: Error Reports Processing...\nfield -> {field},\nerror -> {errors}\n\n")
                    print(article)
                    print(converted_data)
                    validation_errors.append({field: errors})

    if validation_errors:
        # Handle any validation errors, other than UNIQUE constraint violations
        return Response(validation_errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("Articles added to Database", status=status.HTTP_201_CREATED)

def convert_python_to_json(serializer):
    result_data = []
    for data in serializer.data:
        src = {
            'id': data.get('source_id'),
            'name': data.get('source_name'),
        }
        data['source'] = src
        data['urlToImage'] = data.get('url_to_image')
        del data['source_id']
        del data['source_name']
        del data['url_to_image']
        result_data.append(data)
    return result_data

@api_view(['GET'])
def get_news(request):
    # Retrieve and return a list of news articles
    articles = NewsArticle.objects.all()
    serializer = NewsArticleSerializer(articles, many=True)
    result_data = convert_python_to_json(serializer)
    return Response(result_data)