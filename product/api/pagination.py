from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination)

#Method 1
class ProductLimitOffset(LimitOffsetPagination):
    max_limit = 10
    default_limit = 2

#Method 2
class ProductPageNumberPagination(PageNumberPagination):
    page_size = 2




class ReviewPageNumberPagination(PageNumberPagination):
    page_size = 2
