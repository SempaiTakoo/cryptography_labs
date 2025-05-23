import random
import string

import nltk


def compare_texts(text1: str, text2: str) -> float:
    n = min(len(text1), len(text2))

    if n == 0:
        return 0.0

    matches = sum(
        1
        for char1, char2 in zip(text1, text2)
        if char1 == char2
    )
    return matches / max(len(text1), len(text2))


def generate_random_letters_text(total_chars: int) -> str:
    alphabet = string.ascii_letters + ' .'
    return ''.join(random.choices(alphabet, k=total_chars))


def generate_random_words_text(word_list: list[str], total_chars: int) -> str:
    words = []
    text_len = 0

    while text_len < total_chars:
        word = random.choice(word_list)

        if text_len + len(word) + (1 if words else 0) > total_chars:
            break

        words.append(word)
        text_len += len(word) + (1 if words else 0)

    return ' '.join(words)


def get_random_natural_lang_words_text(total_chars: int) -> str:
    nltk.download('words', quiet=True)
    words = nltk.corpus.words.words()
    return generate_random_words_text(word_list=words, total_chars=total_chars)


def get_text_from_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def get_avg(nums: list[float]) -> float:
    return sum(nums) / len(nums)


def main(text_filepath_1, text_filepath_2, iter_count: int):
    meaningful_text = get_text_from_file(text_filepath_1)
    another_meaningful_text = get_text_from_file(text_filepath_2)

    random_letters_text = generate_random_letters_text(len(meaningful_text))
    random_words_text = get_random_natural_lang_words_text(len(meaningful_text))

    all_results = [[], [], [], [], []]

    for _ in range(iter_count):
        all_results[0].append(compare_texts(meaningful_text,
                                            another_meaningful_text))
        all_results[1].append(compare_texts(meaningful_text,
                                            random_letters_text))
        all_results[2].append(compare_texts(meaningful_text,
                                            random_words_text))
        all_results[3].append(compare_texts(
            generate_random_letters_text(total_chars=1000),
            generate_random_letters_text(total_chars=1000)
        ))
        all_results[4].append(compare_texts(
            get_random_natural_lang_words_text(total_chars=1000),
            get_random_natural_lang_words_text(total_chars=1000)
        ))

    print(f'''
        Сравнение:
        1) два осмысленных текста на естественном языке: {get_avg(all_results[0])},
        2) осмысленный текст и текст из случайных букв: {get_avg(all_results[1])},
        3) осмысленный текст и текст из случайных слов: {get_avg(all_results[2])},
        4) два текста из случайных букв: {get_avg(all_results[3])},
        5) два текста из случайных слов: {get_avg(all_results[4])}.
        ''')


if __name__ == "__main__":
    TEXT_FILEPATH_1 = 'texts/yagpt_text_1.txt'
    TEXT_FILEPATH_2 = 'texts/yagpt_text_2.txt'
    main(TEXT_FILEPATH_1, TEXT_FILEPATH_2, iter_count=1000)
