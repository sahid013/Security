import math
from Crypto.Util import number  #pip install pycryptodome



def key_elgamal (bits=20):
  p = number.getPrime(bits-1)
  
  while True:
    g = number.getRandomRange(3, p+1)
    if (math.gcd(p, g) == 1):
      break

  x = number.getRandomRange(2, p-1)
  y = pow(g,x) % p
  return x, y, p, g




def encrypt_elgamal(g, p, m, y):
  r = number.getRandomRange(2, p-1)
  c1 = pow(g, r) % p
  c2 = (m * (pow(y, r) % p)) % p
  return c1, c2



def decrypt_elgamal(c1, c2, x, p):
  m = (c2 * (pow(c1, p-1-x) % p)) % p
  return m


m = int(input("Enter the message: "))
x,y,p,g = key_elgamal()
c1,c2 = encrypt_elgamal(g, p, m, y)
print("Cipher Text 1: ",c1)
print("Cipher Text 2: ",c2)

dm = decrypt_elgamal(c1, c2, x, p)
print("Decrypted Message: ",dm)
