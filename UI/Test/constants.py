USER_PHONE_TEST_DATA = [
    ("mailto:valid@example.com", "False"),
    ("1", "True"),
    ("-", "True"),
    (" ", "True"),
    ("1244545754", "True"),
    (";", "False"),  # bug
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "False"),
    ("11111111111111111111111111111111111111111111111111111111111", "True")  # bug
]

LAST_NAME_TEST_DATA = [
    {"lastname": "mailto:valid@example.com", "is_valid": "True"},
    {"lastname": "invalid@", "is_valid": "True"},
    {"lastname": "missing_at_example.com", "is_valid": "True"},
    {"lastname": "mailto:valid.email@example.com", "is_valid": "True"},
    {"lastname": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "is_valid": "False"},
]

USERNAME_TEST_DATA = [
    {"username": "mailto:valid@example.com", "is_valid": "True"},
    {"username": "invalid@", "is_valid": "True"},
    {"username": "missing_at_example.com", "is_valid": "True"},
    {"username": "mailto:valid.email@example.com", "is_valid": "True"},
    {"username": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "is_valid": "False"},
]

EMAIL_TEST_DATA = [
    {"email": "mailto:valid@example.com", "is_valid": "True"},
    {"email": "invalid@", "is_valid": "False"},
    {"email": "missing_at_example.com", "is_valid": "False"},
    {"email": "mailto:valid.email@example.com", "is_valid": "True"},
    {"email": "", "is_valid": "False"},
]