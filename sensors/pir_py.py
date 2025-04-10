import pigpio
import time

# Укажи номер GPIO-пина (в BCM нотации)
PIR_GPIO = 4  # Например, BCM 17 = физический пин 11

# Запуск pigpio daemon, если ещё не запущен:
# sudo pigpiod

# Подключение к pigpio
pi = pigpio.pi()
if not pi.connected:
    print("Не удалось подключиться к pigpio. Убедись, что pigpiod запущен.")
    exit()

# Установка пина как вход
pi.set_mode(PIR_GPIO, pigpio.INPUT)

# Функция, которая вызывается при изменении состояния сигнала
def motion_callback(gpio, level, tick):
    if level == 1:
        print("👀 Обнаружено движение!")
    elif level == 0:
        print("❌ Движение прекратилось.")
    else:
        print("⚠️ Неизвестный уровень:", level)

# Регистрируем callback
cb = pi.callback(PIR_GPIO, pigpio.EITHER_EDGE, motion_callback)

print("Ожидаю движение... Нажми Ctrl+C для выхода.")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nОстанавливаем...")

finally:
    cb.cancel()
    pi.stop()

