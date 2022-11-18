import math
import sympy


# Функция для нахождения суммы n последовательностей бит
def binary_sum(*args) -> str:
    return format(sum([int(val, 2) for val in args]), '032b')[-32:]


# Функция перестановки последних n битов бинарного значения слова в начало
def right_rotate(binary_word: str, rotation_value: int) -> str:
    return binary_word[len(binary_word) - rotation_value:] + binary_word[:len(binary_word) - rotation_value]


# Функция смещения бинарного значения слова на n позиций
def right_shift(binary_word: str, shift_value: int) -> str:
    return '0' * shift_value + binary_word[:len(binary_word) - shift_value]


# Функция для генерации констант
# h - генерация значений хеша
# k - генерация округленных констант
def get_constrains(start_value: int, end_value: int, constrains_type: str = 'h') -> dict:
    # Генерация простых чисел из заданного диапазона
    prime_numbers = list(sympy.primerange(start_value, end_value))
    # Определение степени корня
    root = 2 if constrains_type == 'h' else 3
    # Вычисление корня простых чисел
    prime_numbers = [math.pow(prime_number, 1 / root) for prime_number in prime_numbers]
    # Вычисление произведения дробной части от квадратного корня простых чисел и 2^32
    prime_numbers = [math.modf(prime_number)[0] * 2 ** 32 for prime_number in prime_numbers]
    # Вычисление целой части от полученного произведения
    prime_numbers = [int(math.modf(prime_number)[1]) for prime_number in prime_numbers]
    # Приведение полученного списка двоичных чисел в шестнадцатеричный формат
    prime_numbers = [
        format(prime_number, '032b')
        for prime_number in prime_numbers
    ]

    return prime_numbers
