from rich.prompt import Prompt

from labs.lab_6.utils.utils import (
    binary_sum,
    get_constrains,
    right_rotate,
    right_shift
)
from labs.lab_6.utils.logic_operators import (
    logic_xor,
    logic_and,
    logic_not
)


# Функция для предварительной обработки исходного сообщения
def preprocess_message(message: str) -> str:
    # Преобразование исходного сообщения в двоичный формат
    message_bits = ''.join([format(char, '08b') for char in bytearray(message, 'utf-8')])
    # Сохранение длины (количества бит) исходного сообщения в двоичном формате
    message_bits_len = format(len(message_bits), '064b')
    # Добавление `1`
    message_bits += '1'
    # Добавление `0`, чтобы длина сообщения была кратна 512 - 64
    while (len(message_bits) + 64) % 512 != 0:
        message_bits += '0'
    # Добавление оставшихся 64 бит, представленных в виде двоичного кода длины исходного сообщения
    message_bits += message_bits_len

    return message_bits


# Функция для создания очереди сообщений (w)
def get_message_chunk_queue(preprocessed_message_chunk: str) -> list[str]:
    # Копирование входных данных из шага 1 в новый массив, где каждая запись является 32-битным словом:
    w = [preprocessed_message_chunk[index:index + 32] for index in range(0, len(preprocessed_message_chunk), 32)]
    # Добавление ещё 48 слов, инициализированных нулями, чтобы получить массив w[0…63]:
    w += ['0' * 32 for _ in range(48)]
    # Изменение нулевых индексов в конце массива
    for index in range(16, 64):
        s0 = logic_xor(right_rotate(w[index - 15], 7), right_rotate(w[index - 15], 18), right_shift(w[index - 15], 3))
        s1 = logic_xor(right_rotate(w[index - 2], 17), right_rotate(w[index - 2], 19), right_shift(w[index - 2], 10))

        w[index] = binary_sum(w[index - 16], s0, w[index - 7], s1)

    return w


def get_compressed_constrains(hash_constrains: list[str], round_constrains: list[str], message_chunk_queue: str) -> list[str]:
    a, b, c, d, e, f, g, h = hash_constrains

    for i in range(64):
        s1 = logic_xor(right_rotate(e, 6), right_rotate(e, 11), right_rotate(e, 25))
        ch = logic_xor(logic_and(e, f), logic_and(logic_not(e), g))
        temp1 = binary_sum(h, s1, ch, round_constrains[i], message_chunk_queue[i])
        s0 = logic_xor(right_rotate(a, 2), right_rotate(a, 13), right_rotate(a, 22))
        maj = logic_xor(logic_and(a, b), logic_and(a, c), logic_and(b, c))
        temp2 = binary_sum(s0, maj)

        h = g[-32:].rjust(32, '0')
        g = f[-32:].rjust(32, '0')
        f = e[-32:].rjust(32, '0')
        e = binary_sum(d, temp1)
        d = c[-32:].rjust(32, '0')
        c = b[-32:].rjust(32, '0')
        b = a[-32:].rjust(32, '0')
        a = binary_sum(temp1, temp2)

    return [
        a.rjust(32, '0')[-32:], b.rjust(32, '0')[-32:], c.rjust(32, '0')[-32:], d.rjust(32, '0')[-32:],
        e.rjust(32, '0')[-32:], f.rjust(32, '0')[-32:], g.rjust(32, '0')[-32:], h.rjust(32, '0')[-32:]
    ]


def generate_sha256_value(message: str = None) -> str:
    if not message:
        message = Prompt.ask(
            prompt="[bold blue]Введите сообщение для шифрования[/]",
            default="hello world"
        )

    # Шаг 1. Предварительная обработка сообщения
    preprocessed_message = preprocess_message(message)

    # Шаг 2. Инициализация значения хэша (h)
    hash_constrains = get_constrains(
        start_value=2,
        end_value=20,
        constrains_type='h'
    )

    # Шаг 3. Инициализация округлённых констант (k)
    rounded_constants = get_constrains(
        start_value=2,
        end_value=312,
        constrains_type='k'
    )

    # Шаг 4. Основной цикл
    for bit in range(0, len(preprocessed_message), 512):
        # Генерация `куска` подготовленного сообщения длиной 512 бит
        preprocessed_message_chunk = preprocessed_message[bit: bit + 512]

        # Шаг 5. Создание очереди сообщений (w)
        message_chunk_queue = get_message_chunk_queue(preprocessed_message_chunk)

        # Шаг 6. Цикл сжатия
        compressed_constrains = get_compressed_constrains(
            hash_constrains=hash_constrains,
            round_constrains=rounded_constants,
            message_chunk_queue=message_chunk_queue
        )

        # Шаг 7. Изменение окончательных значений

        hash_constrains = [
            binary_sum(hash_constrains[index], compressed_constrains[index])
            for index in range(len(hash_constrains))
        ]

    # Шаг 8. Получение финального хеша
    sha256_hash = ''.join(
        [
            format(int(hash_constraint, 2), '08x')
            for hash_constraint in hash_constrains
        ]
    ).upper()

    return sha256_hash


if __name__ == '__main__':
    generate_sha256_value()
