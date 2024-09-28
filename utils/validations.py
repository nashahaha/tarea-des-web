import re
import filetype

def validate_username(value):
    return value and len(value) > 4