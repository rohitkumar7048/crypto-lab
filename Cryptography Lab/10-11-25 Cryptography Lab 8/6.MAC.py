import hmac
import hashlib
import secrets
from typing import Union

BytesLike = Union[bytes, bytearray]


def gen_key(length: int = 32) -> bytes:
    """Generate a cryptographically secure random key (default 32 bytes = 256 bits)."""
    return secrets.token_bytes(length)

def _to_bytes(data: Union[str, BytesLike]) -> bytes:
    """Ensure input is bytes (UTF-8 if string)."""
    return data.encode('utf-8') if isinstance(data, str) else bytes(data)


def mac_hmac_sha256(key: bytes, message: Union[str, BytesLike]) -> bytes:

    return hmac.new(key, _to_bytes(message), hashlib.sha256).digest()

class HMACStream:

    def __init__(self, key: bytes):
        self._h = hmac.new(key, digestmod=hashlib.sha256)

    def update(self, chunk: Union[str, BytesLike]):
        self._h.update(_to_bytes(chunk))

    def digest(self) -> bytes:
        return self._h.digest()

    def hexdigest(self) -> str:
        return self._h.hexdigest()


def verify_mac(key: bytes, message: Union[str, BytesLike], tag: bytes) -> bool:

    expected = mac_hmac_sha256(key, message)
    return hmac.compare_digest(expected, tag)

def mac_file(path: str, key: bytes, chunk_size: int = 8192) -> bytes:

    h = hmac.new(key, digestmod=hashlib.sha256)
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.digest()


if __name__ == "__main__":
    # generate a key
    key = gen_key()  
    print("Key (hex):", key.hex())


    message = "hello world"
    tag = mac_hmac_sha256(key, message)
    print("MAC (hex):", tag.hex())


    ok = verify_mac(key, message, tag)
    print("Verify ok:", ok)


    stream = HMACStream(key)
    stream.update("hello ")
    stream.update("world")
    print("Streaming MAC matches one-shot:", hmac.compare_digest(stream.digest(), tag))
