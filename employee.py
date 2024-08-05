import cv2
import dlib
import time
from playsound import playsound

# Inisialisasi detektor wajah dlib
detector = dlib.get_frontal_face_detector()

# Buka kamera (0 untuk kamera default)
cap = cv2.VideoCapture(0)

# Waktu terakhir wajah terdeteksi
last_detection_time = time.time()

# Batas waktu tanpa deteksi (dalam detik)
timeout_duration = 5

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()
    
    # Ubah frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Deteksi wajah
    faces = detector(gray)
    
    if faces:
        # Jika wajah terdeteksi, perbarui waktu terakhir deteksi
        last_detection_time = time.time()
    else:
        # Jika tidak ada wajah yang terdeteksi, cek waktu terakhir deteksi
        current_time = time.time()
        if current_time - last_detection_time > timeout_duration:
            # Jika lebih dari timeout_duration detik, mainkan peringatan suara
            playsound('alert.wav')
            last_detection_time = current_time  # Reset waktu deteksi untuk menghindari pemutaran terus-menerus
    
    # Gambar persegi panjang di sekitar wajah yang terdeteksi
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Tampilkan frame dengan wajah yang terdeteksi
    cv2.imshow('Live Camera - Face Detection', frame)
    
    # Hentikan jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan capture dan tutup jendela
cap.release()
cv2.destroyAllWindows()
