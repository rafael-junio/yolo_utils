"""Generate augmented version of images from a folder full of .jpg"""
import cv2
import os

folder_path = f'/PATH_HERE/'


class Main:

    def run(self):
        for foldername in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, foldername)
            print(f'Data augmentation on > {foldername}')
            for filename in os.listdir(subfolder_path):
                filename_path = os.path.join(subfolder_path, filename)
                img_write_path = os.path.join(subfolder_path, os.path.splitext(f'{filename}')[0])

                if os.path.splitext(f'{filename}')[1] != '.jpg':
                    continue
                img = cv2.imread(filename_path)
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                img_bright = self.change_brightness(hsv)
                self.save_img(img_bright, 'bright', img_write_path)

                img_saturation = self.change_saturation(hsv)
                self.save_img(img_saturation, 'saturation', img_write_path)

                img_rotation = self.change_rotation(hsv, 45)
                self.save_img(img_rotation, 'rotation-45', img_write_path)

                img_rotation = self.change_rotation(hsv, 135)
                self.save_img(img_rotation, 'rotation-135', img_write_path)

                img_zoom = self.change_zoom(hsv)
                self.save_img(img_zoom, 'zoom', img_write_path)

                img_flip = self.change_flip_horizontal(hsv)
                self.save_img(img_flip, 'flip-hor', img_write_path)
        print('Data augmentation done!')

    @staticmethod
    def change_flip_horizontal(image):
        img = cv2.flip(image, 1)
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        return img

    @staticmethod
    def change_brightness(image):
        value_bright = 40
        h, s, v = cv2.split(image)

        lim = 255 - value_bright
        v[v > lim] = 255
        v[v <= lim] += value_bright

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    @staticmethod
    def change_saturation(image):
        value_saturation = 20
        h, s, v = cv2.split(image)

        lim = 180 - value_saturation
        s[s > lim] = 180
        s[s <= lim] += value_saturation

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    @staticmethod
    def change_rotation(img, angle=45):
        h, w = img.shape[:2]
        M = cv2.getRotationMatrix2D((int(w / 2), int(h / 2)), angle, 1)
        img = cv2.warpAffine(img, M, (w, h))
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        return img

    @staticmethod
    def change_zoom(img):
        value = 0.8
        h, w = img.shape[:2]
        h_taken = int(value * h)
        w_taken = int(value * w)
        h_start = 50
        w_start = 50
        img = img[h_start:h_start + h_taken, w_start:w_start + w_taken, :]
        img = cv2.resize(img, (w, h), cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        return img

    @staticmethod
    def save_img(image, transform_type, path):
        cv2.imwrite(f'{path}-{str(transform_type)}.jpg', image)


if __name__ == '__main__':
    Main().run()
