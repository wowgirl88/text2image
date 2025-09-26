# Text2Image Steganography Tool

A Python-based steganography tool that encodes text into images and decodes text from images using Unicode character representation.

## Features

- **Text Encoding**: Convert text into image format by storing Unicode characters as pixel values
- **Text Decoding**: Extract hidden text from encoded images
- **Multiple Data Sources**: Support for both keyboard input and file input
- **Automatic Encoding Detection**: Smart handling of different file encodings
- **Efficient Storage**: Optimized image size based on text length
- **Cross-Platform**: Works on any system with Python 3.x

## How It Works

### Encoding Process
1. Text is converted to Unicode code points
2. The maximum Unicode value determines the pixel depth (8-bit, 16-bit, or 32-bit)
3. An optimally sized square image is created to store the data
4. Unicode values are stored as pixel intensities in the image

### Decoding Process
1. Image is loaded and pixel values are extracted
2. Non-zero pixel values are converted back to Unicode characters
3. Original text is reconstructed from the character codes

## Installation

### Prerequisites
- Python 3.6 or higher
- PIL (Pillow) library
- NumPy library

### Dependencies Installation
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application
```bash
python main.py
```

### Menu Options

1. **Encoder**: Encode text into an image
   - Choose input method (keyboard or file)
   - Specify output image path

2. **Decoder**: Decode text from an image
   - Provide path to encoded image

3. **Exit**: Close the application

### Supported File Encodings
The tool automatically detects and handles multiple text encodings:
- UTF-8
- CP1251
- ISO-8859-1
- Latin1

## Technical Details

### Image Modes
- **L**: 8-bit grayscale (for Unicode values ≤ 255)
- **I;16**: 16-bit grayscale (for Unicode values ≤ 65535)
- **I**: 32-bit grayscale (for larger Unicode values)

### File Structure
```
main.py - Main application file
```

## Limitations

- Encoded images may be larger than the original text file
- Very large texts will generate large images
- Image format must support the required bit depth

## Use Cases

- Secure text storage in image format
- Educational purposes for steganography concepts
- Data hiding in seemingly normal images
- Text backup in visual format

## Security Notes

This tool provides basic steganography functionality. For secure communications, consider additional encryption methods before encoding text into images.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.
