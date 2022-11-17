from rich import print
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

k = ['1000010100010100010111110011000', '1110001001101110100010010010001', '10110101110000001111101111001111',
     '11101001101101011101101110100101', '111001010101101100001001011011', '1011001111100010001000111110001',
     '10010010001111111000001010100100', '10101011000111000101111011010101', '11011000000001111010101010011000',
     '10010100000110101101100000001', '100100001100011000010110111110', '1010101000011000111110111000011',
     '1110010101111100101110101110100', '10000000110111101011000111111110', '10011011110111000000011010100111',
     '11000001100110111111000101110100', '11100100100110110110100111000001', '11101111101111100100011110000110',
     '1111110000011001110111000110', '100100000011001010000111001100', '101101111010010010110001101111',
     '1001010011101001000010010101010', '1011100101100001010100111011100', '1110110111110011000100011011010',
     '10011000001111100101000101010010', '10101000001100011100011001101101', '10110000000000110010011111001000',
     '10111111010110010111111111000111', '11000110111000000000101111110011', '11010101101001111001000101000111',
     '110110010100110001101010001', '10100001010010010100101100111', '100111101101110000101010000101',
     '101110000110110010000100111000', '1001101001011000110110111111100', '1010011001110000000110100010011',
     '1100101000010100111001101010100', '1110110011010100000101010111011', '10000001110000101100100100101110',
     '10010010011100100010110010000101', '10100010101111111110100010100001', '10101000000110100110011001001011',
     '11000010010010111000101101110000', '11000111011011000101000110100011', '11010001100100101110100000011001',
     '11010110100110010000011000100100', '11110100000011100011010110000101', '10000011010101010000001110000',
     '11001101001001100000100010110', '11110001101110110110000001000', '100111010010000111011101001100',
     '110100101100001011110010110101', '111001000111000000110010110011', '1001110110110001010101001001010',
     '1011011100111001100101001001111', '1101000001011100110111111110011', '1110100100011111000001011101110',
     '1111000101001010110001101101111', '10000100110010000111100000010100', '10001100110001110000001000001000',
     '10010000101111101111111111111010', '10100100010100000110110011101011', '10111110111110011010001111110111',
     '11000110011100010111100011110010']


# Функция для предварительной обработки исходного сообщения
def preprocess_message(message: str) -> str:
    # Преобразование исходного сообщения в двоичный формат
    message_bits = ''.join([format(ord(char), '08b') for char in message])
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
def get_message_chunk_queue(preprocessed_message_chunk: str):
    # Копирование входных данных из шага 1 в новый массив, где каждая запись является 32-битным словом:
    w = [preprocessed_message_chunk[index:index + 32] for index in range(0, len(preprocessed_message_chunk), 32)]
    # Добавление ещё 48 слов, инициализированных нулями, чтобы получить массив w[0…63]:
    w += ['0' * 32 for _ in range(48)]
    # Изменение нулевых индексов в конце массива
    for index in range(16, 64):
        s0 = logic_xor(logic_xor(right_rotate(w[index - 15], 7), right_rotate(w[index - 15], 18)),
                       right_shift(w[index - 15], 3))
        s1 = logic_xor(logic_xor(right_rotate(w[index - 2], 17), right_rotate(w[index - 2], 19)),
                       right_shift(w[index - 2], 10))

        w[index] = binary_sum(w[index - 16], s0, w[index - 7], s1)

    return w


def get_compressed_constrains(hash_constrains, round_constrains, message_chunk_queue):
    a, b, c, d, e, f, g, h = hash_constrains

    for i in range(64):
        s1 = logic_xor(logic_xor(right_rotate(e, 6), right_rotate(e, 11)), right_rotate(e, 25))
        ch = logic_xor(logic_and(e, f), logic_and(logic_not(e), g))
        temp1 = binary_sum(h, s1, ch, round_constrains[i], message_chunk_queue[i])
        s0 = logic_xor(logic_xor(right_rotate(a, 2), right_rotate(a, 13)), right_rotate(a, 22))
        maj = logic_xor(logic_xor(logic_and(a, b), logic_and(a, c)), logic_and(b, c))
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


def generate_sha256_value(message: str = None):
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
    sha256_hash = ''.join([format(int(hash_constraint, 2), '08x') for hash_constraint in hash_constrains]).upper()
    # print(sha256_hash)
    return sha256_hash


if __name__ == '__main__':
    generate_sha256_value()
