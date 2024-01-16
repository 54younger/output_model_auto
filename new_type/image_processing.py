import os
import cv2
import numpy as np




if __name__ == "__main__":

    folder_path = "./img"
    output_folder = "./img/resize"

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path)
            height, width, _ = img.shape
            side_length = int(max(height, width) * 2)
            background = np.zeros((side_length, side_length, 3), dtype=np.uint8)
            x_offset = 0
            y_offset = side_length - height
            background[y_offset:y_offset+height, x_offset:x_offset+width] = img
            output_filename = os.path.splitext(filename)[0] + "_resize.jpg"
            output_path = os.path.join(output_folder, output_filename)
            cv2.imwrite(output_path, background)
