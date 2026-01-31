"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include

def index_page(request):
	return HttpResponse("""
	    <h1>Онлайн-библиотека</h1>
        <p><a href="/books/">Перейти в каталог книг</a></p>
        <p><a href="/admin/">Админка</a></p>
	""")
urlpatterns = [
    path('admin/', admin.site.urls),
	path('books/', include('books.urls')),
	path('', index_page)
]
