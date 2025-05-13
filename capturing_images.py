import cv2
import os



def capture_images(output_folder="captured_images", num_images=10):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(0)  # Open the default camera
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        image_path = os.path.join(output_folder, f"image_{count}.jpg")
        cv2.imwrite(image_path, frame) # Save the captured frame as an image
        print(f"Captured {image_path}") 
        
        count += 1
        cv2.waitKey(500)  # Wait for 500ms between captures
    
    cap.release()
    cv2.destroyAllWindows()
    print("Image capture complete.")

if __name__ == "__main__":
    capture_images()

