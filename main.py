import string

def sort_words(words):
    ukr_words = sorted(
        [word for word in words if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in word)],
        key=lambda word: word.lower()
    )
    eng_words = sorted(
        [word for word in words if any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in word)],
        key=lambda word: word.lower()
    )
    return ukr_words + eng_words


def process_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()

            first_sentence = text.split('.')[0]
            print("Перше речення:")
            print(first_sentence)
            text_cleaned = text.translate(str.maketrans('', '', string.punctuation))

            words = text_cleaned.split()

            sorted_words = sort_words(words)

            print("\nВідсортовані слова:")
            print(sorted_words)

            print("\nКількість слів:", len(words))

    except FileNotFoundError:
        print(f"Помилка: файл '{file_name}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


file_name = "Text"
process_file(file_name)