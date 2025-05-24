from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    if request.method == "GET":
        try:
            name = "AWS Working with API"
            return JsonResponse({"message": name})
        except Exception as e:
            return JsonResponse({
                "message": "AWS not Working with API",
                "error": str(e)
            })
