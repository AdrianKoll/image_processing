import unittest
from image_processing.core import load_image, convert_to_grayscale


class TestCore(unittest.TestCase):
    def test_load_and_convert(self):
        # Utilize uma imagem de exemplo (pode ser uma imagem pequena de teste)
        image = load_image("tests/sample.jpg")  # Certifique-se de ter essa imagem na pasta de testes
        self.assertIsNotNone(image)

        grayscale = convert_to_grayscale(image)
        self.assertEqual(grayscale.mode, "L", "A imagem convertida não está em escala de cinza.")


if __name__ == "__main__":
    unittest.main()