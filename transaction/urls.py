from django.urls import path
from .views import TransactionAPIView ,TransactionDetails,showall
urlpatterns = [
    path('transaction/',TransactionAPIView.as_view()),
    #path('detail/<int:pk>/',article_detail)
    path('detail/<int:id>',TransactionDetails.as_view()),
    path('showall/<int:id>',showall.as_view())
]
