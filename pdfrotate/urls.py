from django.urls import path,include
from .views import PDF_Page_Rotate

urlpatterns = [
    path('pdf_rotate/',PDF_Page_Rotate.as_view())
]