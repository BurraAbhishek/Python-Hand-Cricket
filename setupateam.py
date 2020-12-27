import random
import string
import time

def rand_pass(size):
    generate_pass = ''.join([random.choice( string.ascii_uppercase + string.ascii_lowercase + string.digits)
                             for n in range(size)])
    return generate_pass
n=random.randint(8,12)
pwod=rand_pass(n)

print("Welcome to Python based hand cricket")
print("NOTE: Team names '1', 'Computer' and 'CPU' are system reserved. Hence, they are not allowed.")
teamname=input("Team name: ")
if teamname=='1' or teamname=='CPU' or teamname=='Computer':
    pd=input("System reserved, can't give you chosen team. Hit enter, and then try again.")
else:
    k="team"+teamname+".txt"
    try:
        f=open(k, 'r')
        f.close()
        pb=input("Team name exists already, hence can't give you same team. Hit enter, and then try again.")
    except:
        ta=input("Player ID 1: ")
        tb=input("Player ID 2: ")
        tc=input("Player ID 3: ")
        td=input("Player ID 4: ")
        te=input("Player ID 5: ")
        tf=input("Player ID 6: ")
        tg=input("Player ID 7: ")
        th=input("Player ID 8: ")
        ti=input("Player ID 9: ")
        tj=input("Player ID 10: ")
        tk=input("Player ID 11: ")
        l=[teamname,ta,tb,tc,td,te,tf,tg,th,ti,tj,tk,0,0,pwod]
        s=str(l)
        print("Team registration in progress...")

        f=open(k, 'w')
        f.write(s)
        f.close()

        print("Registered. Open Match registration file to play match")
        print("ATTENTION! Your team key is ",pwod," . Keep it safe because you need it every time you register for a match")
        pa=input()

