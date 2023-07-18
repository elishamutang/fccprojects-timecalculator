def add_time(start, duration, *args):

    from args_calculator import args_calculator

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

    if EM < 10:
        EM = (str(EM)).zfill(2)
    
    number_of_days = round(EH/24)
    AM_PM_switch = EH/12 #PM is even, AM is odd
    days = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}

    if "PM" in new_time: #PM time calculation
        if EH <= 12:
            if EH == 12:
                Sym = "AM"
                new_time_format = f"{EH}:{EM} {Sym}"
            elif EH < 12:
                new_time_format = f"{EH}:{EM} {Sym}"
            if args:
                final_day = args_calculator(args, days, number_of_days) #Created a function to calculate final day.
                new_time_format = f"{EH}:{EM} {Sym}, {final_day}"
        elif EH > 12 and EH < 24: 
            if EH == 12:
                Sym = "PM"
            else:
                Sym = "AM" # (next day) comment
                EH = EH % 12
                new_time_format = f"{EH}:{EM} {Sym} (next day)"
        elif EH >= 24:
            Sym = ["PM" if AM_PM_switch%2==0 else "AM"] #switching between AM and PM
            EH = EH % 12
            if EH == 0:
                EH = 12
            else:
                pass
            if args:
                final_day = args_calculator(args, days, number_of_days) #Created a function to calculate final day.
                new_time_format = f"{EH}:{EM} {Sym[0]}, {final_day} ({number_of_days} days later)"
            else:
                new_time_format = f"{EH}:{EM} {Sym[0]} ({number_of_days} days later)"

    if "AM" in new_time: #AM calculation
        if EH <= 12:
            if EH == 12:
                Sym = "PM"
                new_time_format = f"{EH}:{EM} {Sym}"
            elif EH < 12:
                new_time_format = f"{EH}:{EM} {Sym}"
        elif EH > 12 and EH < 24:
            Sym = "PM"
            EH = EH % 12
            if args:
                start_day = (''.join(args)).lower().capitalize()
                new_time_format = f"{EH}:{EM} {Sym}, {start_day}"
            else:
                new_time_format = f"{EH}:{EM} {Sym}"
        elif EH >= 24:
            EH = EH % 12
            Sym = ["PM" if AM_PM_switch%2==0 else "AM"] #switching between AM and PM
            if EH == 0:
                EH = 12
            else:
                pass
            if args:
                final_day = args_calculator(args, days, number_of_days) #Created a function to calculate final day.
                if number_of_days < 2:
                    new_time_format = f"{EH}:{EM} {Sym[0]}, {final_day} (next day)"
                else:
                    new_time_format = f"{EH}:{EM} {Sym[0]}, {final_day} ({number_of_days} days later)"
            else:
                if number_of_days < 2:
                    new_time_format = f"{EH}:{EM} {Sym[0]} (next day)"
                else:
                    new_time_format = f"{EH}:{EM} {Sym[0]}, ({number_of_days} days later)"




    return new_time_format