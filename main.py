salary=input("Enter Salary: ")
staffSalary=input("Enter Staff Salary: ")
staff=input("Enter Staff: ")

salary=float(salary)
staffSalary=float(staffSalary)
staff=float(staff)

staffPercentage=(salary/staffSalary)/100
newSalary=salary+staffPercentage+staff

print("staffPercentage:" + str(staffPercentage))
print("newSalary:" + str(newSalary))