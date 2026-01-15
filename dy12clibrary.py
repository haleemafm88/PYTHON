import re

try:
    title= input("enter a book title:")
    if not re.fullmatch(r"[A-Za-z ]+", title):
        raise ValueError("Error: Book title should contain only alphabets and spaces.")
    
    year= input("enter the publication year:")
    if not re.fullmatch(r"(19|20)\d{2}",year):
        raise ValueError("error:publication year must be 4-digit number starting woth 19 or 20.")
    
    print("book details accepted successfully")
    print("title:",title)
    print("year:",year)
    
except ValueError as e:
    print(e)
    
except Exception:
    print("An unexpected error occurred.")

finally:
    print("\nThank you for using the mini library system.")
    
    