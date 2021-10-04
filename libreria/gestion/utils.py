from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginacionPersonalizada(PageNumberPagination):
    # es el nombre de la variable que usaremos para indicar el numero de pagina
    page_query_param = 'pagina'
    # es el tamaño de los items por pagina por defecto
    page_size = 2
    # es el nombre de la variable que usaremos para indicar la cantidad de elementos por pagina
    page_size_query_param = 'cantidad'
    # sirve para limitar el tamaño de la pagina (page_size)
    max_page_size = 10

    def get_paginated_response(self, data):
        # data es la informacion que esta siendo paginada
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