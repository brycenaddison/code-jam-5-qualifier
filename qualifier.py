import random
import string


def generate_password(
    password_length: int = 8,
    has_symbols: bool = False,
    has_uppercase: bool = False,
    ignored_chars: list = None,
    allowed_chars: list = None
) -> str:
    """Generates a random password.

    The password will be exactly `password_length` characters.
    If `has_symbols` is True, the password will contain at least one symbol,
    such as #, !, or @.
    If `has_uppercase` is True, the password will contain at least one upper
    case letter.
    Any characters in 'ignored_chars' are guaranteed not to be used in the
    password.
    Only characters in 'allowed_chars' will be used in the password, if the
    list is present.
    """
    if ignored_chars is not None and allowed_chars is not None:
        raise UserWarning("Only one of ignored_chars and allowed_chars may "
                          "be passed at the same time.")

    if password_length < 1:
        return ""

    s = string.ascii_letters + string.digits + string.punctuation
    uppercase = string.ascii_uppercase
    symbols = string.punctuation

    if ignored_chars is not None:
        tmp = list(s)
        for char in tmp:
            for s in ignored_chars:
                if char == s:
                    tmp.remove(char)
        s = "".join(tmp)
        uppercase = "".join(set(s).intersection(uppercase))
        symbols = "".join(set(s).intersection(symbols))

    if allowed_chars is not None:
        s = "".join(set(s).intersection(allowed_chars))
        uppercase = "".join(set(uppercase).intersection(allowed_chars))
        symbols = "".join(set(uppercase).intersection(symbols))

    password = []

    for i in range(password_length):
        password.append(random.choice(s))

    if has_symbols and set(password).intersection(
            symbols) == set():

        i = random.randint(0, password_length - 1)
        password[i] = random.choice(symbols)

    if has_uppercase and set(password).intersection(
            uppercase) == set():

        i = random.randint(0, password_length - 1)
        password[i] = random.choice(uppercase)

    return "".join(password)
