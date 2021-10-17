from django.core.exceptions import ValidationError


def file_size(value):
    '''Валидатор размера файла'''
    limit = 104861614
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 100 MiB.')