from django.http import HttpRequest


class Handler(object):
    def __init__(self, **kwargs):
        # Go through keyword arguments, and either save their values to our
        # instance, or raise an error.
        for key, value in kwargs:
            setattr(self, key, value)

    def validate_request(self, request):
        raise NotImplementedError('.validate_request(request) must be implemented')

    def extract_data(self, request):
        raise NotImplementedError('.extract_data(request) must be implemented')

    def data(self, request):
        # Make the error obvious if a proper response is not returned
        assert isinstance(request, HttpRequest), (
            'Expected a `HttpRequest`, but received a `%s`'
            % type(request)
        )

        self.validate_request(request)
        return self.extract_data(request)


class WebFormPostHandler(Handler):
    field = 'data'

    def validate_request(self, request):
        assert request.method == 'POST', 'only POST requests allowed'
        assert request.POST and request.POST.__contains__(self.field), (
            'POST form data does not contain key %s'
            % self.field
        )

    def extract_data(self, request):
        return request.POST[self.field]
