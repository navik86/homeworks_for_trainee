import time


def repeater(call_count, start_sleep_time, factor, border_sleep_time):
    def outher(foo):
        def wrapper():
            if call_count == 0:
                return print(f'Запусков не будет')
            else:
                print(f'Кол-во запусков = {call_count}')
                print('Начало работы')
                for i in range(call_count):
                    t = start_sleep_time * factor ** i
                    if t >= border_sleep_time:
                        t = border_sleep_time
                    print(f'Запуск номер {i+1}. Ожидание: {t} секунд.', end=' ')
                    time.sleep(t)
                    func_result = foo()
                    print(f'Результат декорируемой функций = {func_result}.')
                print('Конец работы')
        return wrapper
    return outher


@repeater(call_count=5, start_sleep_time=1, factor=2, border_sleep_time=100)
def foo():
    return 'Y_LAB'


if __name__ == '__main__':
    foo()