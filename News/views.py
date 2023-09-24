# from django.shortcuts import render
# from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import NewsArticle
from .serializers import NewsArticleSerializer

# class NewsArticleViewSet(viewsets.ModelViewSet):
#     queryset = NewsArticle.objects.all()
#     serializer_class = NewsArticleSerializer

# def check_and_convert_to_news_article(data):
def convert_json_to_python(data):
    news_article_data = {
        'source_id': "Unknown" if data['source']['id'] is None else data['source']['id'],
        'source_name': data['source']['name'],
        'author': data['author'],
        'title': data['title'],
        'description': data['description'],
        'url': data['url'],
        'url_to_image': data['urlToImage'],
        'published_at': data['publishedAt'],
        'content': data['content']
    }
    return news_article_data


@api_view(['POST'])
def add_news(request):
    # Process the POST request data and create a new news article
    request_data = request.data
    serialized_articles = []
    for data in request_data:
        converted_data = convert_json_to_python(data)  
        # print("Data received:", converted_data)
        serializer = NewsArticleSerializer(data=converted_data)
        if serializer.is_valid():
            serializer.save()
            serialized_articles.append(serializer.data)
        else:
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serialized_articles, status=status.HTTP_201_CREATED)







    # for data in request_data:
    #     print(converted_data)
    #     NewsArticle(**converted_data)
    #     NewsArticle.save()
    # return Response("serializer.data", status=status.HTTP_201_CREATED)
    
    
    
    
    
    # if serializer.is_valid():
    #     serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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