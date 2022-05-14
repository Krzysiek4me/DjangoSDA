"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from books.views import get_hello, get_uuids_a, get_uuids_b, get_argument_from_path, \
    get_argument_from_query, check_http_query_type, get_headers, raise_error_for_fun, AuthorListBaseView, \
    CategoryListTemplateView, BooksListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_hello),
    path('uuids-a', get_uuids_a),
    path('uuids-b', get_uuids_b),
    path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    path('query-args', get_argument_from_query, name="get_from_query"),
    path('http-args', check_http_query_type, name="get_from_type"),
    path('get-headers', get_headers, name="get_headers"),
    path('raise-error', raise_error_for_fun, name="raise_error"),
    path('author-list', AuthorListBaseView.as_view(), name="author-list"),
    path('category-list', CategoryListTemplateView.as_view(), name="category-list"),
    path('books-list', BooksListView.as_view(), name="books-list"),
]

# if settings.DEBUG:
#     urlpatterns.append(path('admin/', admin.site.urls))

