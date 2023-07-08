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

    if EH >= 24: #Check if end time is more than 24 hrs, if True, then more than one day.
        print("Next day mate")
        num_of_days = round(EH/24)
        print(num_of_days)
        if "PM" in new_time:
            if EH > 12:
                Sym = "AM"
                EH -= 12
                if EH == 12:
                    Sym = "PM"
                if EM < 10:
                    EM = (str(EM)).zfill(2)
                else:
                    pass
                print(f"{EH}:{EM} {Sym}")
        #elif "AM" in new_time:











    return new_time