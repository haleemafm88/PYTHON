import random
import math

try:
    name =input("enter the names of guest (comma-separated):")
    name_list=[name.strip() for name in name.split(",")]
    unique= list(set(name_list))
    
    if not unique or unique == ['']:
        raise ValueError("no valid names entered")
    
    selected_name= random.choice(unique)
    reversed_names=selected_name[::-1]
    total_unique=len(unique)
    rounded_sqrt=round(math.sqrt(total_unique))
    
    print("game result:")
    print("selected names:",selected_name)
    print("reversed names:",reversed_names)
    print("total unique names:",total_unique)
    print("rounded squre:",rounded_sqrt)
    
except Exception as e:
    print("error:",e)
finally:
    print("thanks for playing the game")