'''
author: Siena Landerkin
version: 1.0.1  September 2024
'''

#variables
end = (
    "\t\t  Stuff your ball. It can be as stuffed fully or lightly depending on your preference."
    "\n\n\tRound {0}: Dec around (Total: 6 stitches)\n\n\tTo Finish: Stitch hole closed, fasten off and hide ends.\n"
    )
beginning = (
    "\n\tRound 1: Make a magic ring, and make 6 sc inside of it.\n\n"
    "\tRound 2: Inc in every stitch around (Total: 12 stitches)\n\n"
    "\tRound 3: Sc in 1 stitch, inc in the next around (Total: 18 stitches)\n"
    )
odd_round = (
    "\tRound {3}: [{0} sc, {1}] six times. (Total: {2} stitches)\n"
    )
even_round = (
    "\tRound {3}: {4} sc, {1}, [{0} sc, {1}] five times, {4} sc. (Total: {2} stitches)\n"
    )

#shifting pattern
def pattern(stch, rnds, shft, cntr, even, odd):
    if cntr == rnds:
        print(end.format(cntr))
        return "Done"
    
    elif cntr < stch//6:
        if cntr % 2 == 0:
            print(even.format(shft, "inc", 6*cntr, cntr, shft//2))
        else:
            print(odd.format(shft, "inc", 6*cntr, cntr))
        return pattern(stch, rnds, shft+1, cntr+1, even, odd)
        
    elif cntr == stch//6:
        if cntr % 2 == 0:
            print(even.format(shft, "inc", 6*cntr, cntr, shft//2))
        else:
            print(odd.format(shft, "inc", 6*cntr, cntr))
        print("\tRound {0}-{1}: Sc around. (Total: {2} stitches)\n".format(cntr+1, (stch//3)+1, 6*cntr))
        return pattern(stch, rnds, shft, cntr+(stch//6 + 2), even, odd)
        
    elif cntr > (stch//3)+1:
        if (stch//6) % 2 == 0:
            if cntr % 2 == 0:
                print(even.format(shft, "dec", 6*(shft+1), cntr, shft//2))
            else:
                print(odd.format(shft, "dec", 6*(shft+1), cntr))
        else:
            if cntr % 2 == 0:
                print(odd.format(shft, "dec", 6*(shft+1), cntr))
            else:
                print(even.format(shft, "dec", 6*(shft+1), cntr, shft//2))
        return(pattern(stch, rnds, shft-1, cntr+1, even, odd))
        
        