import cv2
import numpy as np


def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0 
        filtered_image[:, :, 0] = 0
    elif filter_type == "original":
        return image.copy()
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
    elif filter_type == "cartoon":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        )
        color = cv2.bilateralFilter(image, 9, 300, 300)
        filtered_image = cv2.bitwise_and(color, color, mask=edges)

    return filtered_image

    
def main():
    VidCap = cv2.VideoCapture(0)

    if not VidCap.isOpened():
        print("Error: Camera wasn't captured, try connecting one first...\nError Code: E001CAM")
        return
    
    filter_type = "original"
    print("Keys= r=Red, g=Green, b=Blue, s=Sobel, c=Canny, t=Cartoon, q=Quit.")

    while True:
        ret, frame = VidCap.read()
        if not ret:
            print(" Cant recieve Frame.")
            break

        out = apply_color_filter(frame, filter_type)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            filter_type = "red_tint"
        
        elif key == ord('g'):
            filter_type = "green_tint"

        elif key == ord('b'):
            filter_type = "blue_tint"

        elif key == ord('s'):
            filter_type = "sobel"

        elif key == ord('c'):
            filter_type = "Canny"

        elif key == ord('t'):
            filter_type = "cartoon"

        elif key == ord('q'):
            break

    VidCap.release()
    cv2.destroyAllWindows()

        
if __name__ == "__main__":
    main()
    
