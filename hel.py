import Employee
lstemp=[]
while True:
    print("====Employee Menu====")
    print("1.Add")
    print("2.Display")
    print("3.search")
    print("4.Delete")
    print("5.Update")
    print("6.Exit")

    choice=int(input("Enter Your Choice:"))

    if choice==1:
        emp=Employee.Emp()
        emp.getData()
        found=False
        for e in lstemp:
            if e.eid==emp.eid:
                found=True
                break
        if found:
            print("Employee ID already exists!!")
        else:
            emp.calSalary()
            lstemp.append(emp)
            print("Employee added successfully")

    elif choice==4:
        if len(lstemp)==0:
            print("No employee data available!!")
        else:
            for emp in lstemp:
                emp.putData()

    elif choice==5:
        key=input("Enter Employee ID:")
        found=False
        for emp in lstemp:
            if str(emp.eid)==key or emp.enm.lower()==key.lower():
                emp.putData()
                founf=True
        if not found:
            print("Employee mot found!!")