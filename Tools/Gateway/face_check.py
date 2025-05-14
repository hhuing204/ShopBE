
    
import cv2
import numpy as np
import requests
from io import BytesIO

def face_check(image: np.ndarray, shop_id: str) -> str:
    try:
        url = f"http://localhost:8085/api/v1/user/check-in/{shop_id}"

        # Encode ảnh (giống lưu ra file, nhưng lưu vào RAM)
        success, encoded_img = cv2.imencode('.jpg', image)
        if not success:
            print("❌ Không encode được ảnh")
            return "failure"

        img_bytes = BytesIO(encoded_img.tobytes())  # RAM-based file
        img_bytes.name = "image.jpg"  # Quan trọng: requests cần .name để hiểu MIME

        files = {
            "image_file": ("image.jpg", img_bytes, "image/jpeg")
        }

        response = requests.post(url, files=files)

        if response.status_code == 200:
            result = response.json()
            if result.get("status") == "success":
                return "success"
            else:
                return "failure"
        else:
            print("⚠️ API lỗi mã:", response.status_code)
            return "failure"

    except Exception as e:
        print(f"❌ Lỗi trong face_check: {e}")
        return "failure"

        
    # import random
    # return random.choice(["success", "failure", "unknown"])
