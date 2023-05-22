from typing import Optional


def process_stream(stream):
    for number in stream:
        num = parse_number(number)
        if num is not None:
            print(num)
        else:
            print("ERROR")
            break


def parse_number(number) -> Optional[int]:
    try:
        return int(number)
    except ValueError:
        return None


# Ejemplo de uso
stream = ['1', '2', '3', 'a', '4', '5']
process_stream(stream)
