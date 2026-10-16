class Emp:
    def __init__(self,eid=0,enm="",bs=0):
        self.eid=eid
        self.enm=enm
        self.bs=bs
        self.hra=0
        self.da=0
        self.pf=0
        self.ns=0
    def getData(self):
        self.eid=int(input("Enter Employee ID:"))
        self.enm=input("Enter Employee Name:")
        self.bs=int(input("Enter Employee basic Salary:"))
    def calSalary(self):
        if self.bs<5000:
            self.hra=self.bs*0.10
            self.da=self.bs*0.20
            self.pf=self.bs*0.05
        elif self.bs<10000:
            self.hra=self.bs*0.20
            self.da=self.bs*0.40
            self.pf=self.bs*0.10
        else:
            self.hra=self.bs*0.30
            self.da=self.bs*0.60
            self.pf=self.bs*0.15
    def putData(self):
        print("Employee ID           :",self.eid)
        print("Employee Name         :",self.enm)
        print("Employee basic Salary :",self.bs)
        print("HRA                   :",self.hra)
        print("DA                    :",self.da)
        print("PF                    :",self.pf)
        print("Net Salary            :",self.ns)
        print('------------------------------------------')
    