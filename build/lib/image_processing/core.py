from PIL import Image


def load_image(path):
    """
    Carrega uma imagem a partir do caminho especificado.

    :param path: Caminho para o arquivo da imagem.
    :return: Objeto Image da biblioteca Pillow.
    """
    return Image.open(path)


def convert_to_grayscale(image):
    """
    Converte a imagem para escala de cinza.

    :param image: Objeto Image.
    :return: Imagem em escala de cinza.
    """
    return image.convert("L")