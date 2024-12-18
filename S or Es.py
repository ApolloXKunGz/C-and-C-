"""s or es"""
def pluralize(word):
    """ตรวจสอบว่าต้องเติม s es หรือ ies"""
    if word.endswith(('s', 'sh', 'ch', 'x', 'z', 'o')):#ถ้าลงท้ายด้วยพวกนี้ให้เติม es ได้เลย
        return word + 'es'
    elif word.endswith('y'):#ถ้าลงท้ายด้วย y และหน้าy ไม่ใช่สระ ให้เปลี่ยนyเป็น i แล้วเติม es
        if len(word) > 1 and word[-2] not in 'aeiou':
            return word[:-1] + 'ies'
        else:#ถ้าลงท้ายด้วย y และหน้า y เป็นสระ ให้เติมs ได้เลย
            return word + 's'
    else:
        return word + 's'

input_word = input()
plural_word = pluralize(input_word)
print(plural_word)
