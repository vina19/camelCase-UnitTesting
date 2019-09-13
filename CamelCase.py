#Convert sentence to camelCase
def camelcase(sentence):
    title_case = sentence.title()
    upper_camel_case = title_case.replace(' ', '')
    return upper_camel_case[0:1].lower() + upper_camel_case[1:]

#displaying the banner
def display_banner():
    msg = 'Awesome camelCaseGenerator program'
    instructions = 'Start with entering a sentence to convert to camelCase'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')
    print(f'\n {stars} \n {instructions} \n {stars}\n')

def main():
    display_banner()
    
    #inputing the sentence from the user
    sentence = input("Please enter a sentence: ")
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()