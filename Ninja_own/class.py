class Employee:
     name=""
     age=""
     sal=""
     def get_emp(self):
         return self.name,self.age,self.sal
anudeep=Employee()
anudeep.name="Anudeep"
anudeep.age=23
anudeep.sal=20000
print anudeep.get_emp()
