from plyer import notification
import time
if __name__ == '__main__':
    while True:
        notification.notify(
            title ="**** Take rest****",
            message="rest is vital for better mental health",
            timeout=5)
        time.sleep(30)
