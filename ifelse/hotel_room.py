month = input()
nights = int(input())

if month in 'May October'.split(' '):
    if nights <= 7:
        st_price = 50
        ap_price = 65
    elif nights > 7 and nights <= 14:
        st_price = (50 - 50 * 0.05)
        ap_price = 65
    elif nights > 14:
        st_price = (50 - 50 * 0.3)
        ap_price = (65 - 65 * 0.1)
    studio_price = st_price * nights
    aparment_price = ap_price * nights

elif month in 'June September'.split(' '):
    if nights <= 14:
        st_price = 75.2
        ap_price = 68.7
    elif nights > 14:
        st_price = (75.2 - 75.2 * 0.2)
        ap_price = (68.7 - 68.7 * 0.1)
    studio_price = st_price * nights
    aparment_price = ap_price * nights

elif month in 'July August'.split(' '):
    if nights <= 14:
        st_price = 76
        ap_price = 77
    elif nights > 14:
        st_price = 76
        ap_price = (77 - 77 * 0.1)
    studio_price = st_price * nights
    aparment_price = ap_price * nights


print(f"Apartment: {aparment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")

