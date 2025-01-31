#!/usr/bin/env python3
"""
This module contains a class that filters out sensitive information from logs.
"""

import re
import logging
from typing import List, Tuple

# Import RedactingFormatter and filter_datum
RedactingFormatter = __import__('filtered_logger').RedactingFormatter

# Define PII fields that should be redacted in logs
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


# Define filter_datum function
def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns a log message with sensitive information filtered out.

    Arguments:
        fields (List[str]): list of strings representing all fields to filter.
        redaction (str): A string representing sequence to replace each field.
        message (str): A string representing log message.
        separator (str): A string representing separator for each field.

    Returns:
        str: The log message with information filtered out.
    """
    return re.sub(
        fr'({"|".join(fields)})=[^{separator}]*',
        lambda match: match.group(1) + "=" + redaction,
        message
    )


# Define RedactingFormatter class
class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class

    Attributes:
    REDACTION (str): A string representing sequence to replace each field.
    FORMAT (str): A string representing the format of the log message.
    SEPARATOR (str): A string representing separator for each field.

    Methods:
    format(self, record: logging.LogRecord) -> str:
        Formats a record for display.

    Arguments:
        record (logging.LogRecord): The record to format.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes RedactingFormatter object

        Arguments:
            fields (List[str]): list of string representing all fields filtered
            redaction (str): A string representing sequence to replace field.
            message (str): A string representing log message.
            separator (str): A string representing separator for each field.
            format (str): A string representing the format of the log message.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
        """
        Formats a record for display.

        Arguments:
            self (RedactingFormatter): The RedactingFormatter object.
            record (logging.LogRecord): The record to format.
            NotImplementedError: An error thats raised when an abstract method

        Returns:
            str: The formatted record.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named 'user_data'.

    - Logs only up to logging.INFO level.
    - Does not propagate messages to other loggers.
    - Uses a StreamHandler with RedactingFormatter to filter PII.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger
