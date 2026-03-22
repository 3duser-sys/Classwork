import cv2
import numpy as np
from tkinter import Tk, filedialog

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0 
        filtered_image[:, :, 0] = 0 
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0 
        filtered_image[:, :, 2] = 0 
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    elif filter_type == "Canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filtered_image = cv2.Canny(gray, 100, 200)
    elif filter_type == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = 3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = 3)
        filtered_image = cv2.magnitude(sobelx, sobely)
    elif filter_type == "laplacian":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filtered_image = cv2.Laplacian(gray, cv2.CV_64F)
    return filtered_image


image_path = filedialog.askopenfilename(
    title="upload boi",
    filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")]
)

image = cv2.imread(image_path)




if image is None:
    print("Error: Image not found.")
else:
    filter_type = "original"

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red")
    print("d - Decrease Blue")
    print("c = Canny edges")
    print("s - Sobel edges")
    print("l - Laplacian edges")
    print("q - Quit")

    while True:
        
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("Color Filter", filtered_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('c'):
            filter_type = "Canny"
        elif key == ord('s'):
            filter_type = "sobel"
        elif key == ord('l'):
            filter_type = "laplacian"
        elif key == ord('q'):
            print("Exiting...")
            break
        
        else:
            print("Invalid Keys! Please use 'r', 'b', 'g', 'i', 'd', 'q'!")

    cv2.destroyAllWindows()