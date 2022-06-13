from Art import logo

print(logo)
user_name = input("Hello, what is your name?\n")
print(f"Welcome to to the Caesar Cipher, {user_name}")
alphabet = ['A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U'
    , 'V', 'W', 'X', 'Y', 'Z']
direction = input("Type \"encode\" to encrypt a message, or type \"decode\" to decrypt a message\n").lower()
text = input("Type your message:\n")
shift = int(input("Type the number that you wish to shift each letter by:\n"))

isVal = True
text.strip()
for letter in text:
    if letter.upper() not in alphabet and letter != " ":
        isVal = False
while isVal == False:
    text = input("Enter in another message and plz only enter in letters:").upper()
    for letter in alphabet:
        if letter.upper() in alphabet:
            isVal = True


def encrypt(text, shift):
    og = []
    for letter in text:
        og.append(letter)
    text = text.upper()
    newStr = ""
    list = []
    cipher = []
    count = 0
    for letter in text:
        list.append(letter)
    for letter in list:
        count += 1
        if letter == " ":
            cipher.append(letter)
        if letter != " ":
            value = shift + alphabet.index(letter)
            value -= count
            if letter.isupper():
                cipher.append(alphabet[shift + alphabet.index(letter)].strip())
            elif not letter.isupper():
                cipher.append(alphabet[shift + alphabet.index(letter)].strip())
    for x in range(len(og)):
        if not og[x].isupper():
            cipher[x] = cipher[x].lower()
    for letter in cipher:
        newStr += letter
    print(f"The encoded text is: {newStr}")


def decrypt(text, shift):
    og = []
    for letter in text:
        og.append(letter)
    text = text.upper()
    newStr = ""
    list = []
    cipher = []
    count = 0
    for letter in text:
        list.append(letter)
    for letter in list:
        count += 1
        if letter == " ":
            cipher.append(letter)
        if letter != " ":
            value = alphabet.index(letter) - shift
            if letter.isupper():
                cipher.append(alphabet[value].strip())
            elif not letter.isupper():
                cipher.append(alphabet[value].strip())
    for x in range(len(og)):
        if not og[x].isupper():
            cipher[x] = cipher[x].lower()
    for letter in cipher:
        newStr += letter
    print(f"The decoded text is: {newStr}")


if direction == "encode" and isVal:
    encrypt(text=text, shift=shift)
if direction == "decode" and isVal:
    decrypt(text=text, shift=shift)
