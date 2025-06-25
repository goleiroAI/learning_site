from django import template

register = template.Library()

@register.filter
def get_progress_color(percent):
    percent = int(percent)
    if percent <= 50:
        ratio = percent / 50
        r = int(0 + (128 - 0) * ratio)
        g = int(123 - (123 - 0) * ratio)
        b = int(255 - (255 - 128) * ratio)
    else:
        ratio = (percent - 50) / 50
        r = int(128 + (220 - 128) * ratio)
        g = int(0 + (53 - 0) * ratio)
        b = int(128 - (128 - 69) * ratio)
    return f'rgb({r}, {g}, {b})'
