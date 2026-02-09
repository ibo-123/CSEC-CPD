for i in range(int(input())):
        time = input().strip()
        if time[:2] == "00":
                print(f"12:{time[3:5]} AM")
                continue
        elif time < "12:00":
                print(f"{time} AM")
        else:
                hh = "0" + str(int(time[:2]) - 12) if time[:2] != "12" else str(12)
                if len(hh) >= 3:
                        hh = hh[1:]
                print(f"{hh}:{time[3:5]} PM")