import cv2
import numpy as np
import base64
import requests

def face_check(image: np.ndarray, shop_id: str) -> str:
    #gọi api BE postgre để check
    # return "failure" #sửa thep api BE
    """
    try:
        # Encode image to base64
        _, buffer = cv2.imencode('.jpg', image)
        img_base64 = base64.b64encode(buffer).decode('utf-8')

        # Prepare payload
        payload = {
            "shop_id": shop_id,
            "image": img_base64
        }

        # Send POST request to backend API
        response = requests.post("http://your-backend-api/face-check", json=payload)

        if response.status_code == 200:
            result = response.json()
            if result.get("status") == "success":
                return "success"
            else:
                return "failure"
        else:
            return "failure"
    except Exception as e:
        print(f"Error during face check: {e}")
        return "failure"
    """
    import random
    return random.choice(["success", "failure", "unknown"])
