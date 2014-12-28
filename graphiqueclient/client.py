
import requests
from .image import Image, image_from_location_url
from .errors import InvalidImageError, ServerError
import io


class Client:
    """
    A Graphique client.
    """

    def __init__(self, hostname, port):
        self._hostname = hostname
        self._port = port

    def submit_image(self, image_content):
        """
        Submits an image to the server and returns an Image representation of the submitted image.

        :rtype : Image
        :param image_content: a bytes value or a file-like object containing the content of the image
        :return: the submitted image
        :exception InvalidImageError: when the submitted content is not an image or is corrupted
        :exception ServerError: when something evil on the server happens
        """

        # Make sure image content is not empty first
        image_bytes = image_content if type(image_content) == bytes else image_content.read()
        if not image_bytes:
            raise InvalidImageError

        response = requests.post(
            url="http://{}:{}/images".format(self._hostname, self._port),
            data=io.BytesIO(image_bytes)
        )

        if response.status_code == requests.codes.created:
            return image_from_location_url(response.headers['location'])
        elif response.status_code == requests.codes.bad_request:
            raise InvalidImageError
        elif response.status_code == requests.codes.internal_server_error:
            raise ServerError(response)
        else:
            raise Exception("Response unaccounted for: {}".format(response))

    def create_image(self, image):
        """
        Creates the given image on the server.

        :type image: Image
        """

        url = "http://{}:{}/image/{}".format(self._hostname, self._port, image.tag)
        query_params = {}
        if image.image_format:
            query_params['format'] = image.image_format
        if image.size_within:
            query_params['size-within'] = image.size_within

        response = requests.patch(url, params=query_params)

        if response.status_code == requests.codes.ok:
            return
        elif response.status_code == requests.codes.internal_server_error:
            raise ServerError(response)
        else:
            raise Exception("Response unaccounted for: {}".format(response))

    def __repr__(self):
        return "graphiqueclient.Client(hostname='{}', port={})".format(self._hostname, self._port)