from .serializers import ProductSerializer, SaleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Sale
from rest_framework import status
from django.db.models import Q


@api_view(['GET'])
def search_product(request):
    query = request.query_params.get('q', '')
    products = Product.objects.filter(
        Q(title__icontains=query)
    )
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_detail(id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def add_sale(request):
    product_id = request.data.get('product_id')
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Producto No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
    sale = Sale(product=product)
    sale.save()

    return Response({'success': True}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_sales(request):
    sales = Sale.objects.all()
    serializer = SaleSerializer(sales, many=True)
    return Response(serializer.data)