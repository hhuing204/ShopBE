from flask import Flask, request, jsonify
import os, base64, numpy as np, cv2
from Tools.Gateway.mqtt_client import *
from Tools.Gateway.face_check import *
from Tools.Gateway.image_utils import *
app = Flask(__name__)

@app.route('/check_face', methods=['POST'])
def check_face_route():
    data = request.get_json()
    if not data or 'images' not in data or 'shop_id' not in data:
        return jsonify({'error': 'Missing data'}), 400

    results = []

    for img_b64 in data['images']:
        img = decode_base64_image(img_b64)
        if img is not None:
            # save_image(img, data['shop_id'], prefix="input")
            result = face_check(img, data['shop_id'])
            results.append(result)

    final = max(set(results), key=results.count) if results else "unknown"
    publish_result(final)
    return jsonify({'result': final}), 200

def start_gateway():
    print(" Gateway đang chạy tại http://localhost:5000/")
    app.run(host='0.0.0.0', port=5000)

# Nếu chạy độc lập, cũng chạy luôn
if __name__ == '__main__':
    start_gateway()
