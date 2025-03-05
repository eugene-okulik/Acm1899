import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

current_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(current_path))
target_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
print(target_file_path)

with open(target_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

values_not_exist_in_db = []
for row in data:
    name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
    select_all_info = '''
    SELECT students.name, students.second_name, groups.title, books.title, subjets.title, lessons.title, marks.value
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
    WHERE students.name = %s AND students.second_name = %s AND groups.title = %s AND books.title = %s
    AND subjets.title = %s AND lessons.title = %s AND marks.value = %s
    '''
    values = (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value)
    cursor.execute(select_all_info, values)
    db_selection = cursor.fetchall()
    if len(db_selection) == 0:
        values_not_exist_in_db.append(row)
print(values_not_exist_in_db[1:])
