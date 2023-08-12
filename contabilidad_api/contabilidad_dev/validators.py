import re
from django.core.exceptions import ValidationError

def validate_dominican_legal_document(value):
    # Regular expression pattern for valid ID or RNC format
    pattern = r'^\d{9}$|^\d{11}$'

    if not re.match(pattern, value):
        raise ValidationError('Enter a valid Dominican ID or RNC.')
