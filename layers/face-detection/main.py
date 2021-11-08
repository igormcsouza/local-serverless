"""
# Face Detection Script

It gets the image as string (base64 encoded) and return a list of faces found
on the given image. The result is jsonified so be able to be sent through
backend.
"""
import io
import json
from os import getenv
from base64 import b64decode

import cv2
import argh
import numpy
from PIL import Image


def find(image: str = "") -> str:
    """Return the faces found on image."""
    # Return empty string if a image is empty too.
    if image == "":
        return ""

    # Convert the image from base64 into numpy array
    im = io.BytesIO(b64decode(image))
    im = Image.open(im)
    im = numpy.array(im)

    # Detect the faces on the given image.
    detector = cv2.CascadeClassifier(getenv("HAAR_PATH"))
    results = detector.detectMultiScale(im,
                                        scaleFactor=1.05,
                                        minNeighbors=5,
                                        minSize=(30, 30),
                                        flags=cv2.CASCADE_SCALE_IMAGE)

    return json.dumps(results.tolist())


# assembling:

parser = argh.ArghParser()
parser.add_commands([find])

# dispatching:

if __name__ == '__main__':
    parser.dispatch()
