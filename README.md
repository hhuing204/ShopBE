## Cấu trúc hệ thống
project_root/
├── main.py # File chính, chạy gateway + xử lý nhận diện
├── gateway.py # Flask server nhận ảnh, gọi face_check
├── Tools/
│ ├── Gateway/
│ │ ├── face_check.py # Hàm kiểm tra khuôn mặt (giả lập/AI)
│ │ ├── mqtt_client.py # Kết nối và gửi MQTT đến Adafruit
│ │ └── image_utils.py # Giải mã và lưu ảnh
│ └── send_image/
│ ├── haarcascade_frontalface_default.xml # Mô hình phát hiện mặt
│ ├── mac_map.json # Map MAC address → shopID
│ └── send_image.py # Gửi ảnh test từ webcam
├── dataset/ # Ảnh được lưu tạm để huấn luyện / kiểm tra
├── .env # Chứa AIO_USERNAME, AIO_KEY, AIO_HOST...
└── requirements.txt # Thư viện Python cần cài
## Cách chạy hệ thống

### 1. Cài thư viện cần thiết

```bash
pip install -r requirements.txt
```
### 2. Cấu hình .env
AIO_USERNAME=nhatminh1710
AIO_KEY=aio_xxxxxxxxxxxxxxxxxxx
AIO_HOST=io.adafruit.com
AIO_PORT=1883
### 3.Chạy
```bash
python main.py
```