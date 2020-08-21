#app_name = 'j4blog'
from django.urls import path
from . import views


app_name = 'j4blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<str:article_path>', views.article_detail, name='article'),
    path('<str:page_path>', views.page_detail, name='page'),
    path('tag/<str:tag_path>', views.tag_detail_and_list, name='tag'),
    path('category/<str:category_path>', views.category_detail_and_list, name='category')
]
