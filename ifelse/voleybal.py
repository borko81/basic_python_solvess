import math
year = input()          # leap or normal
holideys = int(input()) # wihtout whikend
go_home = int(input())

free_weekend = 48 - go_home
play_in_sofia = free_weekend * 0.75
holideys_play = holideys * (2 / 3)
play_in_town = go_home

total_play = play_in_sofia + holideys_play + play_in_town

if year == 'leap':
    total_play *= 1.15

print(math.floor(total_play))