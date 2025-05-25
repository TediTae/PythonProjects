print(r'''
              ___====-_       _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############\
   -###############\\    (oo)    //###############-
  -#################\\  / VV \  //#################-
 -###################\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('''
You wake up alone in the middle of a dark forest.
Your head is pounding. You're wearing a jacket,
your shoes are muddy, and you have no memory of how you got here.
In the distance, a scream echoes through the trees.
The sun is setting fast... 
''')

choice_1 = int(input('''
You have two choices:
1.) Follow the scream. Someone might need help.
2.) Go in the opposite direction.
'''))

if choice_1 == 1:
    print('''
You follow the scream, but it's a trap.
A snare tightens around your ankle — you’re left hanging upside down.
As you struggle, something with claws approaches…
YOU DIED.
    ''')
elif choice_1 == 2:
    choice_2 = int((input('''
You ignore the scream and walk silently into the woods.
Your instincts tell you something’s not right and they were correct.
Now you find shelter. Where do you rest?
1.) In an old abandoned cabin.
2.) In a hollow under a tree, covered in leaves.
    ''')))
    if choice_2 == 1:
        print('''
The cabin seems safe. 
You fall asleep. But in the middle of the night, you're not alone.
The door creaks. A shadow stands over you…
YOU DIED.
        ''')
    elif choice_2 == 2:
        choice_3 =int(input('''
You curl under the tree, hiding yourself beneath leaves.
It’s cold, but you’re hidden. You survive the night, barely.
At dawn, you hear a helicopter. What do you do?
1.) Light a fire with dry twigs and wave.
2.) Run toward the sound through the trees.
        '''))
        if choice_3 == 2:
            print('''
You sprint toward the sound, but trip into a ravine you didn’t see.
You hit your head on a rock. The helicopter flies away…
YOU DIED.
            ''')
        elif choice_3 == 1:
            print('''
You use dry twigs to make a small fire and wave a branch with your jacket on it.
The helicopter sees the smoke and circles back.
YOU SURVIVED.
            ''')
        else:
            print('''
In these woods, hesitation or confusion  can be deadly.
Choose 1 or 2, and quickly...
                  ''')


    else:
        print("You had 2 options and you choose a different one. Clever... BUT! ITS GAMEOVER")

else:
    print("Your choice should be only 1 or 2. Try again...")
