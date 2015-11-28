print('bonjour')
if 3 > 2:
    print('It works!')
if 5>15:
    print('vrai')
else:
    print('faux')



age = 40
if age <18:
    print('Bonjour Madame!')
elif age>=18 and age <=35:
    print('Bonjour Monsieur')
else:
    print('Vous n\'avez pas rempli le champ!')

def saluer(nom):
    if nom == 'eric':
        print('Bonjour eric !')
    else :
        print('bonjour ' + nom)

saluer('')
saluer('florence')

clients=['isabelle','marc','paul','laure','eric']
for client in clients:
    saluer(client)

def cout(arome):
    if arome=='citron':
        print('le macaron citron coute 1 euro')
        #else print

macarons=['citron','orange','framboise','chocolat']
for arome in macarons:
        saluer(arome)
        cout(arome)
