from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

from rest_framework.permissions import IsAuthenticated

class indexView(APIView):
    
    def get(self,request):
        context = {
            'ok':True,
            'content':'Servidor activo'
        }
        return Response(context)

class ProductView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        productData = Product.objects.all()
        productSer = ProductSerializer(productData,many=True)
        context = {
            'ok':True,
            'content':productSer.data
        }
        return Response(context)
    
    def post(self,request):
        productSer = ProductSerializer(data=request.data)
        productSer.is_valid(raise_exception=True)
        productSer.save()
        
        context = {
            'ok':True,
            'content':productSer.data
        }
        return Response(context)
    
class ProductDetailView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request,product_id):
        productData = Product.objects.get(pk=product_id)
        productSer = ProductSerializer(productData)
        return Response(productSer.data)
    
    def put(self,request,product_id):
        productData = Product.objects.get(pk=product_id)
        productSer = ProductSerializer(productData,data=request.data)
        productSer.is_valid(raise_exception=True)
        productSer.save()
        return Response(productSer.data)
    
    def delete(self,request,product_id):
        productData = Product.objects.get(pk=product_id)
        productSer = ProductSerializer(productData)
        productData.delete()
        return Response(productSer.data)
    
