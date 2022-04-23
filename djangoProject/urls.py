from django.urls import path, re_path
from . import views, testdb, search, search_post

urlpatterns = [
    path(r'', views.hello),
    path(r'runoob/', views.runoob),
    path(r'insert/', testdb.insert),
    path(r'query/', testdb.query),
    path(r'update/', testdb.update),
    path(r'delete/', testdb.delete),
    path(r'search_from/', search.search_from),
    path(r'search/', search.search),
    path(r'search_post/', search_post.search_post),
    path(r'get_request/', views.get_request),
    path(r'post_request/', views.post_request),
    path(r'other_request/', views.other_request),
    path(r'redirect_request/', views.redirect_request),
    re_path('^index/([0-9]{4})/$', views.index),
    re_path('^index1/([0-9]{4})/([0-9]{2})/$', views.index1),
]