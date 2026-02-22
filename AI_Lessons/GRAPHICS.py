import cv2
import numpy as np

image = cv2.imread('example.jpg')
resized = cv2.resize(image, (500, 500))
glow = cv2.GaussianBlur(resized, (15, 15), 0)
ultra_image = cv2.addWeighted(resized, 0.8, glow, 0.2, 0)
edges = cv2.Canny(cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY), 100, 200)
edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
ultra_image = cv2.addWeighted(ultra_image, 0.9, edges_colored, 0.1, 0)
cv2.imshow("💥 ULTRA Image 💥", ultra_image)
key = cv2.waitKey(0)
if key in [ord('s'), ord('S')]:
    cv2.imwrite('ultra_image.jpg', ultra_image)
    print("✅ Ultra image saved as 'ultra_image.jpg'")
else:
    print("❌ Image not saved")
cv2.destroyAllWindows()
print(f"Ultra Image Dimensions: {ultra_image.shape}")
