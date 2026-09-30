def number_lo():
    try:
        number = int(input("Koi number likho: "))
        print("Aapne likha:", number)
    except ValueError:
        print("Ye number nahi hai! Sirf numbers likho, jaise 5 ya 10.")

number_lo()