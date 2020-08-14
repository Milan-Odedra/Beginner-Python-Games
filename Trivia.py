print("Hello, welcome to trivia!")

ans = input("Are you ready to play (yes/no): ")
score = 0
total_q = 4

if ans.lower() == "yes":
    ans = input("1. What is the best programming language? ")
    if ans.lower() == "python":
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        
        
    ans = input("2. What is 2 + 8 + 9 -1 ? ")
    if ans == "18":
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        
        
        

    ans = input("3. Who is better in your opinion messi or ronaldo ")
    if ans.lower() == "messi" or ans.lower() == 'ronaldo':
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
    
    
    ans = input("4. Who came runners up in the 2018 Champions League Final ")
    if ans.lower() == "liverpool":
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        
        
print("Thank you for playing, you got", score, "questions correct ")
mark = (score/total_q) * 100

print("Mark: ", str (mark) + "%")
print("Goodbye")



# Answers 1(python), 2(18), 3(messi or ronaldo), 4(liverpool).
