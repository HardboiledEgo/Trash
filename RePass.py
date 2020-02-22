def xor_uncipher(str, key):
    uncript_str = ''
    for letter in str:
        uncript_str += chr(ord(letter) ^ key)
    return uncript_str

incr_strg = str(input('Шифруемый пароль: '))
key  = int(input('Шифр-ключ(только цифры!): '))

uncr_strg = xor_uncipher(incr_strg, key)
print('Зашифрованный пароль по ключу ' + str(key) + ': ', uncr_strg)