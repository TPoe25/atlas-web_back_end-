#!/usr/bin/env python3
"""
This module contains a class that filters out sensitive information from logs.
"""

import re
import logging
from typing import List


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

    items = message.split(separator)
    for i, item in enumerate(items):
        for field in fields:
            if item.startswith(field + "="):
                items[i] = field + "=" + redaction
    return separator.join(items)


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
