from django.urls import path, re_path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.article_list,name="list"),
    path('create',views.article_create,name="create"),
    path('delete/<slug>',views.article_delete,name="delete"),
    path('edit/<slug>',views.article_edit,name="edit"),
    path('tag/<slug>',views.TagIndexView,name="tagged"),
    re_path(r'^(?P<slug>[\w-]+)$',views.article_detail,name="detail"),
]
