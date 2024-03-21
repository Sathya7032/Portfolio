from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('contact/',contactHandler,name='contactHandler'),
    path('projects/',project, name='project'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_view,name="logout"),
    path('home/logout/', logout_user, name='logout_user'),
    path('home/',home, name='home'),
    path('home/blog/',blogs, name='blog'),
    path('blog/<slug:url>', post),
    path('home/category/<slug:url>',category),
    path('home/profile/',profile,name='profile'),
    path('home/addcat/',addcat,name='addcat'),
    path('note/<slug:url>',noteView),
    path('dairy/<slug:url>',dairyView),
    path('home/news/',news_list, name='news_list'),
]
