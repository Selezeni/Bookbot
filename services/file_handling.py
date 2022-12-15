BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    marks: list[str] = [",", ".", "!", ":", ";", "?"]
    end: int = start + size
    if end >= len(text):
        end = len(text)
    if (start + size) <= len(text):
        while (text[end] in marks) and ((text[end - 1] in marks) or (text[end + 1] in marks))\
                or (text[end] not in marks) or (len(text[start:end + 1]) > size):
            end -= 1
    return text[start:end + 1], len(text[start:end + 1])


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
