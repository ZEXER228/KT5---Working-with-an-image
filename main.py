
import cv2

image = cv2.imread("image.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (7, 7), 0)

edges = cv2.Canny(blur, 100, 200)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

result = image.copy()

cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

cv2.imwrite("result.jpg", result)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
