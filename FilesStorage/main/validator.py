from django.core.exceptions import ValidationError


def file_size(value):  # add this to some file where you can import it from
    limit = 104861614
    print(value.size)
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 100 MiB.')