AES128_KEY_SIZE = 16  # size of an AES218 key
NONCE_SIZE = 12  # size of an AESGCM nonce
TAG_SIZE = 32  # size of the tag packet prefix
MAGIC_SIZE = 32  # size of the magic hash in the who are you packet

MAX_PACKET_SIZE = 1280  # maximum allowed size of a packet

AUTH_SCHEME_NAME = b"gcm"  # the name of the only supported authentication scheme

TOPIC_HASH_SIZE = 32  # size of a topic hash
IP_V4_SIZE = 4  # size of an IPv4 address
IP_V6_SIZE = 16  # size of an IPv6 address

ENR_REPR_PREFIX = "enr:"  # prefix used when printing an ENR
MAX_ENR_SIZE = 300  # maximum allowed size of an ENR
