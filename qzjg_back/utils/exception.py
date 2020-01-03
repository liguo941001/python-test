from rest_framework.views import exception_handler as df_exception_handler
from rest_framework import status
from rest_framework.response import Response
from .logging import logger


def exception_handle(exc, context):
    response = df_exception_handler(exc, context)
    if response is None:
        view = context['view']
        logger.error('%s:%s' % (view, exc))
        response = Response({'detail': '服务器内部错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response
