"""timeconvert"""
def convert_to_24_hour_format(time: str) -> str:
    """converty"""
    try:
        time_part, period = time[:-2], time[-2:]
        hours, minutes = map(int, time_part.split(':'))
        if period not in ['AM', 'PM'] or not 1 <= hours <= 12 or not 0 <= minutes < 60:
            return "ERROR"
        if period == 'PM' and hours != 12:
            hours += 12
        elif period == 'AM' and hours == 12:
            hours = 0
        return f"{hours:02}:{minutes:02}"
    except ValueError:
        return "ERROR"

time_input = input()

print(convert_to_24_hour_format(time_input))
