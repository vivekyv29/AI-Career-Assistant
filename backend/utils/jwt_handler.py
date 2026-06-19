from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "super_secret_key"
ALGORITHM = "HS256"


def create_access_token(data):

    to_encode = data.copy()

    # Token valid for 7 days
    expire = datetime.utcnow() + timedelta(days=7)

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def verify_token(token):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("PAYLOAD =", payload)

        return payload

    except JWTError as e:

        print("JWT ERROR =", e)

        return None