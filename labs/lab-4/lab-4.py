from rich import print
from rich.prompt import Prompt


RUSSIAN_ALPHABET = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

def generate_alt_alphabet(slogan: str) -> list:
    alt_alphabet = list(dict.fromkeys(slogan)) + [char for char in RUSSIAN_ALPHABET if char not in slogan]
    return alt_alphabet

# Функция для кодирования исходного сообщения
def encode_message(message: str, slogan: str) -> str:
    encoded_message = ''
    alt_alphabet = generate_alt_alphabet(slogan=slogan)
    
    for index in range(len(message)):
        if message[index] in alt_alphabet:
            encoded_message += alt_alphabet[RUSSIAN_ALPHABET.index(message[index])]
        else:
            encoded_message += message[index]
        
    return encoded_message

# Функция для расшифровки исходного сообщеня
def decode_message(message: str, slogan: str) -> str:
    decoded_message = ''
    alt_alphabet = generate_alt_alphabet(slogan=slogan)  
    
    for index in range(len(message)):
        if message[index] in RUSSIAN_ALPHABET:
            decoded_message += RUSSIAN_ALPHABET[alt_alphabet.index(message[index])]
        else:
            decoded_message += message[index]
        
    return decoded_message


def run():
    message = Prompt.ask("[bold blue]Введите сообщение[/]", default='Андрей Николаевич').lower()
    slogan = Prompt.ask("[bold blue]Введите лозунг[/]", default='Чуйко').lower()
    
    encoded_message = encode_message(
        message=message,
        slogan=slogan
    )
    print(f"Зашифрованное сообщение: {encoded_message}")
    
    decoded_message = decode_message(
        message=encoded_message,
        slogan=slogan
    )
    print(f"Дешифрованное сообщение: {decoded_message}")
    
    if decoded_message == message:
        print(f"[bold green]Алгоритм шифрования отработал корректно![/]")
    else:
        print(f"[bold red]Алгоритм шифрования отработал некорректно! Исходное сообщение не совпадает с расшифрованным.[/]")
                
if __name__ == "__main__":
    run()

