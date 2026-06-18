def angle_clock(hour: int, minutes: int):
    angle_minutes = (minutes % 60) / 60
    angle_hours = ((hour + angle_minutes) / 12) % 1

    return min(abs(angle_hours - angle_minutes), 1 - abs(angle_hours - angle_minutes)) * 360


print(angle_clock(12, 30))
print(angle_clock(3, 30))
print(angle_clock(3, 15))
