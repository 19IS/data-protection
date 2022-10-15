import math

import sympy
from rich import print
from rich.prompt import Prompt


# Функция для шифрования сообщения
def encode_message(message: list, public_key: dict) -> list:
    encoded_message = [
        pow(ord(item), public_key['public_exp'], public_key['module'])
        for item in message
    ]
    return encoded_message


# Функция для расшифрования сообщения
def decode_message(encoded_message: list, private_key: dict) -> list:
    decoded_message = [
        chr(pow(item, private_key['private_exp'], private_key['module']))
        for item in encoded_message
    ]
    return decoded_message


# Функция для генерации списка случайных и неповторяющихся простых чисел
def generate_random_prime_numbers(numbers_count: int = 2) -> list:
    random_prime_numbers = []
    while len(random_prime_numbers) < numbers_count:
        random_prime_nuber = sympy.randprime(1000, 100000)
        if random_prime_nuber not in random_prime_numbers:
            random_prime_numbers.append(random_prime_nuber)
    if len(random_prime_numbers) == 1:
        return random_prime_numbers[0]
    else:
        return random_prime_numbers


# Функция генерации публичного и секретного ключей
def generate_key_pair(p: int, q: int) -> tuple:
    # Вычисляем модуль двух различных простых чисел
    n = p * q
    # Вычисляем функцию Эйлера
    euler_function = (p - 1) * (q - 1)
    # Вычисляем открытую экспоненту
    e = None
    while True:
        random_prime_number = generate_random_prime_numbers(1)
        if math.gcd(random_prime_number, euler_function):
            e = random_prime_number
            break
    # Вычисляем секретную экспоненту
    d = None
    for i in range(1, e):
        raw_d = ((euler_function * i) + 1) / e
        if raw_d.is_integer():
            d = int(raw_d)
            break
    # Генерируем публичный ключ
    public_key = {
        "public_exp": e,
        "module": n
    }
    # Генерируем секретный ключ
    private_key = {
        "private_exp": d,
        "module": n
    }

    return public_key, private_key


def run():
    message = Prompt.ask(
        prompt="[bold blue]Введите сообщение для шифрования[/]",
        default="Привет Андрей!"
    )

    p, q = generate_random_prime_numbers()

    print(f"Первое случайное простое число (p): {p}")
    print(f"Второе случайное простое число (q): {q}")

    public_key, private_key = generate_key_pair(p, q)
    print(f"Публичный ключ: {public_key}")
    print(f"Секретный ключ: {private_key}")

    encoded_message = encode_message(message, public_key)
    print(f"Зашифрованное сообщение: {''.join([str(item) for item in encoded_message])}")

    decoded_message = decode_message(encoded_message, private_key)
    print(f"Расшифрованное сообщение: {''.join([str(item) for item in decoded_message])}")


if __name__ == "__main__":
    run()
