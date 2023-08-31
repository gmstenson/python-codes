
def main():

    print()
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    statement_1 = input("1. I feel that I am a person of worth, at least on an equal plane with others. \nEnter D, d, a, or A: ")
    statement_2 = input("2. I feel that I have a number of good qualities. \nEnter D, d, a, or A: ")
    statement_3 = input("3. All in all, I am inclined to feel that I am a failure. \nEnter D, d, a, or A: ")
    statement_4 = input("4. I am able to do things as well as most other people. \nEnter D, d, a, or A: ")
    statement_5 = input("5. I feel I do not have much to be proud of. \nEnter D, d, a, or A: ")
    statement_6 = input("6. I take a positive attitude toward myself. \nEnter D, d, a, or A: ")
    statement_7 = input("7. On the whole, I am satisfied with myself. \nEnter D, d, a, or A: ")
    statement_8 = input("8. I wish I could have more respect for myself. \nEnter D, d, a, or A: ")
    statement_9 = input("9. I certainly feel useless at times. \nEnter D, d, a, or A: ")
    statement_10 = input("10. At times I think I am no good at all. \nEnter D, d, a, or A: ")


    if statement_1 == "D":
        score_1 = 0
    elif statement_1 == "d":
        score_1 = 1
    elif statement_1 == "a":
        score_1 = 2
    elif statement_1 == "A":
        score_1 = 3


    if statement_2 == "D":
        score_2 = 0
    elif statement_2 == "d":
        score_2 = 1
    elif statement_2 == "a":
        score_2 = 2
    elif statement_2 == "A":
        score_2 = 3

    
    if statement_3 == "D":
        score_3 = 3
    elif statement_3 == "d":
        score_3 = 2
    elif statement_3 == "a":
        score_3 = 1
    elif statement_3 == "A":
        score_3 = 0

    
    if statement_4 == "D":
        score_4 = 0
    elif statement_4 == "d":
        score_4 = 1
    elif statement_4 == "a":
        score_4 = 2
    elif statement_4 == "A":
        score_4 = 3

    
    if statement_5 == "D":
        score_5 = 3
    elif statement_5 == "d":
        score_5 = 2
    elif statement_5 == "a":
        score_5 = 1
    elif statement_5 == "A":
        score_5 = 0

    
    if statement_6 == "D":
        score_6 = 0
    elif statement_6 == "d":
        score_6 = 1
    elif statement_6 == "a":
        score_6 = 2
    elif statement_6 == "A":
        score_6 = 3

    
    if statement_7 == "D":
        score_7 = 0
    elif statement_7 == "d":
        score_7 = 1
    elif statement_7 == "a":
        score_7 = 2
    elif statement_7 == "A":
        score_7 = 3


    if statement_8 == "D":
        score_8 = 3
    elif statement_8 == "d":
        score_8 = 2
    elif statement_8 == "a":
        score_8 = 1
    elif statement_8 == "A":
        score_8 = 0

    
    if statement_9 == "D":
        score_9 = 3
    elif statement_9 == "d":
        score_9 = 2
    elif statement_9 == "a":
        score_9 = 1
    elif statement_9 == "A":
        score_9 = 0

    
    if statement_10 == "D":
        score_10 = 3
    elif statement_10 == "d":
        score_10 = 2
    elif statement_10 == "a":
        score_10 = 1
    elif statement_10 == "A":
        score_10 = 0

    total = score_1 + score_2 + score_3 + score_4 + score_5 + \
            score_6 + score_7 + score_8 + score_9 + score_10

    print(f"\nYour score is {total}.")
    print("A score below 15 may indicate problematic low self-esteem.")

main()