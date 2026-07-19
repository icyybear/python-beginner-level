print('''
                                     ._
                                   ,(  `-.
                                 ,': `.   `.
                               ,` *   `-.   \
                             ,'  ` :+  = `.  `.
                           ,~  (o):  .,   `.  `.
                         ,'  ; :   ,(__) x;`.  ;
                       ,'  :'  itz  ;  ; ; _,-'
                     .'O ; = _' C ; ;'_,_ ;
                   ,;  _;   ` : ;'_,-'   i'
                 ,` `;(_)  0 ; ','   
               .';6     ; ' ,-'~
             ,' Q  ,& ;',-.'
           ,( :` ; _,-'~  ;
         ,~.`c _','
       .';^_,-' ~
     ,'_;-''
    ,,~
    i

''')
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0
if size == "S" or size == "s":
    total+=15
elif size == "M" or size == "m":
    total+=20
elif size == "L" or size == "l":
    total+=25
else:
    print("Please enter a valid size.")

if pepperoni == "Y":
   if size== "S":
       total+=2
   else:
       total+=3

if extra_cheese == "Y":
   total+=1



print(f"Your final bill is: ${total}.")