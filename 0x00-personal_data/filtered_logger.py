#!/usr/bin/env python3
"""
This module provides a function to filter out sensitive information
from log messages by replacing specified field values with a redaction string.
"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Obfuscates sensitive information in a log message.

    Args:
        fields (List[str]): List of field names to obfuscate.
        redaction (str): String to replace field values.
        message (str): The log message to process.
        separator (str): The separator character between fields in the message.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(
            f"{field}=.*?{separator}",
            f"{field}={redaction}{separator}",
            message
        )
    return message
