# Функция для кодирования исходного сообщения
def encode_message(blocks: list, key: list, save_register: bool = True) -> str:
    encoded_message = ""

    for block in blocks:
        for key_item in key:
            encoded_message += block[key_item - 1]

    if not save_register:
        encoded_message = encoded_message.upper()
        
    return encoded_message

# Функция для расшифровки исходного сообщеня
def decode_message(blocks: list, key: list) -> str:
    decoded_message = ""

    for block in blocks:
        for index in range(len(key)):
            decoded_message += block[index]

    # Убираем лишние пробелы, которые могли быть добавлены при формировании блоков
    return decoded_message.strip()


def run():
    # Например: Полотенце попало в болото
    message = input("Введите сообщение: ")
    # Например: 4
    rank = int(input("Введите степень: "))
    if message or len(message) > rank:
        # Формируем блоки подстрок длиной rank
        blocks = [message[i:i+rank].ljust(rank) for i in range(0, len(message), rank)]
        # Формируем ключ для шифрование (и расшифрования сообщения)
        key = list(map(int, input('Введите список индексов через пробел (например, 1 4 2 3): ').split(' ')))
        # set (множество) - это набор уникальных, неупорядоченных элементов.
        if len(set(key)) == rank:
            encoded_message = encode_message(blocks, key)
            print(f"Зашифрованное сообщение: {encoded_message}")
            decoded_message = decode_message(blocks, key)
            print(f"Расшифрованное сообщение (с помощью ключа): {decoded_message}")
            if decoded_message == message:
                print(f"Алгоритм шифрования отработал корректно!")
            else:
                print(f"Алгоритм шифрования отработал некорректно! Исходное сообщение не совпадает с расшифрованным.")
        else:
            print(f"Все элементы списка должны быть уникальные, а само количество элементов должно совпадать со сзачением степени!")
    else:
        print(f"Длина сообщения ({message}) меньше степени ({rank}) или сообщнение пустое!")


if __name__ == "__main__":
    run()
