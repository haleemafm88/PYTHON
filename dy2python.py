a="""     Python is a high-level, general-purpose programming language known for its simple, readable syntax and versatility. Created by Guido van Rossum and first released in 1991, it supports multiple programming paradigms including procedural, object‑oriented, and functional programming.   """
print(len(a))
print('Ist letter of the paragraph=',a[0])
print('last letter of the paragraph=',a[-1])
print(a[0:50])
print(a.replace,("python","PYTHON"))
print(a.upper())
print(a.lower())
print(a.strip())
b=a.split(",")
print(b)
b="python" in a
print(b)
