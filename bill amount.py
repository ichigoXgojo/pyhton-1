def total_cald(bill_amount, tip_prec=10):
    total = bill_amount * (1 + 0.01 * tip_prec)
    total = round(total, 2)
    print(f"please pay ${total}")


total_cald(100, 15)
total_cald(200)