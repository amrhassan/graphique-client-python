[![Build Status](https://travis-ci.org/amrhassan/graphique-client-python.svg?branch=master)](https://travis-ci.org/amrhassan/graphique-client-python)

Python Client for [Graphique](https://amrhassan.github.io/graphique)
===========================

### Get from PyPi ###
*TODO*

### Usage ###
```python
import graphiqueclient

# Client instances are thread-safe, and also very lightweight.
# Use however you like.
client = graphiqueclient.create_client(hostname='localhost', port=8980)
```

**Image Submission**
```python
image = client.submit_image(open('/home/amr/an_image.jpg', 'rb'))
print(image.servable_url())
```

**Image Variant Creation**
```python
variant = graphiqueclient.Image(tag='137a07962e49a58b6161ace95bb1b07d.jpg')\
    .sized_within(500, 400).formatted_to_jpeg(0.75)
client.create(image);
print(image.servable_url())
```

**Directly Obtaining a Servable URL for an Image**
```python
# If you are sure that an image variant already exists on the server, you can obtain its
# publicly-servable URL directly without making an explicit request to the server.
variant = graphiqueclient.Image(tag='137a07962e49a58b6161ace95bb1b07d.jpg')\
    .sized_within(500, 400).formatted_to_jpeg(0.75)
print(variant.servable_url())
```
