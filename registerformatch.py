import ast

teamname=input("Team name: ")

k="team"+teamname+".txt"

try:
    f=open(k, 'r')
    s=f.read()
    f.close()
    d=ast.literal_eval(s)
    pwod=input("Enter your team key: ")
    if pwod == d[14]:
        d.pop(14)
        g=open("team1.txt", 'w')
        g.write(str(d))
        g.close()
        print("Team",teamname,"is now ready to play a match!")
        pwod=input("Enter your password: ")
        h=open("gpascd.txt",'w')
        h.write(pwod)
        h.close()
        print("Your password is",pwod)
    else:
        print("Looks like you forgot your key. Contact support for more details")

except:
    print("Team",teamname,"is not registered with the software.")

