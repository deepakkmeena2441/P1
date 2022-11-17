import random
print("Word Puzzle Game")
score=0
list_words=["father","red","deepak","priya","engineering","oollege","mahadev"]

list_words.sort(reverse=False)
i=0
while i<=4:
    d=list(list_words[i])
    random.shuffle(d)
    print("Arrange the letters to form a valid word ")
    print(" ".join(d))
    str=input()
    if list_words[i]==str:
        print()
        print("Correct")
        score+=1
    else:
        print("Wrong")
        score-=1
    i+=1
print("Net Score is ",score)




    
