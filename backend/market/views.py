from .serializers import ProductSerializer, ClientSerializer, TypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Client, Type
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

class ProductListApiView(APIView):
    def get(self, request, *args, **kwargs):
        if "type" in request.GET:
            todos = Product.objects.filter(type_product__name=request.GET.get('type')).order_by('-price')
        else:
            todos = Product.objects.all().order_by('-price')
        if todos.count() > 0:
            serializer = ProductSerializer(todos, context={"request": request}, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"empty": True}, status=status.HTTP_200_OK)

class TypeListApiView(APIView):
    def get(self, request, *args, **kwargs):
        todos = Type.objects.all()
        if todos.count() > 0:
            serializer = TypeSerializer(todos, context={"request": request}, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"empty": True}, status=status.HTTP_200_OK)

class ClientListApiView(APIView):
    def get(self, request, *args, **kwargs):
        todos = Client.objects.all()
        if todos.count() > 0:
            serializer = ClientSerializer(todos, context={"request": request}, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"empty": True}, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            cart = []
            myData = dict(request.data)
            for prod_id in myData['cart']:
                try:
                    prod = Product.objects.get(id=int(prod_id['id']))
                    cart.append(prod)
                except ObjectDoesNotExist:
                    pass
            serializer.save(cart=cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)