def add_time(start, duration, *args):

    [T, Sym] = start.split(" ")
    [SH, SM] = T.split(":")
    [DH, DM] = duration.split(":")

    hour_time = str(int(SH) + int(DH)) + ":" #Hours
    min_time = int(SM) + int(DM) #Minute

    if min_time < 10:
        min_time = (str(min_time)).zfill(2) #If minute less than 10, fill in leading zeros
    else:
        min_time = str(min_time)

    new_time = hour_time + min_time + f" {Sym}" #New time after start + duration

    [T, Sym] = new_time.split(" ")
    [EH, EM] = T.split(":")
    EH, EM = int(EH), int(EM)

    if EM >= 60:
        EH += round(EM/60)
        EM -= 60

    #print(f"{EH}:{EM} {Sym}")

    number_of_days = round(EH/24)
    print(f"{EH/24} days")

    if EM < 10:
        EM = (str(EM)).zfill(2)
    

    if "PM" in new_time:
        if EH > 12 and EH < 24: # (next day) comment
            if EH == 12:
                Sym = "PM"
            else:
                pass
            Sym = "AM"
            EH = EH % 12
            new_time_format = f"{EH}:{EM} {Sym} (next day)" #Make this new_time
            print(new_time_format)
        elif EH >= 24:
            AM_PM_switch = EH/12
            Sym = ["PM" if AM_PM_switch%2==0 else "AM"] #switching between AM and PM
            EH = EH % 12
            new_time_format = f"{EH}:{EM} {Sym[0]} ({number_of_days} days later)"
            print(new_time_format)

    if "AM" in new_time:
        if EH <= 12:
            if EH == 12:
                Sym = "PM"
                new_time_format = f"{EH}:{EM} {Sym}"
                print(new_time_format)
            else:
                pass
        elif EH > 12 and EH < 24:
            Sym = "PM"
            EH = EH % 12
            new_time_format = f"{EH}:{EM} {Sym} (next day)"
            print(new_time_format)
        elif EH >= 24:
            EH = EH % 12
            new_time_format = f"{EH}:{EM} {Sym} ({number_of_days}) days later"
            print(new_time_format)

            











    return new_time