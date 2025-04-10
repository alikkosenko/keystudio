import smbus
import time

# Адрес устройства PCF8591 по умолчанию
PCF8591_ADDRESS = 0x48

# Открытие I2C-шины
bus = smbus.SMBus(1)

# Функция для чтения данных с канала A0
def read_adc(channel):
    if channel < 0 or channel > 3:
        print("Неверный канал, выбирай от 0 до 3")
        return -1

    # Запрос на чтение с PCF8591
    bus.write_byte(PCF8591_ADDRESS, 0x40 | channel)  # Адрес с флагом чтения
    time.sleep(0.1)  # Задержка для стабильности

    # Чтение данных с канала
    data = bus.read_byte(PCF8591_ADDRESS)
    return data

# Главный цикл
while True:
    adc_value = read_adc(0)  # Чтение с канала A0
    print(f"Значение с A0: {adc_value}")
    time.sleep(1)  # Пауза между измерениями

