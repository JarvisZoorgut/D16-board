from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleCreate, UserResponseList

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('<int:pk>', ArticleDetail.as_view(), name = 'article_detail'),
    path('responses/', UserResponseList.as_view()),
]
