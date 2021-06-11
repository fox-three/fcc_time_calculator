### FreeCodeCamp.org Time Calculator Project

```time_calculator.py``` contains a function ```add_time()``` that takes an initial time, adds a specified duration to the time and returns the new time and days after the initial time after the duration has passed. The function takes three arguments:

* The initial (start) time
* The duration of time that will pass
* The day of the week associated with the start time (this argument is optional)

For example:

```py
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

(*** These examples were taken from the original FCC README.md)  
