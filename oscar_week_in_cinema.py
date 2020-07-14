movie_name = input()
place_kind = input()
tickets = int(input())

if movie_name == 'A Star Is Born':
    if place_kind == 'normal':
        total = tickets * 7.50
    elif place_kind == 'luxury':
        total = tickets * 10.5
    elif place_kind == 'ultra luxury':
        total = tickets * 13.5
elif movie_name == 'Bohemian Rhapsody':
    if place_kind == 'normal':
        total = tickets * 7.35
    elif place_kind == 'luxury':
        total = tickets * 9.45
    elif place_kind == 'ultra luxury':
        total = tickets * 12.75
elif movie_name == 'Green Book':
    if place_kind == 'normal':
        total = tickets * 8.15
    elif place_kind == 'luxury':
        total = tickets * 10.25
    elif place_kind == 'ultra luxury':
        total = tickets * 13.25
else:
    if place_kind == 'normal':
        total = tickets * 8.75
    elif place_kind == 'luxury':
        total = tickets * 11.55
    elif place_kind == 'ultra luxury':
        total = tickets * 13.95

# Resutl
print(f'{movie_name} -> {total:.2f} lv.')


