from django.dispatch import Signal

post_rating = Signal(providing_args=['instance', 'value', 'is_negative'])
