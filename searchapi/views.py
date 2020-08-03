from django.shortcuts import render

from rest_framework import generics

from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import SearchApi
from .serializers import SearchApiSerializer

from .task import paytm_mall,shop_clues,tata_cliq



# Create your views here.


class Search(generics.ListAPIView):
    serializer_class               = SearchApiSerializer
    search_fields                  = ['product_name']
    query_set                      = SearchApi.objects.all()

    # def get_queryset(self):
    #     qs                         = SearchApi.objects.all()
    #     query                      = self.request.GET.get('q',None)

    #     if query is not None:
    #         query                  = query.replace(" ","")
    #         qs                     = qs.filter(Q(product_search_name__icontains=query))
    #     return qs

    def get(self, request, *args, **kwargs):
        qs                         = SearchApi.objects.all()
        query                      = self.request.GET.get('q',None)

        if query is not None:
            query                  = query.replace(" ","")
            qs                     = qs.filter(Q(product_search_name__icontains=query))
        if query is not None:
            paytm_mall.delay(query)
            shop_clues.delay(query)
        paginator = Paginator(qs, 50)
        page = request.GET.get('page')
 
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
    
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        return render(request, "search.html",context={'products':products})

