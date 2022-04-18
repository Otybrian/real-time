from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'), 
    path('profile/', views.profile, name='profile'),
    path('new_neighbor',views.new_neighbor, name= 'new_neighbor'),
    path('neighborhood', views.neighborhood, name = 'neighborhood'),
    path('hood/<str:name>',views.single_hood,name='single_hood'),
    path('join_hood/<int:id>', views.join_hood, name='join'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave'),
    path("business/create/", views.create_business, name="create_business"), # create business
    path('business/', views.business, name = 'business'),
    path('search/', views.search, name='search_results'),
    path('post/new-post', views.create_post, name='create_post'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)