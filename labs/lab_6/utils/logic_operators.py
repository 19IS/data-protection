# Функция для вычисления XOR двух последовательностей бит
def logic_xor(val_1: str, val_2: str) -> str:
    max_bit_sequence_value = max(len(val_1), len(val_2))
    val_1 = val_1.rjust(max_bit_sequence_value, '0')
    val_2 = val_2.rjust(max_bit_sequence_value, '0')

    result = ''.join(
        [
            str(int(bool(int(val_1[bit])) != bool(int(val_2[bit]))))
            for bit in range(max_bit_sequence_value)
        ]
    )

    return result


# Функция для вычисления AND двух последовательностей бит
def logic_and(val_1: str, val_2: str) -> str:
    max_bit_sequence_value = max(len(val_1), len(val_2))
    val_1 = val_1.rjust(max_bit_sequence_value, '0')
    val_2 = val_2.rjust(max_bit_sequence_value, '0')

    result = ''.join(
        [
            str(int(bool(int(val_1[bit])) and bool(int(val_2[bit]))))
            for bit in range(max_bit_sequence_value)
        ]
    )

    return result


# Функция для вычисления NOT последовательности бит
def logic_not(val: str) -> str:
    result = ''.join([str(int(not bool(int(bit)))) for bit in val])

    return result
