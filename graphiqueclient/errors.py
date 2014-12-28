
class GraphiqueError(Exception):
    pass


class InvalidImageError(GraphiqueError):
    pass


class ImageNotFoundError(GraphiqueError):
    pass


class ServerError(GraphiqueError):

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return self.response.text