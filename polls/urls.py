from django.urls import path
from . import views

# app_name defines a namespace used in reverse url mapping, e.g. 'polls:index'
app_name = "polls"
urlpatterns = [
    path("",views.index, name="index"),
    # View poll choices and vote
    path('<int:question_id>/', views.detail, name='detail'),
    #note: ClassView.as_view() requires pk as parameter, not question_id
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),
    # Class-based view doesn't have all the values the template needs
    #path('<int:pk>/results/',views.ResultsView.as_view(), name='results'),
    path('json/', views.get_questions_as_json),
    #
    # Some Class-based views
    #
    path('list/', views.PollListView.as_view(), name='list'),
]
