# armypygame
Made this clear back when I was somewhere around *10*, just barely started programming

Seriously, take this with a grain. I was absolutely *terrible* at programming, especially python (and using some of your cousin's code for the sake of learning)! I'll probably add some levels just for kicks and giggles for you guys, **or you can add your own!**

Uses Python 2.5+ and Pygame (with whatever version works with your python rev)

Enjoy!

-Kevin
kevint@aptitekk.com

---------------------

##Layout mechanics:

You will have to completely copy a class over (Use an existing one, no I wasn't as bright to make it modular xD), and layouts must involve *all* objects

```python

self.layout=['wwwwwwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbw5',
             '0wpw0000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
             '0w0w0000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
             '0w1w0000000r00000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
             '0w0w0000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbw4',
             '00h00000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
             'ww000000w9w000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
             '9w000000w9w000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
             '9w000000www000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbw3',
             'ww000000000000a00000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
             'w0000000000000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
             'w00000wwww0000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
             '000000999w0000000000wbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
             'w00000wwww0000000000wwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
             'w0000000000000000000ewbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbww',
             'wwwwwwwwwwwwwwwwwwwwwwbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbw2',]
```
Key:

| Letter        | Object        |
| ------------- | ------------- |
| w             | wall          |
| 0             | grass         |
| p             | player  !     |
| e             | end !		    |
| 1             | pistol !      |
| 2             | rifle ! 	    |
| 3             | machine gun!  |
| 4             | flashlight!   |
| 5             | flame thrower!|
| a             | enemy (Gray)  |
| c             | superEnemy    |
| r             | ruins			|
| t             | tank			|
! Required, or other coordinates must be supplied for them in the parser on layout creation
*Note: "b" is just a commonly seen "filler" letter that just ends up being the green grass color (or default layout bg color)*


You can change these to whatever since each layout class has its own parser.
Mainly how it works is the layout (including any enemy sprites) will move around the player. Thats right, the player doesn't move at all xD

####Adding to the game
This is another place where I'm kind of kicking myself for. Its a sort of grueling process.
First add your "darkness" tag to ...options.py... for your level "darkness" (if you want the peephole "hider" until the player finds a flashlight)
Then add your level to the ...mainmenu.playlevel... def. First as a variable then down to the level counter.

