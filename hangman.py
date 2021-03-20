import random 

život=6
text=open('hangman.txt').read().splitlines() # automaticky urobi list 
slovo=random.choice(text)
slovos=[]
for i in range(0, len(slovo)):
    slovos.append("*")
print("Dlzka slova je : " + str(len(slovo)))
while život>0:

    vstup=input("Zadaj pismeno: ")
    for i in range(0, len(slovo)):
        if vstup in slovo[i]:
            slovos[i]=vstup
            život+=1
    život-=1
    for i in range(0, len(slovo)):
        print(slovos[i], end=" ")
    if "*" not in slovos:
        život=0
        print("Uhadli ste, gratulujeme ")
    if život==0:
        pass
    else: 
        print("Ostava vam " + str(život ) + " života ")


        
       


