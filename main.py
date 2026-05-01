import network
import time

class OfflineModeDetector:
    def __init__(self):
        self.last_connection_time = 0

    def check_offline_mode(self):
        try:
            network.isconnected()
            self.last_connection_time = time.time()
            return False
        except Exception as e:
            if time.time() - self.last_connection_time > 60:
                return True
            else:
                return False

detector = OfflineModeDetector()

def main():
    while True:
        if detector.check_offline_mode():
            print("Offline mode detected")
        else:
            print("Online mode detected")
        time.sleep(1)

if __name__ == "__main__":
    main()
```

Kodda quyidagilar qo'llaniladi:

- `network` moduli orqali internetga ulanishni tekshirish uchun `isconnected()` funksiyasi qo'llaniladi.
- `time` moduli orqali vaqt hisoblash uchun `time.time()` funksiyasi qo'llaniladi.
- Offline modega qarshi tekshirish uchun `check_offline_mode()` metodi yaratiladi.
- Offline modega qarshi tekshirish uchun 1 dan 60 soniga qadar davom etadigan davr yaratiladi.
- Offline modega qarshi tekshirish uchun 1 sonidan keyin yana tekshirish uchun `time.sleep(1)` funksiyasi qo'llaniladi.
