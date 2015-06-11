import json


class Serializer:
    def deserialize(self, data):
        raise NotImplementedError('.deserialize(data) must be implemented')


class JSONSerializer(Serializer):
    def deserialize(self, data):
        return json.loads(data)