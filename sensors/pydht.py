import pigpio
import time

pi = pigpio.pi()
if not pi.connected:
    print("Ошибка подключения к pigpio")

pin = 4
pi.set_mode(pin, pigpio.OUTPUT)
pi.write(pin, 0)
time.sleep(0.02)  # Задержка 20 мс — стартовый сигнал
pi.set_mode(pin, pigpio.INPUT)

# Читаем первые 100 уровней сигнала
for i in range(100):
    print(pi.read(pin), end="")
    time.sleep(0.00005)  # 50 мкс
print()

pi.stop()

