from PIL import Image, ExifTags
from django.conf import settings
import datetime
import PIL
import sys
import os, os.path


class ImageResize:

    def __init__(self, image_for=settings.PROPERTIES, folder_path=None, file_image=None,):
        self.path = folder_path if folder_path is not None and folder_path != '' else './'
        self.images = list()
        self.valid_images = [".jpg", ".gif", ".png"]
        self.base_sizes = settings.BASE_IMAGES_SIZES.get(image_for, {})
        self.base_width = self.base_sizes.get('width', 0)
        self.base_height = self.base_sizes.get('height', 0)
        self.limit_size_bytes = 500000  # = 500 kb
        self.files_in_folder = len(os.listdir(self.path))
        self.file = file_image
        self.image_files_in_folder = 0
        self.files_resized = 0
        self.files_with_error = 0

    def get_files_in_folder(self):
        return len(os.listdir(self.path))

    def process_image(self, img):
        width_percent = (self.base_width / float(img.size[0]))
        height_size = int((float(img.size[1]) * float(width_percent)))
        '''
        meta_data_ok = False
        meta_data = None
        try:
            meta_data = img.getexif().items()
            meta_data_ok = True
        except Exception as e:
            print(e)

        if meta_data_ok:

            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(meta_data)

            try:
                if exif[orientation] == 3:
                    img = img.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    img = img.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    img = img.rotate(90, expand=True)
            except Exception as e:
                print(e)
        '''
        resized_img = img.resize((self.base_width, self.base_height), PIL.Image.ANTIALIAS)
        resized_img.save(self.file.path)
        resized_img.close()
        img.close()

    def resize_image(self, image_instance):
        self.path = settings.MEDIA_ROOT
        self.file = image_instance
        img = Image.open(self.file.path)
        #if img.size[0] > self.base_width:
        self.process_image(img)

    def crop_image(self, image_instance):
        self.path = settings.MEDIA_ROOT
        self.file = image_instance
        img = Image.open(self.file.path)

        left = 0
        top = 60
        right = float(img.size[0])
        bottom = float(img.size[1])
        crop_img_result = img.crop((left, top, right, bottom))
        crop_img_result.save(self.file.path)
        crop_img_result.close()
        img.close()

    def resize_images(self):
        print('\nResize Process Start (%s)\n' % datetime.datetime.now())
        for f in os.listdir(self.path):
            ext = os.path.splitext(f)[1]
            if ext.lower() not in self.valid_images:
                continue
            self.image_files_in_folder += 1
            bytes_size = os.stat(os.path.join(self.path, f)).st_size
            if bytes_size > self.limit_size_bytes:
                img = Image.open(os.path.join(self.path, f))
                self.process_image(img)
                self.files_resized += 1

        end = datetime.datetime.now()
        print(''.join(
                [
                    'Resize Process End At %s ',
                    '%s - %s %s' % (end.day, end.month, end.year),
                    ', Files In Folder',
                    str(self.files_in_folder),
                    ', ',
                    'Images In folder',
                    str(self.image_files_in_folder),
                    ', Image Resized  ',
                    str(self.files_resized)
                ]
            )
        )
