from django.urls import path
from django.conf.urls.static import static
from movieapp import settings
from . import views

urlpatterns = [
    path('', views.movieListingPage, name="movielistingpage"),
    path('getpostmoviejson/', views.getPostMovieJson, name='getpostmoviejson'),
    path('moviedetailpage/<int:id>', views.movieDetailPage, name='moviedetailpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)