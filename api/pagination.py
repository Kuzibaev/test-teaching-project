import math

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = "page_size"

    def get_paginated_response(self, data, **kwargs):
        current_page = self.page.number
        num_pages = math.ceil(self.page.paginator.count / self.page.paginator.per_page)

        previous_page = current_page - 1 if current_page > 1 else None
        next_page = current_page + 1 if current_page < num_pages else None

        response_data = {
            'count': self.page.paginator.count,
            'pages': num_pages,
            'previous': previous_page,
            'next': next_page,
            **kwargs,
            'results': data,
        }

        return Response(response_data)

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'pages': {
                    'type': 'integer',
                    'example': 5,  # Replace with an appropriate example value
                },
                'previous': {
                    'type': 'integer',
                    'nullable': True,  # Allows for a null value
                    'example': 4,  # Replace with an appropriate example value
                },
                'next': {
                    'type': 'integer',
                    'nullable': True,  # Allows for a null value
                    'example': 6,  # Replace with an appropriate example value
                },
                'results': schema,
            },
        }
