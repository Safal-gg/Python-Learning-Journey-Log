class GetEmployee:
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary

    def give_raise(self,bonus=5000):
        self.salary += bonus
        return self.salary

info=GetEmployee('safal','shrestha',5000)
salary=info.give_raise(1000)
print(salary)