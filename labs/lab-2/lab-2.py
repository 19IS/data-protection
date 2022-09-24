import pandas as pd
from rich import print
from rich.prompt import Prompt

# Функция для кодирования исходного сообщения
def encode_message(message: list, shift: int, alphabet: list) -> str:
    message = list(message)
    for index, char in enumerate(message):
        if char in alphabet:
            message[index] = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
    return ''.join(message)

# Функция для расшифровки исходного сообщеня
def decode_message(message: list, shift: int, alphabet: list) -> str:
    message = list(message)
    for index, char in enumerate(message):
        if char in alphabet:
            message[index] = alphabet[(alphabet.index(char) - shift) % len(alphabet)] 
    return ''.join(message)


def run():
    russian_alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    message = Prompt.ask("[bold blue]Введите сообщение[/]").lower()
    mode = Prompt.ask("[bold blue]Выберите действие для сообщения[/]", choices=["зашифровать", "расшифровать"])
    
    if mode == "зашифровать":
        shift = int(Prompt.ask("[bold blue]Введите значение сдвига[/]"))
        
        if shift == 0:
            print(f"[bold yellow]Значение сдвига равно 0. Закодированное сообщение будет идентично исходному![/]")
        elif shift > len(russian_alphabet):
            print(f"[bold yellow]Значение сдвига больше {len(russian_alphabet)}. Значение сдвига автоматически будет равно: {shift % len(russian_alphabet)}![/]")
            
        encoded_message = encode_message(
            message=message,
            shift=shift,
            alphabet=russian_alphabet
        )
        print(f"Зашифрованное сообщение: {encoded_message}")
        decoded_message = decode_message(
            message=encoded_message,
            shift=shift,
            alphabet=russian_alphabet
        )
        print(f"Дешифрованное сообщение: {decoded_message}")
        if decoded_message == message:
            print(f"[bold green]Алгоритм шифрования отработал корректно![/]")
        else:
            print(f"[bold red]Алгоритм шифрования отработал некорректно! Исходное сообщение не совпадает с расшифрованным.[/]")
            
    elif mode == "расшифровать":
        print(f"[bold blue]Варианты расшифровок сообщения:[/]")
        # щъзшмсарс р цлрх рп цщхцйхгэ щчцщцицй пзбръг рхьцшфзюрр еъц щруцйгм фмъцлг, ъц мщъд цэшзхз лцтыфмхъз (8-я итерация будет верной)
        for iteration in range(len(russian_alphabet)):
            decoded_variant = decode_message(message=message, shift=iteration, alphabet=russian_alphabet)
            print(f"{iteration}: {decoded_variant}")
                
                
if __name__ == "__main__":
    run()

