# resources/middleware/request_logging.py

import logging

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

# AGREGAR EN MIDDLEWARES  "resources.middlewares.request_logging_middleware.RequestLoggingMiddleware",


class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        method = request.method
        path = request.get_full_path()
        content_type = request.content_type
        body = request.body.decode("utf-8") if request.body else ""
        headers = {k: v for k, v in request.headers.items()}
        metadata = request.META
        cookies = request.COOKIES
        get_params = request.GET.dict()
        data_params = request.POST.dict() if method == "POST" else {}
        json_params = request.data if hasattr(request, "data") else {}

        logging.info(f" -- Method:\n {method}")
        logging.info(f" -- Path:\n {path}")
        logging.info(f" -- Content-Type:\n {content_type}")
        logging.info(f" -- Headers:\n {headers}")
        logging.info(f" -- Metadata:\n {metadata}")
        logging.info(f" -- Cookies:\n {cookies}")
        logging.info(f" -- GET Params:\n {get_params}")
        logging.info(f" -- POST Params:\n {data_params}")
        logging.info(f" -- JSON Params:\n {json_params}")
        logging.info(f" -- Body:\n {body}")

        return None
