from django.http.response import HttpResponse
from django.views.generic import View


class RtsView(View):
    request_handler_class = None
    serializer_class = None

    def dispatch(self, request, *args, **kwargs):
        request_handler = self.request_handler_class()
        serializer = self.serializer_class()

        data = request_handler.data(request)
        obj = serializer.deserialize(data)

        return HttpResponse(obj)
