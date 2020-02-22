def xor_uncipher(str, key):
    uncript_str = ''
    for letter in str:
        uncript_str += chr(ord(letter) ^ key)
    return uncript_str

incr_strg = '㑮、㑣㐔㐐㑮、㐚㑯㐐㐚㑯、〛〈'
print('Оригинальная строка:\t', incr_strg)
key  = int(input('Введите ключ шифрования: '))

uncr_strg = xor_uncipher(incr_strg, key)
print('Расшифрованная строка по ключу ' + str(key) + ':\t', uncr_strg)

input('...')