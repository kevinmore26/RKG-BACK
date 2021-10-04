from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginacionPersonalizada(PageNumberPagination):
    
    page_query_param = 'pagina'
    
    page_size = 2
    
    page_size_query_param = 'cantidad'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(data={
            "paginacion": {
                'paginaContinua': self.get_next_link(),
                "paginaPrevia": self.get_previous_link(),
                "total": self.page.paginator.count,
                "porPagina": self.page.paginator.per_page
            },
            "data": {
                "content": data,
                "message": None
            }
        })