import abc


class ImageReader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_decoded_image(self):
        pass


class DecodedImage:
    def __init__(self, image):
        self._image = image

    def get(self):
        return "Decoded image: " + self._image


class GifDecoder(ImageReader):
    def __init__(self, image):
        self._decoded_image = DecodedImage(image)

    def get_decoded_image(self):
        return self._decoded_image.get()


class JpegDecoder(ImageReader):
    def __init__(self, image):
        self._decoded_image = DecodedImage(image)

    def get_decoded_image(self):
        return self._decoded_image.get()


def main():
    image = "image.jpg"

    if image.endswith("gif"):
        reader = GifDecoder(image)
    elif image.endswith("jpg"):
        reader = JpegDecoder(image)
    else:
        reader = None

    if reader is not None:
        print(reader.get_decoded_image())
    else:
        print("Image type is not supported")


if __name__ == "__main__":
    main()
