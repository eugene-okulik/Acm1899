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

subjects = [
    ('chemistry29',),
    ('biology29',)
]
insert_subjects_query = "INSERT INTO `subjets` (title) VALUES (%s)"
cursor.executemany(insert_subjects_query, subjects)
cursor.execute("SELECT id FROM `subjets` ORDER BY id DESC LIMIT %s", (len(subjects),))
subject_ids = [row["id"] for row in cursor.fetchall()]

lessons = [
    ('lesson1', subject_ids[0]),
    ('lesson2', subject_ids[0]),
    ('lesson3', subject_ids[1]),
    ('lesson4', subject_ids[1])
]
insert_lessons_query = "INSERT INTO `lessons` (title, subject_id) VALUES (%s, %s)"
cursor.executemany(insert_lessons_query, lessons)
cursor.execute("SELECT id FROM `lessons` ORDER BY id DESC LIMIT %s", (len(lessons),))
lesson_ids = [row["id"] for row in cursor.fetchall()]

marks = [
    (0, lesson_ids[0], student_id),
    (1, lesson_ids[1], student_id),
    (2, lesson_ids[2], student_id),
    (3, lesson_ids[3], student_id)
]
insert_marks_query = "INSERT INTO `marks` (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(insert_marks_query, marks)

cursor.execute(f'SELECT * from marks where student_id = {student_id}')
print(cursor.fetchall())

cursor.execute(f'SELECT * from books where taken_by_student_id = {student_id}')
print(cursor.fetchall())

select_all_info = f'''
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
WHERE students.id = {student_id}
'''
cursor.execute(select_all_info)
print(cursor.fetchall())

db.commit()

db.close()
