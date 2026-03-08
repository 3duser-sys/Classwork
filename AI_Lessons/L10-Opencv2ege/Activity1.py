import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2: 
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Grayscale Image", gray_image)

    print("Select an option")
    print('1. Sanny Edge Detection')
    print('2. Cobel Edge Detection')
    print('3. Laplacian Edge Detection')
    print('4. Gaussian Smothing')
    print('5. Median Filtering')
    print('6. Exit')

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            sobe1_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobe1_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

            combined_sobel = cv2.bitwise_or(sobe1_x.astype(np.uint8), sobe1_y.astype(np.uint8))
            display_image("Sobel Edge Detection", combined_sobel)
        
        elif choice == '2':
            print("Adjust Threshold for Canny. Default: 100, 200")

            lower_threshold = int(input("Enter lower threshold: "))
            upper_threshold = int(input("Enter upper threshold: "))
            edges = cv2.Canny(gray_image, lower_threshold, upper_threshold)
            display_image("Canny Edge Detection", edges)

        elif choice == '3':
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", laplacian)

        elif choice == '4':
            print("Adjust Kernel Size for Gaussian Smoothing. Default: 5")
            kernel_size = int(input("Enter kernel size (odd number): "))
            blurred = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
            display_image("Gaussian Smoothing", blurred)

        elif choice == '5':
            print("Adjust Kernel Size for Median Filtering. Default: 5")
            kernel_size = int(input("Enter kernel size (odd number): "))
            median_blurred = cv2.medianBlur(gray_image, kernel_size)
            display_image("Median Filtering", median_blurred)

        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

interactive_edge_detection('example.jpg')


