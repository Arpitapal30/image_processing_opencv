import cv2
import os

def apply_edge_detection(input_folder="captured_images", output_folder="edge_images"):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            
            if image is None:
                print(f"Error: Could not read {image_path}")
                continue
            
            edges = cv2.Canny(image, 100, 200)  # Apply Canny edge detection
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, edges)
            print(f"Edge detected image saved: {output_path}")
    
    print("Edge detection complete.")

if __name__ == "__main__":
    apply_edge_detection()
