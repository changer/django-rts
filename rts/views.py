from django.http.response import HttpResponse
from django.views.generic import View


class RtsView(View):
    request_handler_class = None

    def dispatch(self, request, *args, **kwargs):
        request_handler = self.request_handler_class()

        obj = request_handler.get_object(request)

        return HttpResponse(obj)
