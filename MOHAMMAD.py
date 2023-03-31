import requests,random,time

Z = '\033[1;31m' #احمر

X = '\033[1;33m' #اصفر

F = '\033[2;32m' #اخضر

C = "\033[1;97m" #ابيض

B = '\033[2;36m'#سمائي

Y = '\033[1;34m' #ازرق فاتح.

C = "\033[1;97m" #ابيض

E = '\033[1;31m'

B = '\033[2;36m'

G = '\033[1;32m'

S = '\033[1;33m'

Op = "MOO"

print(X+'*'*28)

azooz=f" {G} اكتب باسورد الادات حب "

print(azooz)

print(X+'*'*28)

def cls():

 os.system("clear")

def pas():

  J = input(f"{Z}اكتب باسورد الاداه   ")

  if J ==Op:

   print(F+"\n 🟢 تم الباسورد صح ")

   cls()

  else:

   print(Z+'  الباسورد خطأ🔴 ')

   pas()

pas()

print(f'''{G}[ {Z} استمتع بوقتك {G}]''')

token=input('Enter Token : '+X)

ID=input(G+'Enter ID : '+X)

print('')

print(f'        {Z}[    {G}بــداء الصــيــد   {Z}]          ')

print('')

user='alahmohamadaliabasfatmazhraallahvijfa'

num='6789'

while True:

 rng=int("".join(random.choice(num)for i in range(1)))

 emai=str("".join(random.choice(user)for i in range(rng)))

 

 email = emai+'@gmail.com'

 

 req = requests.get(f'https://CheckTiktokzaid.zaidbot.repl.co/2/email={email}').text

 

 if '"Email":"Good"' in req:

  

  print(f'{G} Good Email TikTok : {email}')

  print(f'{B} Goood Email : {email}')

  cc=(f'''

 Tik Tok [ادعلي بداعت امك ]

-----------------------------------------------

-----------------------------------------------

 يول ادعلي يول بداعت امك     

-----------------------------------------------

-----------------------------------------------

  Gmail »»» :    {email}

-----------------------------------------------

-----------------------------------------------  

  PY : @M0773_M

  Tle : https://t.me/B4_4U

 -----------------------------------------------

 -----------------------------------------------

   ''')

  

  requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(cc))

  print(cc)

 else:

  print(f'{X} Bad Email TikTok : {email}')

