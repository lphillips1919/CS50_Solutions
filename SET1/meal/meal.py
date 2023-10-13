def main():
    time = input("What time is it? ").strip()
    if convert(time) >= 7.0 and convert(time) <= 8.0:
        print("Breakfast time")
    elif convert(time) >= 12.0 and convert(time) <= 13.0:
        print("Lunch time")
    elif convert(time) >= 18.0 and convert(time) <= 19.0:
        print("Dinner time")
    else:
        return
    

def convert(time):
    x, y = time.split(":")
    hrs = float(x)
    mins = float(y) * 1 / 60
    return(hrs+mins)
    
if __name__ == "__main__":
    main()