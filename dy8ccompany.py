class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show_details(self):
        print(self.name,self.age)
        
class employee(person):
    def __init__(self,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
    
    def show_details(self):
        print()
        
        
    
        