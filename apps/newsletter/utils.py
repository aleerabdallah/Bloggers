import random
from django.http import HttpRequest
from hashids import Hashids



# hashids = Hashids(salt='the salt is alsulk', min_length=6)
hashids = Hashids()


def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

def build_absolute_path(request, obj_path):
    # host = request.get_host()
    return request.build_absolute_uri(str(obj_path.picture.url))


def encode_id(id: int):
    return hashids.encode(id)

def decode_id(id: int):
    return hashids.decode(id)


