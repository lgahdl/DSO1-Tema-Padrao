from api.data.DAO import DAO
from api.model.Request import Request


class RequestDAO(DAO):
    def __init__(self):
        super().__init__('requests.pkl')

    def add(self, index, request: Request):
        if (isinstance(request.id_request, int)) and (request is not None) \
                and isinstance(request, Request) and (index == request.id_request):
            super().add(index, request)

    def get(self, index: int):
        if index is not None and isinstance(index, int):
            return super().get(index)

    def remove(self, index):
        if index is not None and isinstance(index, int):
            return super().remove(index)
