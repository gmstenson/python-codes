"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input("\nPlease enter your age: "))

max_heart_rate_per_minute = 220 - age

min_rate = max_heart_rate_per_minute * 0.65
max_rate = max_heart_rate_per_minute * 0.85

print(f"When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {min_rate:.0f} and {max_rate:.0f} beats per minute.")