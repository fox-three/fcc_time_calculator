def add_time(start, duration, day=None):

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    lower_days = [day.lower() for day in days]

    def cycle(arr, start, iters, return_cycle_count=False):
        current_idx = arr.index(start)
        count = 0
        cycle_count = 0
        while count < iters:
            count += 1
            try:
                current_idx += 1
                current_idx = arr.index(arr[current_idx])
            except:
                current_idx = 0
                cycle_count += 1
        if return_cycle_count:
            return arr[current_idx], cycle_count
        else:
            return arr[current_idx]

    # Check start, duration and days for errors and declare vars
    start_time, start_hours, start_minutes, start_ampm, start_day = "","","","",""
    try:
        start_time, start_ampm = start.split()[0], start.split()[-1]
        start_hours, start_minutes = int(start_time.split(":")[0]), int(start_time.split(":")[-1])
        if start_hours not in [i for i in range(1, 13)]:
            raise BaseException
        elif start_minutes not in [i for i in range(60)]:
            raise BaseException
    except:
        return "Error: Check start time."

    duration_hours, duration_minutes = 0,0
    try:
        duration_hours, duration_minutes = int(duration.split(":")[0]), int(duration.split(":")[-1])
    except:
        return "Error: Check duration time."
    if day:
        try:
            if day.lower() not in [day.lower() for day in days]:
                raise BaseException
            start_day = day
        except:
            return "Error: Check day."

    # Convert start time to 24-hr
    if start_ampm == "PM":
        if start_hours != 12: start_hours = start_hours + 12

    # Define and calculate new time vars
    new_time, new_hours, new_minutes, new_ampm, new_day = "","","","",""
    idx_new_minutes, add_hours = cycle([i for i in range(60)], start_minutes, duration_minutes, True)
    duration_hours += add_hours
    minutes = [f"0{i}" for i in range(10)]+[f"{i}" for i in range(10,60)]
    new_minutes = minutes[idx_new_minutes]
    idx_new_hours, add_days = cycle([i for i in range(24)], start_hours, duration_hours, True)
    if idx_new_hours > 12:
        idx_new_hours = idx_new_hours - 12
        new_ampm = "PM"
    elif idx_new_hours == 12:
        new_ampm = "PM"
    else:
        new_ampm = "AM"
        if idx_new_hours == 0: idx_new_hours = 12
    new_hours = [f"{i}" for i in range(13)][idx_new_hours]

    day_count = 0 + add_days

    # return new_time
    if day:
        new_day = days[lower_days.index(cycle(lower_days, day.lower(), day_count))]
        if day_count < 1:
            new_time = f"{new_hours}:{new_minutes} {new_ampm}, {new_day}"
        elif day_count == 1:
            new_time = f"{new_hours}:{new_minutes} {new_ampm}, {new_day} (next day)"
        else:
            new_time = f"{new_hours}:{new_minutes} {new_ampm}, {new_day} ({day_count} days later)"
    else:
        if day_count < 1:
            new_time = f"{new_hours}:{new_minutes} {new_ampm}"
        elif day_count == 1:
            new_time = f"{new_hours}:{new_minutes} {new_ampm} (next day)"
        else:
            new_time = f"{new_hours}:{new_minutes} {new_ampm} ({day_count} days later)"

    return new_time
