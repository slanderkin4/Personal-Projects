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
    "\n\tRound 1: Make a magic ring, and make 6 sc inside of it.\n\n\t"
    "Round 2: Inc in every stitch around (Total: 12 stitches)\n"
    )
pattern_string = (
    "\tRound {3}: (Sc in the next {0} stitches, {1})."
    " Repeat 6 times until the end of the round. (Total: {2} stitches)\n"
    )

#basic pattern
def pattern(stch, rnds, shft, cntr, strg):
    if cntr == rnds:
        print(end.format(cntr))
        return "Done"
    
    elif cntr < stch//6:
        print(strg.format(shft, "inc", 6*cntr, cntr))
        return pattern(stch, rnds, shft+1, cntr+1, strg)
        
    elif cntr == stch//6:
        print(strg.format(shft, "inc", 6*cntr, cntr))
        print("\tRound {0}-{1}: Sc around. (Total: {2} stitches)\n".format(cntr+1, (stch//3)+1, 6*cntr))
        return pattern(stch, rnds, shft, cntr+(stch//6 + 2), strg)
        
    elif cntr > (stch//3)+1:
        print(strg.format(shft, "dec", 6*(shft+1), cntr))
        return(pattern(stch, rnds, shft-1, cntr+1, strg))
