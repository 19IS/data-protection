from hashlib import sha256
from rich import print
from labs.lab_6.lab_6 import generate_sha256_value


def run_tests():
    test_messages = [
        'SHA-2 (Secure Hash Algo!@#!@#r#ithm 2,+=) is a&*_^&*%%E$^@#$!@#!@$@#@%@#$!@#!@#!@%()+_)(*&^%$#@!~ set of cryptographic hash functions designed by the United States National Security Agency (NSA)',
        '!@#%^*+_)(*_()&*I^U%Y$#@&^%$#@!~',
        '!@#%^*+_)(*_()&asjkdjfklasdfjdfjkkwerkfjqwopdfjeruicmasdfjklasdfgjkl;*   as;jasjqwepweionasdfgnasdfjklasdfnzxcvjkl; hjkasdJKLFJQWJIOER89123348IO1NHV I^U%Y$#@&^%$#@!~',
        'приветFylhtАндрейцукйцукйцукйц1234123412341?(???(?%:()_)_^&*)_',
        'test'
    ]
    for iteration, test_message in enumerate(test_messages):
        try:
            my_sha256_hash = generate_sha256_value(test_message)
            lib_sha256_hash = sha256(test_message.encode('utf-8')).hexdigest().upper()
            print(f"Результат работы собственной функции: {my_sha256_hash}")
            print(f"Результат работы функции из сторонней библиотеки: {lib_sha256_hash}")
            assert my_sha256_hash == lib_sha256_hash
            print(f"[bold green]Test {iteration + 1}: passed[/]")
        except AssertionError:
            print(f"[bold red]Test {iteration + 1}: failed[/]")


if __name__ == '__main__':
    run_tests()
