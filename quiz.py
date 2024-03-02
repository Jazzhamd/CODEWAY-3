q1="Q1:Who is the director of the Godfather trilogy?"
ans1="Francis Ford Coppola"
q2="Q2:\"It's not who I am underneath, it's what I do that defines me.\"This line was said by Batman in which film?"
ans2="Batman Begins"
q3="Q3:How many actors have played the character of Spider-man in live action film adaptations?"
ans3="Four"
q4="Q4:Which Indian actor has the highest number of Oscar submissions?"
ans4="Kamal Haasan"
q5="Q5:Who is the first Indian actor to act in four film formats (black and white, colour, 3D and motion capture)?"
ans5="Rajinikanth"
welcomeMessage="Welcome to this quiz on cinema!"
rules="There will be five questions, each carrying one point. No points will be deducted for incorrect answers. All the best!"
print(welcomeMessage)
print("\n",rules)
print('\n')
Continue=1
while(Continue):
    score=0
    print(q1)
    print("a)Steven Spielberg\nb)James Cameron\nc)Francis Ford Coppola\nd)Stanley Kubrick")
    ch=input("\nEnter your choice:")
    if(ch=="c"):
        print("\nCorrect answer!")
        score+=1
    else:
        print("\nIncorrect answer.\nCorrect choice:c Your choice:",ch)
    print(q2)
    print("a)Dark Knight(2008)\nb)Batman Begins(2005)\nc)The Batman(2022)\nd)Dark Knight Rises(2012)")
    ch=input("\nEnter your choice:")
    if(ch=="b"):
        print("\nCorrect answer!")
        score+=1
    else:
        print("\nIncorrect answer.\nCorrect choice:b Your choice:",ch)
    print(q3)
    print("a)One\nb)Five\nc)Three\nd)Four")
    ch=input("\nEnter your choice:")
    if(ch=="d"):
        print("\nCorrect answer!")
        score+=1
    else:
        print("\nIncorrect answer.\nCorrect choice:d Your choice:",ch)
    print(q4)
    print("a)Amitabh Bachchan\nb)Kamal Haasan\nc)Naseerudin Shah\nd)Irrfan Khan")
    ch=input("\nEnter your choice:")
    if(ch=="b"):
        print("\nCorrect answer!")
        score+=1
    else:
        print("\nIncorrect answer.\nCorrect choice:b Your choice:",ch)
    print(q5)
    print("a)Kamal Haasan\nb)Amitabh Bhachchan\nc)Rajinikanth\nd)Chiranjeevi")
    ch=input("\nEnter your choice:")
    if(ch=="c"):
        print("\nCorrect answer!")
        score+=1
    else:
        print("\nIncorrect answer.\nCorrect choice:c Your choice:",ch)
    print("\nScore:",score)
    Continue=int(input("\nPress 1 to play again or 0 to exit:"))
    if(Continue==0):
        break
    
