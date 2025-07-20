"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Frontend URLs
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('category/<str:category_slug>/', views.category_news, name='category_news'),

    # Custom Admin Panel URLs
    path('myadmin/login/', views.admin_login, name='admin_login'),
    path('myadmin/logout/', views.admin_logout, name='admin_logout'),
    path('myadmin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('myadmin/add-news/', views.add_news, name='add_news'),
    path('news-list/', views.news_list, name='news_list'),  # news list view का path
    path('category/<slug:category_slug>/', views.category_news, name='category_news'),


    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('add/', views.add_news, name='add_news'),  # आपकी खबर जोड़ें वाली view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
