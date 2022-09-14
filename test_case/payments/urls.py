from django.urls import path
from .views import ItemList, ItemDetail, ItemBuyApi, SuccessPayment

app_name = 'payments'

urlpatterns = [
    path('', ItemList.as_view(), name='item_list' ),
    path('item/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('success/', SuccessPayment.as_view(), name='success_payment'),
    
    # api
    path('buy/<int:pk>/', ItemBuyApi.as_view()),
]