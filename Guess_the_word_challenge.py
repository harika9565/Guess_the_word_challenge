import random
array=['mahatmagandhi', 'subhashchandrabose', 'bhagatsingh', 'sardarvallabhbhaipatel', 'jawaharlalnehru', 'balgangadhartilak', 'lalalajpatrai', 'ranilaxmibai', 'mahadeviverma', 'basantidevi']
randname=random.choice(array)
name=list(randname)
a=len(name)
display=[]
for i in range(0,a):
    display +="_"
print(display)
end_of_game=False
lives=a-4
while not end_of_game:
    n=input("\nenter an alphabet\n").lower()
    for position in range(a):
        letter= name[position]
        if(letter==n):
            display[position]=letter
    lives-=1
    print(display)
    if ("_" not in display or lives==0):
        end_of_game= True
        if("_" not in display):
            print("you won")
        else:
            print("you lost")
            name_str = ''.join(name)
            print(name_str)


