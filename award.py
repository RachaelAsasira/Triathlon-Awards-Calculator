def calculate_time(swimming_time, cycling_time, running_time):
    total_time = swimming_time + cycling_time + running_time
    qualifying_time = 100

    if total_time <= qualifying_time:
        print("Provincial colours: Within the qualifying time.")
    elif qualifying_time < total_time <= qualifying_time + 5:
        print("Provincial Half Colours: Within 5 minutes of qualifying time")
    elif qualifying_time + 5 < total_time <= qualifying_time + 10:
        print("Provincial Scroll: Within 10 minutes of qualifying time.")
    else:
        print("No award: More than 10 minutes beyond qualifying_time.")            


# Example usage:
swimming_time = 20
cycling_time = 40
running_time = 40

award_result = calculate_time(swimming_time, cycling_time, running_time)
print(award_result)