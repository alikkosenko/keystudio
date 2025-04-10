#include <stdio.h>
#include <pigpio.h>
#include <unistd.h>

#define DHT_PIN 4

int dht11_read(int *temperature, int *humidity) {
    uint8_t last_state = PI_HIGH;
    uint8_t counter = 0;
    uint8_t j = 0, i;

    uint8_t data[5] = {0};

    // Подать стартовый сигнал
    gpioSetMode(DHT_PIN, PI_OUTPUT);
    gpioWrite(DHT_PIN, PI_LOW);
    gpioDelay(20000);  // 20 мс

    gpioWrite(DHT_PIN, PI_HIGH);
    gpioDelay(30);     // 20-40 мкс

    gpioSetMode(DHT_PIN, PI_INPUT);

    // Считывание сигнала
    for (i = 0; i < 85; i++) {
        counter = 0;
        while (gpioRead(DHT_PIN) == last_state) {
            counter++;
            gpioDelay(1);
            if (counter == 255) break;
        }
        last_state = gpioRead(DHT_PIN);

        if (counter == 255) break;

        // Первые 3 перехода игнорируются
        if ((i >= 4) && (i % 2 == 0)) {
            data[j / 8] <<= 1;
            if (counter > 16)  // если долго — значит "1"
                data[j / 8] |= 1;
            j++;
        }
    }

    // Проверка контрольной суммы
    if ((j >= 40) &&
        (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF))) {
        *humidity = data[0];
        *temperature = data[2];
        return 0;  // успех
    } else {
        return 1;  // ошибка
    }
}

int main() {
    if (gpioInitialise() < 0) {
        printf("pigpio init failed\n");
        return 1;
    }

    int temp = 0, hum = 0;

    for (int i = 0; i < 5; i++) {
        if (dht11_read(&temp, &hum) == 0) {
            printf("Temperature: %d °C, Humidity: %d %%\n", temp, hum);
            break;
        } else {
            printf("Failed to read. Retrying...\n");
            sleep(2);
        }
    }

    gpioTerminate();
    return 0;
}

