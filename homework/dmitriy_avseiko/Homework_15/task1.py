import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port='25060',
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO `students` (name, second_name) VALUES ('Testname', 'Testsecondname')")
student_id = cursor.lastrowid

insert_books_query = "INSERT INTO `books` (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_books_query, [
        ('Python_AA', student_id),
        ('python_BB', student_id),
        ('Python_CC', student_id)
    ]
)

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('group28022025', 'feb 2024', 'feb 2025')")
group_id = cursor.lastrowid
cursor.execute(f'UPDATE `students` SET group_id = {group_id} WHERE id = {student_id}')

insert_subject1_query = "INSERT INTO `subjets` (title) VALUES (%s)"
values = ('chemistry29',)
cursor.execute(insert_subject1_query, values)
subject1_id = cursor.lastrowid
insert_subject2_query = "INSERT INTO `subjets` (title) VALUES (%s)"
values = ('biology29',)
cursor.execute(insert_subject2_query, values)
subject2_id = cursor.lastrowid

insert_lesson1_query = "INSERT INTO `lessons` (title, subject_id) VALUES (%s, %s)"
values = ('lesson1', subject1_id)
cursor.execute(insert_lesson1_query, values)
lesson1_id = cursor.lastrowid
insert_lesson2_query = "INSERT INTO `lessons` (title, subject_id) VALUES (%s, %s)"
values = ('lesson2', subject1_id)
cursor.execute(insert_lesson2_query, values)
lesson2_id = cursor.lastrowid
insert_lesson3_query = "INSERT INTO `lessons` (title, subject_id) VALUES (%s, %s)"
values = ('lesson3', subject2_id)
cursor.execute(insert_lesson3_query, values)
lesson3_id = cursor.lastrowid
insert_lesson4_query = "INSERT INTO `lessons` (title, subject_id) VALUES (%s, %s)"
values = ('lesson4', subject2_id)
cursor.execute(insert_lesson4_query, values)
lesson4_id = cursor.lastrowid

insert_mark1_query = "INSERT INTO `marks` (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (0, lesson1_id, student_id)
cursor.execute(insert_mark1_query, values)
insert_mark2_query = "INSERT INTO `marks` (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (1, lesson2_id, student_id)
cursor.execute(insert_mark2_query, values)
insert_mark3_query = "INSERT INTO `marks` (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (2, lesson3_id, student_id)
cursor.execute(insert_mark3_query, values)
insert_mark4_query = "INSERT INTO `marks` (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = (3, lesson4_id, student_id)
cursor.execute(insert_mark4_query, values)

cursor.execute(f'SELECT * from marks where student_id = {student_id}')
print(cursor.fetchall())

cursor.execute(f'SELECT * from books where taken_by_student_id = {student_id}')
print(cursor.fetchall())

select_all_info = '''
SELECT groups.title, groups.start_date, groups.end_date, students.name, students.second_name, books.title, marks.value,
 lessons.title, subjets.title
FROM `students`
LEFT JOIN `groups`
ON students.group_id = groups.id
LEFT JOIN `books`
ON students.id = books.taken_by_student_id
LEFT JOIN `marks`
ON students.id = marks.student_id
LEFT JOIN `lessons`
ON marks.lesson_id = lessons.id
LEFT JOIN `subjets`
ON lessons.subject_id = subjets.id
WHERE students.id = %s
'''
values = (student_id,)
cursor.execute(select_all_info, values)
print(cursor.fetchall())

db.commit()

db.close()
