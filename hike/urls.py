from django.urls import path

from . import views

urlpatterns = [
    # ex: /hike/
    path('', views.index, name='index'),
    path('<int:challenge_id>/', views.challenge, name='challenge'),
    path('search/<str:type>', views.search, name='search'), 
    path('hike_details/<int:hike_id>', views.hike_details, name='hike_details'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]