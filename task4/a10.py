def print_formatted(number):
    width = len(format(number, 'b'))
    
    for i in range(1, number + 1, 1):
        dec = str(i).rjust(width,' ')
        oct = format(i, "o").rjust(width, ' ')
        hex = format(i, "X").rjust(width, ' ')
        bin = format(i, 'b').rjust(width, ' ')
        
        print(f"{dec} {oct} {hex} {bin}")