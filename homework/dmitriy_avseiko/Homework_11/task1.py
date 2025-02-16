class Book:
    page_material = 'paper'
    presence_of_text = True

    def __init__(self, book_title, author, number_of_pages, ISBN, book_reserved):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.book_reserved = book_reserved


book1 = Book('Герой нашего времени', 'Лермонтов', 224, '9785170921645',
             False)
book2 = Book('Преступление и наказание', 'Достоевский', 608, '9785389049260',
             False)
book3 = Book('Лолита', 'Набоков', 544, '9785171373870', False)
book4 = Book('Братья Карамазовы', 'Достоевский', 832, '9785389066571',
             False)
book5 = Book('Яма', 'Куприн', 416, '9785170904808', False)

book3.book_reserved = True
book_list = [book1, book2, book3, book4, book5]

for i in book_list:
    if i.book_reserved:
        print(f'Название: {i.book_title}, Автор: {i.author}, страниц: {i.number_of_pages}, материал: {i.page_material},'
              f' зарезервирована')
    else:
        print(f'Название: {i.book_title}, Автор: {i.author}, страниц: {i.number_of_pages}, материал: {i.page_material}')


class Schoolbook(Book):

    def __init__(self, book_title, author, number_of_pages, ISBN, book_reserved, subject, level, tasks_availability):
        super().__init__(book_title, author, number_of_pages, ISBN, book_reserved)
        self.subject = subject
        self.level = level
        self.tasks_availability = tasks_availability


schoolbook1 = Schoolbook('Алгебра', 'Иванов', 123, '9785170921123',
                         False, 'Математика', 6, True)
schoolbook2 = Schoolbook('Геометрия', 'Петров', 456, '9785389049456',
                         False, 'Математика', 7, True)
schoolbook3 = Schoolbook('Органическая биология', 'Сидоров', 789, '9785171373789',
                         False, 'Биология', 8, False)

schoolbook2.book_reserved = True
schoolbook_list = [schoolbook1, schoolbook2, schoolbook3]

for i in schoolbook_list:
    if i.book_reserved:
        print(f'Название: {i.book_title}, Автор: {i.author}, страниц: {i.number_of_pages}, предмет: {i.subject}, '
              f'класс: {i.level}, зарезервирована')
    else:
        print(f'Название: {i.book_title}, Автор: {i.author}, страниц: {i.number_of_pages}, предмет: {i.subject}, '
              f'класс: {i.level}')
