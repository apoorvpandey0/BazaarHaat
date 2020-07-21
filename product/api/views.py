from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,)
from rest_framework.filters import (SearchFilter,OrderingFilter)
from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination)

from django.db.models import Q
from django_filters import rest_framework as filters

from product.models import Product,Review
from .permissions import IsSeller
from .pagination import ProductLimitOffset,ProductPageNumberPagination,ReviewPageNumberPagination
from .serializers import (
            ProductListSerializer,ProductDetailSerializer,
            ProductCreateSerializer,ProductUpdateStockSerializer,ProductUpdateSerializer,
            ReviewListSerializer,

            )

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    # lookup_field = 'id'   #lookup_field always defaults to ID/Primary Key
    lookup_field_kwarg = 'abc'  #Keyword which is to be passed from URL

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = ProductPageNumberPagination   #ProductLimitOffset  #LimitOffsetPagination #PageNumberPagination

    #Method 1 of search filtering
    filter_backends =(filters.DjangoFilterBackend,SearchFilter,OrderingFilter)
    filterset_fields = ('category', 'stock')
    search_fields = ['tags__name','title','description']

    #Method 2 of Search Filtering
    # def get_queryset(self,*args,**kwrgs):
    #     # quertyset_list = super(PostListAPIView,self).get_queryset(*args,**kwrgs)
    #     queryset_list = Product.objects.all()
    #     query = self.request.GET.get('q').lower()
    #     if query:
    #         queryset_list = Product.objects.filter(
    #           Q(tags__name__in=query) |
    #           Q(title__icontains=query) |
    #           Q(description__icontains=query)).distinct()
    #     return queryset_list

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated]

class ProductUpdateStockAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateStockSerializer
    permission_classes = [IsAuthenticated,IsSeller]


# --------------------------------Reviews-----------------------------------------------------


class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    pagination_class = ReviewPageNumberPagination   #ProductLimitOffset  #LimitOffsetPagination #PageNumberPagination

    #Method 1 of search filtering
    filter_backends =(filters.DjangoFilterBackend,SearchFilter,OrderingFilter)
    filterset_fields = ('id','user','product','rating') #For ?rating=3 or in general ?<fieldname> = <value>
    search_fields = ['id','user','product','rating']
