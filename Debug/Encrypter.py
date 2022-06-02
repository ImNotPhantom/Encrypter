#! python -u

# Encrypt and decrypt a file using xor encryption

from xorCryptPy import xorCrypt
import os
import random
import time

def substring_after(s, delim):
    return s.partition(delim)[2]

while True:
    wtd = input('Encrypt or Decrypt? (e/d): ')

    if wtd == 'e':
        rk = input('\nDo you want to use a random key? (y/n): ')
        rk = rk.lower()

        if rk not in ['y', 'n']:
            print('\nInvalid answer!\n')
        file = input('\nFile to encrypt (with the file extention): ')
        if os.path.exists(file):
            eType = 'e'
            break
        else:
            print('File does not exist')
            continue
    elif wtd == 'd':
        urk = input('\nDid you use a random key? (y/n): ')
        urk = urk.lower()

        if urk not in ['y', 'n']:
            print('\nInvalid answer!\n')

        file = input('\nFile to decrypt (The .encfile\'s name): ')
        if os.path.exists(file + '.encfile'):
            eType = 'd'
            output = input('\nOutput file name (with the file extention): ')
            break
        else:
            print('\nFile does not exist')
    else:
        print('Invalid input')
        continue

while True:
    if eType == 'e':
        if rk == 'y':
            key = random.randint(1, 10)
        elif rk == 'n':
            key = 6
        with open(file, 'r') as f:
            data = f.read()
            eData = xorCrypt(data, key)
        with open(file.replace(substring_after(file, '.'), 'encfile'), 'w') as f:
            f.write(eData)
        if rk == 'y':
            print('Encrypted file: ' + file.replace(substring_after(file, '.'), 'encfile') + '\n\n⚠️Key: ' + str(key) + '⚠️')
            print('⚠️MAKE SURE TO REMEBER THE KEY⚠️\n\n')
        elif rk == 'n':
            print('Encrypted file: ' + file.replace(substring_after(file, '.'), 'encfile'))
        print('\n\nYou can find the encrypted file in the same directory as the original file')
        print('You can close this window now.\n')
        while True:
            time.sleep(1)
    elif eType == 'd':
        with open(file + ".encfile", 'r') as f:
            if urk == 'y': 
                key = int(input('\nKey: '))
            elif urk == 'n':
                key = 6
            data = f.read()
            dData = xorCrypt(data, key)
        with open(output, 'w') as f:
            f.write(dData)
        print('Decrypted file: ' + output)
        print("\nYou can find the original file in the same directory as the decrypted file")
        print("You can close this window now.\n")
        while True:
            time.sleep(1)