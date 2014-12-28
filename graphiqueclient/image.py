import hashlib


class Image:

    def __init__(self, tag, size_within=None, image_format=None):
        self._tag = tag
        self._size_within = size_within
        self._image_format = image_format

    @property
    def tag(self):
        """
        The tag of this image.

        :rtype : str
        """
        return self._tag

    @property
    def size_within(self):
        return self._size_within

    @property
    def image_format(self):
        return self._image_format

    def formatted_to_jpeg(self, quality=0.95):
        image_format_str = 'jpeg({})'.format(quality)
        return Image(tag=self.tag, size_within=self.size_within, image_format=image_format_str)

    def formatted_to_png(self):
        return Image(tag=self.tag, size_within=self.size_within, image_format='png')

    def sized_within(self, width, height):
        return Image(tag=self.tag, size_within="{}x{}".format(width, height), image_format=self.image_format)

    def servable_url(self, hostname='localhost', port=9806):
        return "http://{}:{}/{}".format(hostname, port, self._qualified_tag())

    def aws_s3_servable_url(self, bucket, prefix):
        return "https://{}.s3.amazonaws.com/{}{}".format(bucket, prefix, self._qualified_tag())

    def _is_original(self):
        return self.size_within is None and self.image_format is None

    def _qualified_tag(self):
        if self._is_original():
            return self.tag
        else:

            def hashed_attributes():
                size_attribute = 'size-within=' + self.size_within.lower() if self.size_within else ''
                format_attribute = self.image_format.upper() if self.image_format else ''
                return hashlib.md5((format_attribute + size_attribute).encode('utf-8')).hexdigest()

            extensionless_tag, _ = self.tag.split('.')
            return "{}-{}.{}".format(extensionless_tag, hashed_attributes(), self._target_file_name_extension())

    def _target_file_name_extension(self):
        if not self.image_format:
            return self.tag[self.tag.rfind('.')+1:]
        elif self.image_format.startswith('jpeg'):
            return 'jpg'
        elif self.image_format.startswith('png'):
            return 'png'
        else:
            raise RuntimeError("Image format unaccounted for!")

    def __repr__(self):
        return "graphiqueclient.Image(tag='{}')".format(self.tag)


def image_from_location_url(location_url):
    """
    Parses and creates an Image instance out of its URL.

    :type location_url: str
    :rtype : Image
    """
    return Image(tag=location_url[location_url.rfind('/')+1:])
