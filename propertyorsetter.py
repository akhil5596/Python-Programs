class employe:
    salary=5600
    salarybonus=400

    @property
    def totalsalary(self):
        return self.salary+self.salarybonus
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus=val-self.salary

a=employe()
print(a.totalsalary)
print(a.salarybonus)
a.totalsalary=5800
print(a.salarybonus)
