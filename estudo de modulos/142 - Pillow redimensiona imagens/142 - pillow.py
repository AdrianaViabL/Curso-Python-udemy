import os
from PIL import Image


def main(main_images_folder, new_width):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe.')

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extention = os.path.splitext(file)  # separando o nome do arquivo de sua extencao

            converted_tag = '_converted'

            new_file = file_name + converted_tag + extention
            new_file_full_path = os.path.join(root, new_file)
            # if converted_tag in file_name:  #para apagar as novas imagens
            #     os.remove(file_full_path)
            #continue

            if os.path.isfile(new_file_full_path):
                print(f'Arquivo {new_file_full_path} ja existe')
                continue

            if converted_tag in file_full_path:
                continue

            img_pillow = Image.open(file_full_path)
            exif = img_pillow.getexif()  #para ver as informaçõe da foto(so funciona em fotos)
            # print(exif.get(36867)) #chave para ver a data que a foto foi tirada
            # continue
            width, height = img_pillow.size
            new_height = round(new_width * height / width)  # feito uma regra de tres para pegar a nova altura
            print(width, new_width, height, new_height)
            new_image = img_pillow.resize((new_width, new_height), Image.LANCZOS)
            try:
                new_image.save(
                    new_file_full_path,
                    optimize=True,
                    quality=50,
                    exif=img_pillow.info.get('exif')
                )
            except:
                try:
                    new_image.save(
                        new_file_full_path,
                        optimize=True,
                        quality=50,
                    )
                except:
                    raise RuntimeError(f'Could not convert "{file_full_path}".')
            print(f'{file_full_path} convertido com sucesso')
            new_image.close()
            img_pillow.close()


if __name__ == '__main__':
    main_images_folder = '/home/adriana/Documents/GitHub/Curso Python udemy/estudo de modulos/142 - Pillow redimensiona imagens/imagens'
    main(main_images_folder, new_width=500)
