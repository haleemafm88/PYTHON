python={"haleema","ashik","devi","sachin"}
data_science={"inshana","nihal","ishal","devi","sachin"}
python.add("ashiha")
print(python)
data_science.remove("ishal")
print(data_science)
print(python&data_science)
print(python-data_science)
print(python|data_science)
details={
    "python":len(python),
    "data science":len(data_science)
}
print(details)
for x in details:
    print("Course: Python, Students: ",len(x))
    print("course:datascience,student:",len(x))
    break
courses={
    course:count * 2 for course,count in details.items()
}
print(courses)