import json
from difflib import get_close_matches

data = json.load( open("colours.json") )

def translate( colour ):
    colour = colour.lower()
    if colour in data:
        return data[colour]
    elif len( get_close_matches(colour, data.keys()) ) > 0:
        yn = input( "Did you mean %s instead? Type y if yes, or n if no: " % get_close_matches(colour, data.keys())[0] )
        if yn == 'y' or yn == 'Y':
            return data[ get_close_matches(colour, data.keys())[0] ]
        elif yn == 'n' or yn == 'N':
            return("Can't find colour. Please, double check it!")
        else:
            return("We didn't understand your input.")
    else:
        return("Can't find colour. Please, double check it!")

colour = input("Enter a colour: ")
output = translate(colour)
if type(output) == list:
    for item in output:
        print( item )
else:
    print( output )
