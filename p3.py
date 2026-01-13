import hashlib
def get_sha256_hash(text):
    sha_signature=hashlib.sha256(text.encode()).hexdigest()
    return sha_signature
text="cynersecurity is important!"
print(f"text:{text}")
print(f"sha-256 hash:{ get_sha256_hash(text)}")
