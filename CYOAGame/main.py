print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

print('You are walking along the road and come across a split in the path. There is a sign pointing to the right saying "Shortcut to lake. Watch out for bandits!"')
path = input('Do you go left or right? ')
if path.lower() == "right":
    print(
        """     
              ;     \
              `;   __`\
               ;,-',_`,\
                ;|/`)  \
                 \/'_)/ |
                  \/( | :
             ,---=='='=`===----.
             `---==|  ;  \==---'
                   |  ;.  \
                   |  `;   \
                   |   ;.   \
                   |   `;    \
                   |    ;.    \
                   |    `;     \   
                   |     ;.     \
                   |     `;      \
                   `--..._ `  _.-'
                          `--'
          """)
    print("Shortly after taking the right path you come across a group of bandits. They quickly rob you of all you have. In your rush to reach the treasure faster you have been forced to quit your journey.")
    print("GAME OVER")

else:
    print("After walking several miles you come to a large lake. In the middle of the lake is a large island. You could wait for a boat or attempt to swim across.")

lake = input("Do you wait or swim? ")
if lake.lower() == "swim":
    print('''
                    ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\
        ''')
    print("You attempt to swim across the lake. Unfortunatly the waters are infested with bloodthirsty sharks. You are quickly eaten by a group of them. Your impatience has cost you your life.")
    print("GAME OVER")
    exit()
else:
    print("After waiting only a few minutes, a boat offering passage to the island arrives on the shore.")
    print("Once reaching the island you come across a room with three doors. The doors are colored red, yellow, and blue.")

door = input("Which door do you go through? red, yellow or blue? ")
if door.lower() == "red":
    print('''
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        ''')
    print("Oh no! You fall into a pit of fire!")
    print("GAME OVER")
    exit()
elif door.lower() == "yellow":
    print('''
                        ,.
                    ,_> `.   ,';
                ,-`'      `'   '`'._
             ,,-) ---._   |   .---''`-),.
           ,'      `.  \  ;  /   _,'     `,
        ,--' ____       \   '  ,'    ___  `-,
       _>   /--. `-.              .-'.--\   \__
      '-,  (    `.  `.,`~ \~'-. ,' ,'    )    _\
      _>    \     \ ,'  ') )   `. /     /    <,.
   ,-'   _,  \    ,'    ( /      `.    /        `-,
   `-.,-'     `.,'       `         `.,'  `\    ,-'
    ,'       _  /   ,,,      ,,,     \     `-. `-._
   /-,     ,'  ;   ' _ \    / _ `     ; `.     `(`-\
    /-,        ;    (o)      (o)      ;          `'`,
  ,~-'  ,-'    \     '        `      /     \      <_
  /-. ,'        \                   /       \     ,-'
    '`,     ,'   `-/             \-' `.      `-. <
     /_    /      /   (_     _)   \    \          `,
       `-._;  ,' |  .::.`-.-' :..  |       `-.    _\
         _/       \  `:: ,^. :.:' / `.        \,-'
       '`.   ,-'  /`-..-'-.-`-..-'\            `-.
         >_ /     ;  (\/( ' )\/)  ;     `-.    _<
         ,-'      `.  \`-^^^-'/  ,'        \ _<
          `-,  ,'   `. `"""""' ,'   `-.   <`'
            ')        `._.,,_.'        \ ,-'
             '._        '`'`'   \       <
                >   ,'       ,   `-.   <`'
                 `,/          \      ,-`
                  `,   ,' |   /     /
                   '; /   ;        (
                    _)|   `       (
                    `')         .-'
                      <_   \   /    
                        \   /\(
                         `;/  `

        ''')
    print("Behind the door is a very hungry lion! You were a great snack!")
    print("GAME OVER")
    exit()
else:
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
        ''')
    print("Behind the door you find a huge treasure room! You now have more riches than you know what to do with!")
    print("Congratulations! You Win!")

