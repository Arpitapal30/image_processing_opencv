import cv2
import os

def apply_bw_transformation(input_folder="captured_images", output_folder="bw_images"):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            
            if image is None:
                print(f"Error: Could not read {image_path}")
                continue
            
            bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to black and white
            output_path = os.path.join(output_folder, filename) #Gray = 0.3R + 0.59G + 0.11B =>(1)
            cv2.imwrite(output_path, bw_image)
            print(f"Black & White image saved: {output_path}")
    
    print("Black & White transformation complete.")

if __name__ == "__main__":
    apply_bw_transformation()