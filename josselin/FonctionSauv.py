def sauv(score):
    fichierScore = open('fichierScore.txt', 'r')
    tableScore = [fichierScore.readline(), fichierScore.readline(), fichierScore.readline(), fichierScore.readline(), fichierScore.readline()]
    for line in range(len(tableScore)):
        tableScore[line] = tableScore[line][0:-1]
    fichierScore.close()
    if score > int(tableScore[4]):
        fichierScore, rang, newScore = open('fichierScore.txt', 'w'), 0, [0, 0, 0, 0, 0]
        for line in range(0, len(tableScore)):
            if score > int(tableScore[line]) and line == rang:
                fichierScore.write(str(score))
                fichierScore.write('\n')
                newScore[line] = score
            else:
                fichierScore.write(tableScore[rang])
                fichierScore.write('\n')
                newScore[line] = str(tableScore[rang])
                rang += 1
        fichierScore.close()
        return newScore
    return tableScore

var, lastBestScore = True, 0

while var:
    score = int(input('Score = '))
    print(sauv(score))
    if score > lastBestScore:
        print('Best Score !')
        lastBestScore = score