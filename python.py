print ( "        How I Get Dressed Up Every Morning?       " )
print ( "-----------------------------------" ) 
print ( "I have to decide what should I wear Today hmm" ) 
print ( "-----------------------------------" ) 
print ( "Let's start" ) 
print ( "-----------------------------------" ) 
print ( "Firstly, I'll get up from my bed" ) 
print ( "Then i'll go to the bathroom to take shower" ) 
print ( "Then i'll get back to my closet to pick up my clothes" ) 
print ( "There i'll decide which shirt I should wear" ) 

ans = []

list = ["Sweat Shirt","T-Shirt","Check Shirt"] 
for shirts in list:
    a = input(f"Should I wear a {shirts} ? (y/n)")
    if a == 'y' or a == 'Y':
        print(f"Okay I'll wear {shirts}")
        ans.append(shirts)
        break
print ( "-----------------------------------" ) 
print ( "Great, Now I should choose Pants" ) 
print ( "-----------------------------------" )

list = ['Pant','Jeans','Shorts']
for pants in list:
    a = input(f"Should I wear a {pants} ? (y/n)")
    if a == 'y' or a == 'Y':
        print(f"Okay I'll wear {pants}")
        ans.append(pants)
        break

print ( "-----------------------------------" ) 
print ( "Great, Now I should choose Shoes" ) 
print ( "-----------------------------------" ) 

list = ['Sneakers','Flip Flop','Sandal']
for shoes in list:
    a = input(f"Should I wear a {shoes} ? (y/n)")
    if a == 'y' or a == 'Y':
        print(f"Okay I'll wear {shoes}")
        ans.append(shoes)
        break

print ( "-----------------------------------" ) 
print ( "Great, Now I should choose socks" ) 
print ( "-----------------------------------" ) 

BlueSocks   =   'BlueSocks' 
RedSocks   =   'RedSocks' 
BlackSocks   =   'BlackSocks' 
list = ['Blue Socks','Red Socks','Black Socks']
for socks in list:
    a = input(f"Should I wear a {socks} ? (y/n)")
    if a == 'y' or a == 'Y':
        print(f"Okay I'll wear {socks}")
        ans.append(socks)
        break

print ( "-----------------------------------" ) 
print ( "Great, I have completed my dressing" ) 
print ( "-----------------------------------" )

print ("I will wear", end =" ")
for item in ans:
    print(item, end = " ")