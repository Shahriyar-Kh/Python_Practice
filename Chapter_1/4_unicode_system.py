#unicode system in python 
#unicode is a standard for representing text in different languages and scripts. It assigns a unique code point to each character, which can be used to represent the character in a computer system. In python, we can use unicode to represent characters from different languages and scripts.

#string to bytes or encode
string="Shahriyar khan"
tobyte=string.encode("utf-8") #utf-8 is a variable length encoding that can represent all unicode characters. It uses 1 to 4 bytes to represent a character depending on the character. It is the most commonly used encoding for unicode characters.
print(tobyte)

#bytes to string or decode
#encode is the process of converting a string to bytes, while decode is the process of converting bytes to a string. When we encode a string, we specify the encoding format (such as utf-8) that we want to use to represent the characters in bytes. When we decode bytes, we specify the encoding format that was used to encode the bytes so that it can be correctly converted back to a string.
#decode the bytes to string

print(tobyte.decode("utf-8"))
string1="khan"
tobyte1=string1.encode('utf-8')
print(tobyte1)
print(tobyte1.decode('utf-8'))