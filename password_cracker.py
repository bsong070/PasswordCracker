import hashlib

def hash_compare(word,hash):
  hashed_word = hashlib.sha1(word.encode()).hexdigest()
  return hash == hashed_word

def crack_sha1_hash(hash, use_salts=False):

    with open('top-10000-passwords.txt') as top_pw:
      dictionary = top_pw.readlines()

    with open('known-salts.txt') as f:
      salts = f.readlines()

    for word in dictionary:
      word = word.strip()

      if use_salts:
        for salt in salts:
          salt = salt.strip()
          salt_variation = [word + salt, salt + word]
          
          for salted_word in salt_variation:
            if hash_compare(salted_word, hash):
              return word
      else:
        if hash_compare(word,hash):
          return word

    return 'PASSWORD NOT IN DATABASE'