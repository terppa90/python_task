from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import ListView
from django.http import JsonResponse
from rest_framework.decorators import api_view


from webshop_api import serializers
from webshop_api.models import CartItem

# Create your views here.

# Works
@api_view(['GET', 'POST'])
def allProducts(request):
    
    if request.method == 'GET':
        allProducts = CartItem.objects.all()
        serializer = serializers.ProductSerializer(allProducts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Works
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = CartItem.objects.get(pk=pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = serializers.ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductApiView(APIView):
#     serializer_class = serializers.ProductSerializer

#     def get(self, request, format=None):
#         """Get all Products"""
#         allProducts = CartItem.objects.all()
#         response = {'products':list(allProducts.values('name', 'price'))}

#         return Response(response)


#     def post(self, request):
#         """Post new Product"""
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request):
    #     product = CartItem.objects.get(pk=pk)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    
    # def get(self, request):
    #     all_products = CartItem.objects.all()
    #     return render(request, "webshop/index.html", {
    #         "products": all_products
    #     })


    # def allProducts(request):
    #     all_products = CartItem.objects.all()
    #     return render(request, "webshop/index.html", {
    #         "products": all_products
    #     })


# class AllProductsView(ListView):
#     template_name = "webshop/index.html"
#     model = CartItem
#     context_object_name = "products"