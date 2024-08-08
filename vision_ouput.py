import cv2
class VisualOutput:
    def display_text(self, text):
        # Code to display text on screen
        print(f"Displaying on screen: {text}")

    def display_image(self, image_path):
        # Code to display image on screen
        img = cv2.imread(image_path)
        cv2.imshow('Product Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
