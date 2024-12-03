#Tells if a number is even or odd
def even_or_odd(number):
    if number %2 == 0:#modulo gives the remainder
        return("Even")
    else:
        return("Odd")

# Return a string of the number   
def number_to_string(num):
    return(str(num))

#count how many vowels are in a string
def get_count(sentence):
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for letter in sentence:#splitting the sentence into individual lettere
        if letter in vowel:#comparing the letters to the list of vowels
            count +=1 #adding to the count
    return(count)