from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer 
from api.serializers import AcademicianSerializer

def academician_pagination(queryset, request):
    """
    Add pagination to API data
    """
    paginator = PageNumberPagination()
    paginator.page_size = 10
    results = paginator.paginate_queryset(queryset, request)
    serializer = AcademicianSerializer(results, many=True)
    
    return paginator.get_paginated_response(serializer.data)