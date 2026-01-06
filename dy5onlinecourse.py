frontend={"haleema","inshana","devi","ashika","ashik"}
backend={"ashik","nihal","sachin","ishal","devi"}
backend.add("fathima")
print(backend)
frontend.remove("ashika")
print(frontend)
print(frontend&backend)
print(backend-frontend)
print("unique student:",len(frontend|backend))
course={
    "frontend":len(frontend),
    "backend":len(backend)
}
