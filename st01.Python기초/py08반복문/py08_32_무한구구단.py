
str = "abc"

while True:
    
    try:
        a = int( str ) # ValueError
    except ValueError :
        break