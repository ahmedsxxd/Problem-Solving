def get_num_vowels (str_):
    counter = 1
    translation = ""
    for letter in str_:
        if letter.lower() in "aeuio":
            translation = translation + str(counter)
            counter = counter +1
        else:
            translation = translation + letter
    return translation
    
user_phrase = input('Enter your Phrase: ')
print('Number of vowels & Place: ' + get_num_vowels(user_phrase)) 
input(KeyboardInterrupt)