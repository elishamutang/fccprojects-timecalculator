def args_calculator(final_day, days, number_of_days):
    final = (''.join(final_day)).lower().capitalize()
    if final in days:
        final = (days.get(final) + number_of_days) % 7
        for the_day, value in days.items():
            if value == final:
                final = the_day
                return final