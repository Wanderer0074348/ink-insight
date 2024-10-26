try:
    import pdf2image as p2i
    import os
    import sys
except ImportError:
    raise ImportError("pdf2image not found. Please install it using 'pip install pdf2image'")

class Imager:
    def __init__(self, pdf_path, save_dir = 'images'):
        self.pdf_path = pdf_path
        self.save_dir = save_dir
    
    def check_if_pdf(self):
        if self.pdf_path.endswith('.pdf'):
            return True
        return False
    
    def pdf_to_images(self):
        try:
            if not self.check_if_pdf():
                return None
            images = p2i.convert_from_path(self.pdf_path)
        except Exception as e:
            print(f"Error: {e}")
            return -1
        return images
    
    def save_images(self, images, save_dir):
        try:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            for i, image in enumerate(images):
                image.save(os.path.join(save_dir, f"{i}.jpeg"), '')
        except Exception as e:
            print(f"Error: {e}")
            return -1
        return 0

         
        