from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# 11. Utwórz pierwszą funkcję widoku drukująca/zwracająca hello world (pamietaj dodać ją do urls.py - moesz ustawić jej name).
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4


def get_hello(request: WSGIRequest) -> HttpResponse:
    hello = "hello world!"
    return render(request, template_name="hello_world.html", context={"hello_var": hello})

# 12. Utwórz funkcję zwracającą listę stringów. Stringi niech będą losowym UUID dodawanym do listy. Lista niech posiada 10 elementów.
#     a) Zwróć listę jako HTTPResponse (musisz na liście zrobić json.dumps)
#     b) zwróć listę jako JsonResponse

def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return render(request, template_name="dowolna_nazwa.html", context={"elements":uuids})
    #return HttpResponse(f"uuids{uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids":uuids})

# 13. Napisz funkcję przyjmującą argumenty w ściezce (path arguments) i wydrukuj je. Dwa argumenty pierwszy typu int, drugi typu str, trzeci typu slug.

def get_argument_from_path(request: WSGIRequest, x:int, y:str, z:str) -> HttpResponse:
    return HttpResponse(f"X = {x}, Y = {y}, Z = {z}")

# 14. Napisz funkcję przyjmującą argumenty a,b,c jako zapytanie (query arguments <?> [po znaku zapytania]) i wydrukuj je

def get_argument_from_query(request: WSGIRequest) -> HttpResponse:
    a =request.GET.get("a")
    b =request.GET.get("b")
    c =request.GET.get("c")
    return HttpResponse(f"a = {a}, b = {b}, c = {c}")

# 15. Wykonaj zapytanie typu GET, sprawdź czy wykonana została poprawna metoda drukując jakaś informacje w ifie.

@csrf_exempt
def check_http_query_type(request: WSGIRequest) -> HttpResponse:
    # query_type = "unknown"
    # if request.method == "GET":
    #     query_type = "this is GET"
    # elif request.method == "POST":
    #     query_type = "this is POST"
    # elif request.method == "PUT":
    #     query_type = "this is PUT"
    # elif request.method == "DELETE":
    #     query_type = "this is DELETE"
    # return HttpResponse(query_type)
    return render(request, template_name="methods.html", context={})

# 21. Dodaj admin panel tylko dla flagi DEBUG w settings

def get_headers(request: WSGIRequest) -> JsonResponse:
    our_headers = request.headers
    return JsonResponse({"headers": dict(our_headers)})

#22.

@csrf_exempt
def raise_error_for_fun(request: WSGIRequest) -> HttpResponse:
    if request.method != "GET":
        raise BadRequest("method not allowed")
    return HttpResponse("wszystko OK")

