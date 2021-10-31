from django.db.models.query_utils import select_related_descend
from shop.models.product import Product
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
# from django.http import JsonResponse
from shop.models.customer import Customer
from shop.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

# print(make_password('1234'))
# Create your views here.
 
class Team(View):
    def get(self, request):
        
       return render(request,'team.html')