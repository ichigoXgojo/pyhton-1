n = input ("do you want to shutdown your computer? (y/n): ")
if n == "y":
    import os
    os.system("shutdown /s /t 1")

elif n == "n":
    print("shutdown aborted")