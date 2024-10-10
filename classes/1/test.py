def main():
    ui = input("What time is it? ")
    time = convert(ui)
    print(time)
    if 7.0<= time <=8:
        print("breakfast time")
    elif 12<= time <=13:
        print("lunch time")
    if 18<= time <=19:
        print("dinner time")


def convert(time):
    t = list(map(int, time.split(":")))
    minute = t[1]/60
    return t[0]+minute

main()