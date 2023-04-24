import os
Riot_Games = ['Valorant', 'LeagueofLegends', 'TeamFightTaticts']

with open('JogosRiotGames.txt', 'w', newline='') as file:
    for line in Riot_Games:
        file.write(line + os.linesep)
