from django.shortcuts import render
from rest_framework import status
from .serializers import CategorySerializer, ProductsSerializer
from .models import Category, Products
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class ListProductsView(APIView):
    def get(self, request):
        try:
            category = Products.objects.all()
            serializer = ProductsSerializer(category, many=True)
            serializer_data = {
                "data": serializer.data,
                "status": "success",
                "status_code": status.HTTP_200_OK
            }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def post(self, request):
        try:
            serializer = ProductsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "data": serializer.data,
                    "status": "success",
                    "status_code": status.HTTP_200_OK
                }
            else:
                serializer_data = {
                    "data": serializer.errors,
                    "status": "success",
                    "status_code": status.HTTP_200_OK
                }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)




class DetailDeleteUpdateCreateView(APIView):
    def get(self, request, pk):
        try:
            category = Products.objects.get(pk=pk)
            serializer = ProductsSerializer(category)
            serializer_data = {
                "data": serializer.data,
                "status": "success",
                "status_code": status.HTTP_200_OK
            }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def put(self, request, pk):
        try:
            category = Products.objects.get(pk=pk)
            serializer = ProductsSerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "data": serializer.data,
                    "status": "success",
                    "status_code": status.HTTP_200_OK
                }
            else:
                serializer_data = {
                    "error": serializer.errors,
                    "status": "error",
                    "status_code": status.HTTP_404_NOT_FOUND
                }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def patch(self, request, pk):
        try:
            category = Products.objects.get(pk=pk)
            serializer = ProductsSerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "data": serializer.data,
                    "status": "success",
                    "status_code": status.HTTP_200_OK
                }
            else:
                serializer_data = {
                    "data": serializer.errors,
                    "status": "success",
                    "status_code": status.HTTP_200_OK}
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def delete(self, request, pk):
        try:
            category = Products.objects.get(pk=pk)
            serializer = ProductsSerializer(category)
            category.delete()
            serializer_data = {
                "data": serializer.data,
                "status": "deleted",
                "status_code": status.HTTP_200_OK
            }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)


class ListCategoryView(APIView):
    def get(self, request):
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            serializer_data = {
                "data": serializer.data,
                "status": "success",
                "status_code": status.HTTP_200_OK
            }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "data": serializer.data,
                    "status": "success",
                    "status_code": status.HTTP_200_OK
                }
            else:
                serializer_data = {
                    "data": serializer.errors,
                    "status": "success",
                    "status_code": status.HTTP_200_OK
                }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)


class DetailDeleteUpdateCreateCategoryView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            serializer_data = {
                "data": serializer.data,
                "status": "success",
                "status_code": status.HTTP_200_OK
            }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "data": serializer.data,
                    "status": "success",
                    "status_code": status.HTTP_200_OK
                }
            else:
                serializer_data = {
                    "error": serializer.errors,
                    "status": "error",
                    "status_code": status.HTTP_404_NOT_FOUND
                }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def patch(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "data": serializer.data,
                    "status": "success",
                    "status_code": status.HTTP_200_OK
                }
            else:
                serializer_data = {
                    "data": serializer.errors,
                    "status": "success",
                    "status_code": status.HTTP_200_OK}
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            category.delete()
            serializer_data = {
                "data": serializer.data,
                "status": "deleted",
                "status_code": status.HTTP_200_OK
            }
        except Exception as error:
            serializer_data = {
                "error": str(error),
                "status": "error",
                "status_code": status.HTTP_404_NOT_FOUND
            }
        finally:
            return Response(serializer_data)
