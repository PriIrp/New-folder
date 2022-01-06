#Each number has a few letters assigned to it
#1 and 0 have no value, so will be omitted
NUM_LETTER_DICT = { 
                    "1": "",
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz",
                    "0": ""
                    }

#Pre-Conditions - The number inputted will be a 6 digit pin code

def askUser():
    run = True
    while run:
        try:
            print("\nPlease enter your 6 digit pin in such format xxxxxx")
            str = input()
            if len(str ) == 6:
                run = False
        except:
            pass
    return str


def translate(str):
    letter_list = []
    for num in range(len(str)):
        letters = NUM_LETTER_DICT.get(str[num])
        if letters != "":
            letter_list.append(letters)
        else:
            pass
    return letter_list   


#So main part of the program goes through each element in the list
#It will take the len of the element and 


def comboGenerator(list, num):
    combos = []
    progress = ""
    # for a in range(len(list[0])):
    #     progress += list[0][a]
    #     for b in range(len(list[1])):
    #         progress += list[1][b]
    #         for c in range(len(list[2])):
    #             progress += list[2][c]
    #             for d in range(len(list[3])):
    #                 progress += list[3][d]
    #                 for e in range(len(list[4])):
    #                     progress += list[4][e]
    #                     for f in range(len(list[5])):
    #                         progress += list[5][f]
    #                         combos.append(progress)
    #                         progress = ""
    
        
       
    return combos
        


def combination(list):      #Calculates and returns the number of combinations of words
    num_combos = 1
    for i in range(len(list)):
        num_combos *= len(list[i])
    return num_combos
 

str = askUser()
print(translate(str))
list = translate(str)
combinations = combination(list)
print(f"Possible combos = {combinations}")
#print(comboGenerator(list))
#2019812160