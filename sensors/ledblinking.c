#include <stdio.h>
#include <pigpio.h>
#include <unistd.h> // для sleep()

int main() {

    int status = gpioInitialise();
    printf("%d", status);

    if (status < 0) {
        printf("Ошибка инициализации pigpio\n");
        return 1;
    }

    int pin = 18; // GPIO18

    gpioSetMode(pin, PI_OUTPUT); // Устанавливаем пин как выход

    for (int i = 0; i < 109; i++) {
        gpioWrite(pin, 1); // Включить светодиод
        sleep(1);
        gpioWrite(pin, 0); // Выключить
        sleep(1);
    }

    gpioTerminate(); // Завершение работы pigpio
    return 0;
}

