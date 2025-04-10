from gostcrypto import gosthash
from sympy import factorint


def get_variant(fio: str) -> int:
    fio_bytes = fio.encode('utf-8')
    hash_obj = gosthash.new('streebog256')
    hash_obj.update(fio_bytes)
    hash_result = hash_obj.hexdigest()
    variant_number = int(hash_result[-2:], 16)
    return variant_number


def get_numbers(filepath: str) -> tuple[int, int]:
    with open(filepath, 'r', encoding='utf-8') as f:
        a, b = map(int, f.readlines())
    return a, b


def get_pair_factors(num: int) -> tuple[int, int]:
    return tuple(
        int(num)
        for num in factorint(num).keys()
    )


if __name__ == '__main__':
    variant = get_variant(
        "Караев Тариел Жоомартбекович"
    )
    a, b = get_numbers('input.txt')

    print(f'Мой вариант: {variant}')

    print(f'a[{variant}] = {a}')
    print(f'b[{variant}] = {b}')

    print(f'Цифр в числе a: {len(str(a))}')
    print(f'Цифр в числе b: {len(str(b))}')

    print(
        'Нетривиальные сомножители a: '
        f'{get_pair_factors(a)}'
    )
