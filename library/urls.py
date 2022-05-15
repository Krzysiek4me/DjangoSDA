from books.views import get_hello
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', get_hello, name='home'),
    path('books/', include('books.urls')),
    path('users/', include('users.urls')),

]

if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))

