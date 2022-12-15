BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation_marks = [',', '!', ':', ';', '?', '.']
    cropped_text = text[start:]
    formatted_text = cropped_text[:size]
    if (cropped_text[:size][-1] == '.' and cropped_text[:size+1][-1] == '.') and cropped_text[size+1:] != '':
        formatted_text = formatted_text[:-3]
    while formatted_text[-1] not in punctuation_marks:
            formatted_text = formatted_text[:-1]
    return formatted_text, len(formatted_text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as file:
        text = file.read()
    global PAGE_SIZE, book
    start = counter = 0
    while start < len(text):
        counter += 1
        prepared_page = _get_part_text(text, start, PAGE_SIZE)
        book[counter] = prepared_page[0].lstrip()
        start += prepared_page[1]


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
