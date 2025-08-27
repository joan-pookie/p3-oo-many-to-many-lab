# test_many_to_many.py
import pytest
from many_to_many import Author, Book, Contract

def setup_function():
    # Clear all class variables before each test
    Author.all.clear()
    Book.all.clear()
    Contract.all.clear()

def test_author_book_contract_creation():
    author = Author("J.K. Rowling")
    book = Book("Harry Potter and the Sorcerer's Stone")
    contract = Contract(author, book, "1997-06-26", 15)

    assert author in Author.all
    assert book in Book.all
    assert contract in Contract.all
    assert contract.author == author
    assert contract.book == book
    assert contract.date == "1997-06-26"
    assert contract.royalties == 15

def test_author_sign_contract_and_books():
    author = Author("George R.R. Martin")
    book1 = Book("A Game of Thrones")
    book2 = Book("A Clash of Kings")

    # Sign contracts
    c1 = author.sign_contract(book1, "1996-08-06", 12)
    c2 = author.sign_contract(book2, "1998-11-16", 10)

    assert c1 in Contract.all
    assert c2 in Contract.all
    assert book1 in author.books()
    assert book2 in author.books()
    assert len(author.contracts()) == 2

def test_total_royalties():
    author = Author("J.R.R. Tolkien")
    book1 = Book("The Hobbit")
    book2 = Book("The Lord of the Rings")

    author.sign_contract(book1, "1937-09-21", 20)
    author.sign_contract(book2, "1954-07-29", 25)

    assert author.total_royalties() == 45

def test_contracts_by_date():
    author1 = Author("Author One")
    author2 = Author("Author Two")
    book1 = Book("Book One")
    book2 = Book("Book Two")

    Contract(author1, book1, "2025-08-27", 10)
    Contract(author2, book2, "2025-08-27", 15)
    Contract(author1, book2, "2025-08-28", 12)

    contracts_on_27th = Contract.contracts_by_date("2025-08-27")
    assert len(contracts_on_27th) == 2
    assert all(contract.date == "2025-08-27" for contract in contracts_on_27th)

def test_type_validation_exceptions():
    author = Author("Test Author")
    book = Book("Test Book")

    with pytest.raises(Exception):
        author.sign_contract("NotABook", "2025-08-27", 10)

    with pytest.raises(Exception):
        author.sign_contract(book, 20250827, 10)

    with pytest.raises(Exception):
        author.sign_contract(book, "2025-08-27", "10")
