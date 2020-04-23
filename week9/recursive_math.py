# TOWER OF HANOI
def moveDiscs(pegs, startPeg, endPeg, tmpPeg, numDiscs):
    # If you have only one disc, just move it!
    if numDiscs == 1:
        assert(len(pegs[endPeg]) == 0 or pegs[startPeg][0] < pegs[endPeg][0])
        disc = pegs[startPeg].pop(0)
        print("Moving", disc, "from", startPeg, "to", endPeg)
        pegs[endPeg].insert(0, disc)
        return 1
    else:
        numMoves = 0
        # If you want to move N discs, move the top N-1 discs to the tmp peg
        numMoves += moveDiscs(pegs, startPeg, tmpPeg, endPeg, numDiscs - 1)
        # Then move the bottom disc to the end peg
        numMoves += moveDiscs(pegs, startPeg, endPeg, tmpPeg, 1)
        # Then move the N-1 discs from the tmp to the end peg
        numMoves += moveDiscs(pegs, tmpPeg, endPeg, startPeg, numDiscs - 1)
        return numMoves

# A wrapper function that sets up the other parameters based on pegs
def towersOfHanoi(pegs):
    return moveDiscs(pegs, "left", "right", "middle", len(pegs["left"]))

pegs = { "left" : [1, 2, 3], "middle" : [], "right" : [] }
print("Number of discs moved:", towersOfHanoi(pegs))
print("End peg state:", pegs)

