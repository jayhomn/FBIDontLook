from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('piazzacloud/24', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('piazzacloud/24/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('piazzacloud/24/vote/', views.vote, name='vote'),
]