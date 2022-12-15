BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text (text: str, start: int, page_size: int) -> tuple[str, int]:
    sign = ",.!:;?"
    page = text[start:start + page_size]
    # if page[-2] in sign:
    #     page = page[:-2]
    while page[-1] not in sign:
        page = page[:-1]
    return page, len(page)


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
