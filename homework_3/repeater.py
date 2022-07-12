import time


def repeater(call_count, start_sleep_time, factor, border_sleep_time):
    def outher(foo):
        def wrapper():
            if call_count == 0:
                return print(f'Запусков не будет')
            else:
                t = start_sleep_time
                print(f'Кол-во запусков = {call_count}')
                print('Начало работы')
                for i in range(1, call_count+1):
                    t *= (2 ** factor)
                    t = t if t < border_sleep_time else border_sleep_time
                    print(f'Запуск номер {i}. Ожидание: {t} секунд.', end=' ')
                    time.sleep(t)
                    func_result = foo()
                    print(f'Результат декорируемой функций = {func_result}.')
                print('Конец работы')
        return wrapper
    return outher


@repeater(call_count=3, start_sleep_time=1, factor=2, border_sleep_time=100)
def foo():
    return 'Y_LAB'


if __name__ == '__main__':
    foo()