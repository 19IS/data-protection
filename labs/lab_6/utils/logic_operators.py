# Функция для вычисления XOR n последовательностей бит
def logic_xor(*args) -> str:
    def __xor(val_1: str, val_2: str) -> str:
        return ''.join(
            [
                str(int(bool(int(val_1[bit])) != bool(int(val_2[bit]))))
                for bit in range(max_bit_sequence_value)]
        )

    max_bit_sequence_value = max(*[len(val) for val in args])
    prev_result = __xor(args[0], args[1])
    for i in range(2, len(args)):
        prev_result = __xor(prev_result, args[i])

    return prev_result


# Функция для вычисления AND n последовательностей бит
def logic_and(*args) -> str:
    def __and(val_1: str, val_2: str) -> str:
        return ''.join(
            [
                str(int(bool(int(val_1[bit])) and bool(int(val_2[bit]))))
                for bit in range(max_bit_sequence_value)]
        )

    max_bit_sequence_value = max(*[len(val) for val in args])
    prev_result = __and(args[0], args[1])
    for i in range(2, len(args)):
        prev_result = __and(prev_result, args[i])

    return prev_result


# Функция для вычисления NOT последовательности бит
def logic_not(val: str) -> str:
    result = ''.join(
        [
            str(int(not bool(int(bit))))
            for bit in val
        ]
    )

    return result
