#!/usr/bin/env python3
"""A simple logger that hides private information like email or password.
"""

import logging
import re
import os
import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from typing import List, Tuple, Optional

# List of sensitive fields we want to hide
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Replaces the values of sensitive fields in a message with a redacted string.
    """
    pattern = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """
    Custom log formatter that hides sensitive info.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        # Save the list of fields we want to hide
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        # Hide sensitive fields in the log message
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Sets up a logger that hides sensitive info in its output.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Don’t send logs to parent loggers

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db() -> Optional[MySQLConnection]:
    """
    Connects to the MySQL database using environment variables.
    """
    try:
        username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
        password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
        host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
        db_name = os.getenv('PERSONAL_DATA_DB_NAME')

        if not db_name:
            raise ValueError("Missing database name in environment")

        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=db_name
        )

        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None


def main():
    """
    Connects to the DB, gets user data, and logs it while hiding PII fields.
    """
    db = get_db()
    if not db:
        return

    logger = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    # Get the column names like 'name', 'email', etc.
    columns = [col[0] for col in cursor.description]

    for row in cursor:
        # Turn each row into "column=value" format
        message = "; ".join(
            f"{col}={str(val)}" for col, val in zip(columns, row)
        )
        message += ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
