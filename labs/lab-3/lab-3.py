from rich import print
from rich.prompt import Prompt


# Неправильный алфавит (из лабораторной работы)
# RUSSIAN_ALPHABET = list('абвгдежзийклмнопрстуфхцчшщыьэюя ')

# Правильный алфавит (человеческий)
RUSSIAN_ALPHABET = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя ')

# Функция для кодирования исходного сообщения
def encode_message(message: str, key: str) -> str:
    encoded_message = ''
    
    for index in range(len(message)):
        message_symbol_index = RUSSIAN_ALPHABET.index(message[index])
        key_symbol_index = RUSSIAN_ALPHABET.index(key[index % len(key)])
        encoded_message += RUSSIAN_ALPHABET[(message_symbol_index + key_symbol_index) % len(RUSSIAN_ALPHABET)]
        
    return encoded_message

# Функция для расшифровки исходного сообщеня
def decode_message(message: str, key: str) -> str:
    decoded_message = ''
    
    for index in range(len(message)):
        message_symbol_index = RUSSIAN_ALPHABET.index(message[index])
        key_symbol_index = RUSSIAN_ALPHABET.index(key[index % len(key)])
        decoded_message += RUSSIAN_ALPHABET[(message_symbol_index - key_symbol_index) % len(RUSSIAN_ALPHABET)]
        
    return decoded_message


def run():
    message = Prompt.ask("[bold blue]Введите сообщение[/]", default='Информация становится знанием когда она переработана и проанализирована человеком').lower()
    key = Prompt.ask("[bold blue]Введите ключ[/]", default='требования').lower()
    
    encoded_message = encode_message(
        message=message,
        key=key
    )
    print(f"Зашифрованное сообщение: {encoded_message}")
    
    decoded_message = decode_message(
        message=encoded_message,
        key=key
    )
    print(f"Дешифрованное сообщение: {decoded_message}")
                
if __name__ == "__main__":
    run()

