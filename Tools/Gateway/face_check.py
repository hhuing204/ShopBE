import numpy as np

def face_check(image: np.ndarray, shop_id: str) -> str:
    #gọi api BE postgre để check
    # return "failure" #sửa thep api BE
    import random
    return random.choice(["success", "failure", "unknown"])
