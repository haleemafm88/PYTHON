items=["milk","bread","eggs"]
def add_item(items):
    new_item=items.append("butter")
    return(items)
print(add_item(items))

def remove_last_item(items):
    del_item=items.pop()
    return(items)
print(remove_last_item(items))

display_item = lambda item: print(f"Item: {item}")
display_item(items)

def recurse(items):
   if not items:  
      return 0
   return len(items[0]) + recurse(items[1:])


print("Total characters:",recurse(items))
