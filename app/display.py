from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayBook(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayBook(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content[::-1])