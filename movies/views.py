from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from movies.models import Movies
from movies.serializers import MyModelSerializer
# Create your views here.

@csrf_exempt
def getPostMovieJson(request):
    if request.method == 'GET':
        data = MyModelSerializer(Movies.objects.all(), many=True).data
        return JsonResponse(data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MyModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def movieListingPage(request):
    data = Movies.objects.all()
    context = {
        'data': data,
    }
    return render(request, "movie_listing_page.html", context)

def movieDetailPage(request, id):
    try:
        a = Movies.objects.get(id=id)
    except Movies.DoesNotExist:
        a = None
    context = {
        'a': a,
    }
    return render(request, "movie_detail_page.html", context)