from celery import shared_task,task
from celery.task import Task
import requests
import json

from django.http import HttpResponse


from .models import SearchApi

from django.shortcuts import redirect

from django.core import serializers


def data_present(product_id):
        if SearchApi.objects.filter(product_id=product_id).exists():
            return True
        
        return False

@task
def paytm_mall(query, method='get',header={}, page_count=1,item_per_page=10):
    try:
        paytm_mall_url                              = "https://search.paytm.com/v2/search?userQuery="+query+"&page_count="+str(page_count)+"&items_per_page="+str(item_per_page)
        request                                     = requests.get(url = paytm_mall_url)
        response                                    = request.json()
        products                                    = response['grid_layout']
        list_response                               = []
        for product in products:
            if  data_present(product['product_id']):
                searchapi                           = SearchApi.objects.get(product_id=product['product_id'])
                searchapi.product_id                = product['product_id']
                searchapi.product_name              = product['name']
                searchapi.product_search_name       = product['name'].replace(" ","")
                searchapi.image_url                 = product['image_url']
                searchapi.price                     = product['actual_price']
                searchapi.save()

            else:
                searchapi                           = SearchApi(product_id=product['product_id'],product_name=product['name'],product_search_name= product['name'].replace(" ",""),image_url=product['image_url'],price=product['actual_price'])
                searchapi.save()
            list_response.append(searchapi)
        return {'products':serializers.serialize("json", list_response)}
    except Exception as e:
        print("error in paytm",str(e))
        return str(e)

@task
def shop_clues(query, method='get',header={}, page_count=1,item_per_page=10):
    try:
        paytm_mall_url                              = "http://api.shopclues.com/api/v11/search?q="+query+"&z=1&key=d12121c70dda5edfgd1df6633fdb36c0&page="+str(page_count)
        request                                     = requests.get(url = paytm_mall_url)
        response                                    = request.json()
        products                                    = response['products']
        list_response                               = []
        for product in products:
            if  data_present(product['product_id']):
                searchapi                           = SearchApi.objects.get(product_id=product['product_id'])
                searchapi.product_name              = product['product']
                searchapi.product_search_name       = product['product'].replace(" ","")
                searchapi.image_url                 = product['image_url']
                searchapi.price                     = product['price']
                searchapi.save()

            else:
                searchapi                           = SearchApi(product_id=product['product_id'],product_name=product['product'],product_search_name= product['product'].replace(" ",""),image_url=product['image_url'],price=product['price'])
                searchapi.save()
            list_response.append(searchapi)
        return {'products':serializers.serialize("json", list_response)}
    except Exception as e:
        print("error in shop clues",str(e))
        return str(e)

@shared_task
def tata_cliq(query, page_count=0,item_per_page=10):
    pass    

