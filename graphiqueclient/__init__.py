
from .client import Client
from .image import Image, image_from_location_url


def create_client(hostname='localhost', port=8980):
    """
    Creates a Client instance that connects to the provided hostname and port.

    :type port: int
    :type hostname: str
    :rtype : Client
    """
    return Client(hostname, port)


def image_tagged_with(tag):
    """
    Creates an Image instance for the specified tag and returns it.

    The servable URL for an image can be retrieved via the methods Image.servable_url() and
    Image.aws_s3_servable_url(), but those calls do not guarantee the existence of the image and an explicit
    call to Client.create_image(image) must be made at some point prior to using the image's servable URL.

    :rtype : Image
    :type tag: str
    :param tag: the identifying image tag
    :return: an Image instance
    """
    return Image(tag=tag)