import re

with open('badassradio/settings.py', 'r') as f:
    content = f.read()

content = content.replace(
    'LANGUAGE_CODE = "en-us"',
    'LANGUAGE_CODE = "fr-fr"'
)

content = content.replace(
    'TIME_ZONE = "UTC"',
    'TIME_ZONE = "Europe/Paris"'
)

with open('badassradio/settings.py', 'w') as f:
    f.write(content)
