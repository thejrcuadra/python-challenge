import os

def main():
    CSV_PATH = os.path.join('Resources', 'election_data.csv')

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open(CSV_PATH) as csvfile:
        file = csvfile.readlines()

    totalVotes = getTotalVotes(file)
    candidates, charlesVotes, dianaVotes, raymonVotes = getStats(file)

    charlesPercentage = charlesVotes / totalVotes * 100
    dianaPercentage = dianaVotes / totalVotes * 100
    raymonPercentage = raymonVotes / totalVotes * 100

    with open("election_results.txt", "w") as textFile:
        textFile.write(f"Election Results\n\n")
        textFile.write(f"---------------------------\n\n")
        textFile.write(f"Total Votes: {totalVotes}\n\n")
        textFile.write(f"---------------------------\n\n")
        textFile.write(f"{candidates[0]}: {round(charlesPercentage, 3)}% ({charlesVotes})\n\n")
        textFile.write(f"{candidates[1]}: {round(dianaPercentage, 3)}% ({dianaVotes})\n\n")
        textFile.write(f"{candidates[2]}: {round(raymonPercentage, 3)}% ({raymonVotes})\n\n")
        textFile.write(f"---------------------------\n\n")
        textFile.write(f"Winner: {candidates[1]}")
        print("Election Results have been saved to 'election_results.txt'.")

def getTotalVotes(file):
    totalVotes = 0  
    for x in file:
        totalVotes += 1
    totalVotes = totalVotes - 1
    return totalVotes

def getStats(file):
    index = 1
    candidatry = []
    charlesVotes = 0
    dianaVotes = 0
    raymonVotes = 0
    for x in file:
        while index < 369712:
            skipHeader = file[index]
            if skipHeader[8] == 'J':
                candidateName = skipHeader[18:]
                if candidateName not in candidatry:
                    candidatry.append(candidateName)
                if candidateName[0] == 'C':
                    charlesVotes += 1
                elif candidateName[0] == 'D':
                    dianaVotes += 1
                elif candidateName[0] == 'R':
                    raymonVotes += 1
            elif skipHeader[8] == 'D':
                candidateName = skipHeader[15:]
                if candidateName not in candidatry:
                    candidatry.append(candidateName)
                if candidateName[0] == 'C':
                        charlesVotes += 1
                elif candidateName[0] == 'D':
                        dianaVotes += 1
                elif candidateName[0] == 'R':
                        raymonVotes += 1
                    
            elif skipHeader[8] == 'A':
                candidateName = skipHeader[17:]
                if candidateName not in candidatry:
                    candidatry.append(candidateName)
                if candidateName[0] == 'C':
                    charlesVotes += 1
                elif candidateName[0] == 'D':
                    dianaVotes += 1
                elif candidateName[0] == 'R':
                    raymonVotes += 1
            index += 1

    candidates = []
    for x in candidatry:
        candidates.append(x.rstrip("\n"))
    return candidates, charlesVotes, dianaVotes, raymonVotes
                
main()