# main.py
from image_processing import load_image, convert_to_grayscale, apply_blur


def main():
    # Defina o caminho para a imagem de teste
    image_path = "tests/sample.jpg"

    try:
        # Carrega a imagem com a função definida no seu pacote
        img = load_image(image_path)
        print("Imagem carregada com sucesso!")
    except FileNotFoundError:
        print(f"Imagem não encontrada: {image_path}")
        return

    # Converte a imagem para escala de cinza
    gray_img = convert_to_grayscale(img)
    print("Imagem convertida para escala de cinza.")

    # Aplica um filtro de desfoque com raio 3
    blurred_img = apply_blur(gray_img, radius=3)
    print("Filtro de desfoque aplicado.")

    # Exibe as imagens
    gray_img.show(title="Imagem em Escala de Cinza")
    blurred_img.show(title="Imagem com Desfoque")


if __name__ == '__main__':
    main()