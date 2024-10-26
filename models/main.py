''' This is core module of ink-insight. It contains the main class of ink-insight, which is responsible for the main functionality of the application.
    The main.py is the generator of the application.
'''
try:
    import importlib
    import sys
    import os
    import pdf2image as p2i

    from mlstuff.imageclassifier.imager import Imager
except ImportError:
    raise ImportError("mlstuff not found. Please ensure the path is correct before proceeding.")
def main():
    print("Welcome to ink-insight!")
    image_object= Imager('data/2023ac05134.pdf')
    images= image_object.pdf_to_images()
    image_object.save_images(images, 'data/images/')
if __name__ == '__main__':
    main()