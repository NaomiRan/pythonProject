# object with key-value pair
# access to the key -> object["key"] or object.get(key,"default value")
# the difference above is [] will yell if the key doesn't exist
message = input("> ")
# split the message with delimiter ' ' and return an array
words = message.split(' ')
emojis = {
    ":)": "😁",
    ":(": "😂"
}
output = ""
for word in words:
    output += emojis.get(word,word) + " "
print(output)