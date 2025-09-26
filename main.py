from PIL import Image
import numpy as np
import sys

BANNER = """
┬─┐┌─┐┌─┐┌─┐┌┬┐┌─┐┬─┐
├┬┘├┤ │  │ │ ││├┤ ├┬┘
┴└─└─┘└─┘└─┘─┴┘└─┘┴└─

[1] Encoder
[2] Decoder
[0] Exit
> """

def encoder(text: str, output_path: str) -> None:
    unicode_codes = [ord(char) for char in text]
    num_chars = len(unicode_codes)
    max_code = max(unicode_codes) if unicode_codes else 0
    if max_code <= 255:
        dtype = np.uint8
        mode = 'L'
    elif max_code <= 65535:
        dtype = np.uint16
        mode = 'I;16'
    else:
        dtype = np.uint32
        mode = 'I'
    
    img_size = int(np.ceil(np.sqrt(num_chars)))
    pixel_data = np.zeros(img_size * img_size, dtype=dtype)
    pixel_data[:num_chars] = unicode_codes
    
    img_array = pixel_data.reshape((img_size, img_size))
    img = Image.fromarray(img_array, mode=mode)
    img.save(output_path)
    print(f"Image saved as {output_path}")
    print(f"Image mode: {mode}, Max character code: {max_code}")

def decoder(input_path: str) -> None:
    img = Image.open(input_path)
    if img.mode == 'L':
        dtype = np.uint8
    elif img.mode == 'I;16':
        dtype = np.uint16
    else:
        dtype = np.uint32
    img_array = np.array(img, dtype=dtype)
    pixel_data = img_array.flatten()
    non_zero_pixels = pixel_data[pixel_data != 0]
    text = ''.join([chr(code) for code in non_zero_pixels])
    print(f"Decoded text:\n{text}")

def read_file(input_file: str, encoding='utf-8') -> str:
    try:
        with open(input_file, "r", encoding=encoding) as f:
            data = f.read()
        return data
    except UnicodeDecodeError:
        encodings = ['utf-8', 'cp1251', 'iso-8859-1', 'latin1']
        for enc in encodings:
            try:
                with open(input_file, "r", encoding=enc) as f:
                    data = f.read()
                print(f"Successfully read with encoding: {enc}")
                return data
            except UnicodeDecodeError:
                continue
        raise ValueError("Cannot decode file with any common encoding")

def choose_input(method: int):
    input_source = int(input("""
[1] From keyboard
[2] From file
[3] Exit
> """))
    if input_source == 1:
        data = input("Enter data to encode: ")
    elif input_source == 2:
        input_file = input("Enter filename: ")
        data = read_file(input_file)
    else:
        sys.exit(0)
    return data

def main() -> None:
    print(BANNER)
    try:
        method = int(input())
        if method == 1:
            data = choose_input(method)
            output_image = input("Enter output image path: ")
            encoder(data, output_image)
        elif method == 2:
            image_path = input("Enter image path: ")
            decoder(image_path)
        else:
            sys.exit(0)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()
