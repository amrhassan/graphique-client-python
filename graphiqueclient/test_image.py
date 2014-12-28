from unittest import TestCase
from graphiqueclient.image import Image


class TestImage(TestCase):

    def test_servable_url(self):
        image = Image(tag='superimage.jpg')
        self.assertEquals(
            'http://example.org:8080/superimage-cae556a36c4943f2cdbb592ddc536388.jpg',
            image.formatted_to_jpeg(0.95).sized_within(200, 200).servable_url('example.org', '8080'),
        )
        self.assertEquals(
            'http://example.org:8080/superimage-2afc3be7d8e2ec9079cdd6cbd4543991.png',
            image.formatted_to_png().sized_within(200, 200).servable_url('example.org', '8080'),
        )
        self.assertEquals(
            "http://example.org:8080/superimage.jpg",
            image.servable_url('example.org', '8080'),
        )

    def test_aws_s3_servable_url(self):
        image = Image(tag='superimage.jpg')
        self.assertEqual(
            image.formatted_to_jpeg(0.95).sized_within(200, 200).aws_s3_servable_url('mybucket', 'myprefix/'),
            'https://mybucket.s3.amazonaws.com/myprefix/superimage-cae556a36c4943f2cdbb592ddc536388.jpg'
        )
        self.assertEqual(
            image.formatted_to_png().sized_within(200,200).aws_s3_servable_url('mybucket', 'myprefix/'),
            'https://mybucket.s3.amazonaws.com/myprefix/superimage-2afc3be7d8e2ec9079cdd6cbd4543991.png'
        )
        self.assertEqual(
            image.aws_s3_servable_url('mybucket', 'myprefix/'),
            'https://mybucket.s3.amazonaws.com/myprefix/superimage.jpg'
        )