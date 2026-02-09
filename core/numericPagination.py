from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math

class NumericPagination(PageNumberPagination):
    page_size = 5                 
    page_query_param = "page"      
    max_page_size = 100

    def get_paginated_response(self, data):
        total_pages = math.ceil(self.page.paginator.count / self.page_size)

        return Response({
            "count": self.page.paginator.count,
            "current_page": self.page.number,
            "total_pages": total_pages,
            "next_page": self.page.next_page_number() if self.page.has_next() else None,
            "previous_page": self.page.previous_page_number() if self.page.has_previous() else None,
            "results": data,
        })
