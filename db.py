import pymysql
from dotenv import load_dotenv
import os
load_dotenv()


def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )

def insert_data(email, password):
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"))

        with connection.cursor() as cursor:
            sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
            cursor.execute(sql, (email, password))

        connection.commit()
        connection.close()
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

def login_data(email,password):
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email = %s and password = %s"
            cursor.execute(sql, (email, password))
            user = cursor.fetchone()

        connection.close()

        if user:
            return user['id']
        else:
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False

def transaction_history(user_id, limit=10):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM transactions WHERE user_id = %s ORDER BY DATE DESC LIMIT %s"
            cursor.execute(sql, (user_id, limit))
            return cursor.fetchall()
    finally:
        connection.close()

def get_total_spends(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT SUM(amount) AS total FROM transactions WHERE type='expense' AND user_id=%s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()

            if result and 'total' in result and result['total'] is not None:
                return float(result['total'])
            return 0
    finally:
        connection.close()

def get_total_income(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT SUM(amount) AS total FROM transactions WHERE type='income' AND user_id=%s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()

            if result and 'total' in result and result['total'] is not None:
                return float(result['total'])
            return 0
    finally:
        connection.close()

def add_transactions(user_id, amount, category):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO transactions (user_id, amount, category, type, `date`) VALUES (%s, %s, %s, 'expense', NOW())"
            cursor.execute(sql, (user_id, amount, category))
        connection.commit()
        return True
    finally:
        connection.close()

def adding_money_db(user_id, amount, category):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO transactions (user_id, amount, category, type, `date`) VALUES (%s, %s, %s, 'income', NOW())"
            cursor.execute(sql, (user_id, amount, category))
        connection.commit()
        return True
    finally:
        connection.close()

def delete_from_db(transaction_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM transactions WHERE id = %s"
            cursor.execute(sql, (transaction_id,))
        connection.commit()
        return True
    finally:
        connection.close()

def filter_data(current_user_id, category):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            if category == "All":
                sql = "SELECT * FROM transactions WHERE user_id = %s"
                cursor.execute(sql, (current_user_id,))
            else:
                sql = "SELECT * FROM transactions WHERE user_id = %s AND category = %s"
                cursor.execute(sql, (current_user_id, category))
            connection.commit()
            return cursor.fetchall()
    finally:
        connection.close()