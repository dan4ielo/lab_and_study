#Escape sequence caracters: Practice

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "i'm \\ a \\ cat"

fat_cat = """
I'll do a grocery list here:
\t* Cat food;
\t* Fishies;
\t* Cantip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

#Escape sequences - What do they do?
#\\	Backslash (\)
#\'	Single-quote (')
#\"	Double-quote (")
#\a	ASCII bell (BEL)
#\b	ASCII backspace (BS)
#\f	ASCII formfeed (FF)
#\n	ASCII linefeed (LF)
#\N{name}	Character named name in the Unicode database (Unicode only)
#\r	ASCII carriage return (CR)
#\t	ASCII horizontal tab (TAB)
#\uxxxx	Character with 16-bit hex value xxxx (Unicode only)
#\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
#\v	ASCII vertical tab (VT)
#\000	Character with octal value 00
#\xhh	Character with hex value hh

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print ("%s\r" % i,)
#        if i=="|": break
