import random
import math

names_input = input("Enter customer names (comma-separated): ")
names_list = names_input.split(",")
unique_names = list(set(name.strip() for name in names_list))
random.shuffle(unique_names)
winners = random.sample(unique_names, 2)
winner1 = winners[0][::-1]
winner2 = winners[1][::-1]
print("Winner 1 (reversed):", winner1)
print("Winner 2 (reversed):", winner2)
total_participants = len(unique_names)
print("Total unique participants:", total_participants)
sqrt_value = round(math.sqrt(total_participants))
print("Rounded square root of participants:", sqrt_value)
