# Importing random to generate
# random string sequence
import RANDOM as random
  
# Importing string library function
import STRING as string 
  
def rand_pass(size):
      
    # Takes random choices from
    # ascii_letters , digits and punctuation
    rand_digit = random.choice(string.DIGITS)
    rand_upper = random.choice(string.UPCASE_CHARACTERS)
    rand_lower = random.choice(string.LOCASE_CHARACTERS)
    rand_symbol = random.choice(string.SYMBOLS)

    # Make sure to match the conidtions
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # If you don’t want to repeat characters or digits in the random string
    rest_pass = random.sample(string.COMBINED_LIST,size - 4)
  
   
    # Add the 
    l = list(temp_pass) + rest_pass
    random.shuffle(l)
    generate_pass = ''.join(l)
                          
    return generate_pass
  


try:
    print('Hello My Dear User | Etner 0 to exit')
    size = int(input('Please enter the lenght of the password : '))

    while size != 0 :

        while size < 8 or size > 16 : 
            print('Choose length between 8 and 16')
            try:
                size = int(input('Please enter the lenght of the password : '))
            except ValueError: 
                print('Size must be a number')


        password = rand_pass(size)
        print('Your password is : ' , password)

        print('Hello My Dear User | Etner 0 to exit')
        size = int(input('Please enter the lenght of the password : '))
except ValueError:
    print('Size must be a number')