import uuid
import random
import hashlib

from string import (
    ascii_lowercase,
    ascii_uppercase
)

def generate_uuid(data: str) -> str:
    """ Generates a UUID for database's primary keys """
    data = f"{data}{random.choices([char for char in ascii_lowercase + ascii_uppercase], k=21)}" # Add more random charachter to the data to make the UID more random and unique

    hashed_data_salt = hashlib.md5(data.encode()).hexdigest()
    generated_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, hashed_data_salt)

    return str(generated_uuid)
