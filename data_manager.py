import database_common


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def full_mentor_names(cursor):
    cursor.execute(" SELECT first_name, last_name FROM mentors; ")
    mentor_names = cursor.fetchall()
    return mentor_names


@database_common.connection_handler
def mentors_nicknames(cursor, city):
    cursor.execute('SELECT nick_name FROM mentors WHERE city = %(city)s;',
                   {'city': city})
    nick_names = cursor.fetchall()
    return nick_names


@database_common.connection_handler
def find_user(cursor, first_name):
    cursor.execute("""
    SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number FROM
    applicants WHERE first_name = %(first_name)s;
    """, {'first_name': first_name})
    user_details = cursor.fetchall()
    return user_details


@database_common.connection_handler
def find_by_email(cursor, email):
    cursor.execute("""
    SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
    FROM applicants WHERE email LIKE %(email)s;
    """, {'email': email})
    info_by_email = cursor.fetchall()
    return info_by_email


@database_common.connection_handler
def add_new_applicants(cursor, first_name, last_name, phone_number, email, application_code):
    cursor.execute("""
    INSERT INTO applicants(first_name, last_name, phone_number, email, application_code) VALUES(%s,%s, %s, %s, %s);
    """, (first_name, last_name, phone_number, email, application_code))


@database_common.connection_handler
def get_student_info(cursor, code):
    cursor.execute("""
    SELECT * FROM applicants WHERE application_code = %(application_code)s;
    """, {'application_code': code})
    student_info = cursor.fetchall()
    return student_info


@database_common.connection_handler
def update_telephone_number(cursor, telephone_number):
    cursor.execute("""
    UPDATE applicants SET phone_number = %(phone)s
    WHERE first_name = 'Jemima' AND  last_name = 'Foreman';
    """, {'phone': telephone_number})
    cursor.execute("""
    SELECT * FROM applicants WHERE first_name = 'Jemima' AND  last_name = 'Foreman';
    """)
    new_data = cursor.fetchall()
    return new_data


@database_common.connection_handler
def data_to_be_deleted(cursor, domain_name):
    cursor.execute("""
        SELECT FROM applicants WHERE email LIKE %(domain_name)s;
        """, {'domain_name': domain_name})
    results = cursor.fetchall()
    return results


@database_common.connection_handler
def delete_by_email_domain_name(cursor, domain_name):
    cursor.execute("""
    DELETE FROM applicants WHERE email LIKE %(domain_name)s;
    """, {'domain_name': domain_name})
