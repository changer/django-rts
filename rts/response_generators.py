from django.http import HttpResponse


class ResponseGenerator(object):
    serializer_class = None
    serializer_kwargs = {}

    def get_response(self, obj):
        raise NotImplementedError('.get_response(obj) must be implemented')


class WebFormAutoSubmitGenerator(ResponseGenerator):
    method = 'POST'
    field = 'data'
    action = None

    def get_response(self, obj):
        serializer = self.serializer_class()

        data = serializer.serialize(obj, **self.serializer_kwargs)
        response = HttpResponse(data, content_type='text/xml')

        return response