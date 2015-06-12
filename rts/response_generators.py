class ResponseGenerator(object):
    serializer_class = None
    serializer_kwargs = {}

    def get_response(self, request):
        raise NotImplementedError('.get_response(request) must be implemented')


class WebFormAutoSubmitGenerator(ResponseGenerator):
    method = 'POST'
    field = 'data'
    action = None

    def get_response(self, request, obj):
        serializer = self.serializer_class()

        data = serializer.serialize(obj, **self.serializer_kwargs)