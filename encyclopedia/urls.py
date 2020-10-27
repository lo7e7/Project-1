from django.urls import path

from encyclopedia import views
app_name = "encylopedia"
urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/pages/<str:name>',views.entry_page,name='entrypage'),
    path('wiki/create-page',views.create_page,name='create'),
    path('wiki/edit-page/<str:page_name>',views.edit_pages,name='edit_page'),
    path('wiki/random-page',views.random_page,name='random'),  
]

