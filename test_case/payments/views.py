from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .service import create_checkout_session
from .models import Item



class ItemList(View):
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        return render(request, 'payments/item/list.html', {'items': items})


class ItemDetail(View):
    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'payments/item/detail.html', {'item': item})
    

class ItemBuyApi(APIView):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        path = '/'.join(request.build_absolute_uri().split('/')[:3]) # for example: http.127.0.0.1:8000
        session = create_checkout_session(path, item)
        return Response({'session_id': session.id})


class SuccessPayment(TemplateView):
    template_name = 'payments/success.html'
