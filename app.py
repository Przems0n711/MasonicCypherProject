from flask import Flask, request, render_template

app = Flask(__name__)

encoding_table = ['H', 'Q', 'G', 'P', 'V', 'Z', 'B', 'M', 'X', 'D', 'L', 'T', 'C', 'J', 'K', 'R', 'E', 'W', 'A', 'F', 'Y', 'N', 'I', 'U', 'O', 'S']
decoding_table = ['⸦', '⸕', '⎵', '⸙', '⸖', '⸞', '⸘', '⸗', '⸧', '⸥', '⸪', '⸔', '⸝', '⸠', '⸡', '⸤', '⸢', '⸣', '⸬', '⸫', '⸩', '⸨', '⸜', '⸟', '⸛', '⸚']

def encrypt(plaintext):
  plaintext = plaintext.upper()
  ciphertext = ""
  for x in plaintext:
    if x in decoding_table:
      ciphertext += encoding_table[decoding_table.index(x)]
    else:
      ciphertext += x
  return ciphertext

def decrypt(ciphertext):
  ciphertext = ciphertext.upper()
  plaintext = ""
  for x in ciphertext:
    if x in encoding_table:
        plaintext += decoding_table[encoding_table.index(x)]
    else:
        plaintext += x
  return plaintext

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/encrypt', methods=['POST'])
def handle_encrypt():
  # Get the plaintext from the request body
  plaintext = request.form['plaintext']
  ciphertext = encrypt(plaintext)
  return f'Plaintext: {ciphertext}'

@app.route('/decrypt', methods=['POST'])
def handle_decrypt():
  # Get the ciphertext from the request body
  ciphertext = request.form['ciphertext']
  plaintext = decrypt(ciphertext)
  return f'Cyphertext: {plaintext}'
  return plaintext

if __name__ == '__main__':
  app.run()