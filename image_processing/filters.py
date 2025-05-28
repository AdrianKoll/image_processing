from PIL import ImageFilter


def apply_blur(image, radius=2):
    """
    Aplica um desfoque gaussiano à imagem.

    :param image: Objeto Image.
    :param radius: Raio de desfoque.
    :return: Imagem com efeito de desfoque.
    """
    return image.filter(ImageFilter.GaussianBlur(radius))


def apply_sharpen(image):
    """
    Aplica um filtro de nitidez à imagem.

    :param image: Objeto Image.
    :return: Imagem com maior nitidez.
    """
    return image.filter(ImageFilter.SHARPEN)