from tkinter import *


class EmployeeeSystem:
    employee_list = []
    all_employee_Frame = None

    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll System")
        self.root.config(bg="white")
        title = Label(self.root, text="Employee Payroll Management System", font=("times new roman", 30, "bold"),
                      bg="#296d98", fg="white", padx=10).place(x=0, y=0, relwidth=1)
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contract = StringVar()
        self.var_mob = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_department = StringVar()

        Frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=60, width=600, height=430)
        title1 = Label(Frame1, text="Employee Details", font=("times new roman", 30, "bold"),
                       bg="#3792cb", fg="white", padx=10).place(x=0, y=0, relwidth=1)

        lbl_name = Label(Frame1, text="Employee Name ", font=("times new roman", 20),
                         bg="white", fg="blue", padx=10).place(x=0, y=60)
        txt_name = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_name,
                         fg="red").place(x=220, y=65)
        lbl_age = Label(Frame1, text="Employee Age ", font=("times new roman", 20),
                        bg="white", fg="blue", padx=10).place(x=0, y=95)
        txt_age = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_age,
                        fg="red").place(x=220, y=100)
        lbl_gender = Label(Frame1, text="Employee Gender ", font=("times new roman", 20),
                           bg="white", fg="blue", padx=10).place(x=0, y=130)
        txt_gender = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_gender,
                           fg="red").place(x=220, y=135)
        lbl_dob = Label(Frame1, text="Employee D.O.B ", font=("times new roman", 20),
                        bg="white", fg="blue", padx=10).place(x=0, y=165)
        txt_dob = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_dob,
                        fg="red").place(x=220, y=170)
        lbl_contract = Label(Frame1, text="Employee Ctr No ", font=("times new roman", 20),
                             bg="white", fg="blue", padx=10).place(x=0, y=200)
        txt_contract = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_contract,
                             fg="red").place(x=220, y=205)
        lbl_mob = Label(Frame1, text="Employee Mob Nr ", font=("times new roman", 20),
                        bg="white", fg="blue", padx=10).place(x=0, y=235)
        txt_mob = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_mob,
                        fg="red").place(x=220, y=240)
        lbl_email = Label(Frame1, text="Employee Email ", font=("times new roman", 20),
                          bg="white", fg="blue", padx=10).place(x=0, y=270)
        txt_email = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_email,
                          fg="red").place(x=220, y=275)
        lbl_address = Label(Frame1, text="Employee Address ", font=("times new roman", 20),
                            bg="white", fg="blue", padx=10).place(x=0, y=305)
        txt_address = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_address,
                            fg="red").place(x=220, y=310)
        lbl_department = Label(Frame1, text="Employee Depart ", font=("times new roman", 20),
                               bg="white", fg="blue", padx=10).place(x=0, y=335)
        txt_department = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_department,
                               fg="red").place(x=220, y=340)
        btn_add = Button(Frame1, text="Add Employee", font=("times new roman", 15), bg="white",
                         command=self.add_employee,
                         fg="black").place(x=50, y=375)
        btn_remove = Button(Frame1, text="Remove Employee", font=("times new roman", 15), bg="white",
                            fg="black").place(x=220, y=375)
        btn_see = Button(Frame1, text="See Employees", command=self.see_employee, font=("times new roman", 15),
                         bg="white",
                         fg="black").place(x=446, y=375)
        self.all_employee_Frame = Listbox(Frame1, bg="white", bd=2, relief=RIDGE)
        self.all_employee_Frame.place(x=440, y=90, width=150, height=280)
        title_all = Label(Frame1, text=" All Employees", font=("times new roman", 10, "bold"),
                          bg="#3792cb", fg="white", padx=10).place(x=440, y=60, width=150, height=30)
        scroll = Scrollbar(self.all_employee_Frame, orient=VERTICAL)
        scroll.pack(fill=Y, side=RIGHT)

        self.var_year = StringVar()
        self.var_month = StringVar()
        self.var_days = StringVar()
        self.var_hours = StringVar()
        self.var_salary = StringVar()
        self.var_tax = StringVar()
        self.var_nino = StringVar()
        self.var_pension = StringVar()
        self.var_netsalary = StringVar()

        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame2.place(x=620, y=60, width=600, height=430)
        title1 = Label(Frame2, text="Employee Payslip", font=("times new roman", 30, "bold"),
                       bg="#3792cb", fg="white", padx=10).place(x=0, y=0, relwidth=1)
        lbl_year = Label(Frame2, text="Year", font=("times new roman", 20),
                         bg="white", fg="blue", padx=10).place(x=0, y=60)
        txt_year = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_year,
                         fg="red").place(x=100, y=65)
        lbl_month = Label(Frame2, text="Month", font=("times new roman", 20),
                          bg="white", fg="blue", padx=10).place(x=0, y=95)
        txt_month = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_month,
                          fg="red").place(x=100, y=100)
        lbl_days = Label(Frame2, text="Days", font=("times new roman", 20),
                         bg="white", fg="blue", padx=10).place(x=0, y=130)
        txt_days = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_days,
                         fg="red").place(x=100, y=135)
        lbl_hours = Label(Frame2, text="H/Day", font=("times new roman", 20),
                          bg="white", fg="blue", padx=10).place(x=0, y=165)
        txt_hours = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_hours,
                          fg="red").place(x=100, y=170)
        lbl_salary = Label(Frame2, text="Salary", font=("times new roman", 20),
                           bg="white", fg="blue", padx=10).place(x=0, y=200)
        txt_salary = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_salary,
                           fg="red").place(x=100, y=205)
        lbl_tax = Label(Frame2, text="TAX", font=("times new roman", 20),
                        bg="white", fg="blue", padx=10).place(x=0, y=235)
        txt_tax = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_tax,
                        fg="red").place(x=100, y=240)
        lbl_nino = Label(Frame2, text="N.I.N.O", font=("times new roman", 20),
                         bg="white", fg="blue", padx=10).place(x=0, y=270)
        txt_nino = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_nino,
                         fg="red").place(x=100, y=275)
        lbl_pension = Label(Frame2, text="Pension", font=("times new roman", 20),
                            bg="white", fg="blue", padx=10).place(x=0, y=310)
        txt_pension = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_pension,
                            fg="red").place(x=100, y=315)
        lbl_netsalary = Label(Frame2, text="Net Slr", font=("times new roman", 20),
                              bg="white", fg="blue", padx=10).place(x=0, y=345)
        txt_netsalary = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_netsalary,
                              fg="red").place(x=100, y=350)
        btn_calculate = Button(Frame2, text="Calculate", command=self.calculate, font=("times new roman", 15),
                               bg="white",
                               fg="black").place(x=100, y=380, height=30, width=100)
        btn_clear = Button(Frame2, text="Clear", command=self.clear_inputs, font=("times new roman", 15), bg="white",
                           fg="black").place(x=205, y=380, height=30, width=100)
        btn_print = Button(Frame2, text="Print", font=("times new roman", 15), bg="white",
                           fg="black").place(x=320, y=380, height=30, width=270)
        print_employee_Frame = Frame(Frame2, bg="white", bd=2, relief=RIDGE)
        print_employee_Frame.place(x=320, y=90, width=270, height=280)
        title_print = Label(Frame2, text=" Print Payslip", font=("times new roman", 10, "bold"),
                            bg="#3792cb", fg="white", padx=10).place(x=320, y=60, width=270, height=30)
        scroll = Scrollbar(print_employee_Frame, orient=VERTICAL)
        scroll.pack(fill=Y, side=RIGHT)

    def see_employee(self):
        print(self.var_name.get(),
              self.var_age.get(),
              self.var_gender.get(),
              self.var_dob.get(),
              self.var_contract.get(),
              self.var_mob.get(),
              self.var_email.get(),
              self.var_address.get(),
              self.var_department.get())

    def calculate(self):
        self.var_year.get(),
        self.var_month.get(),
        self.var_days.get(),
        self.var_hours.get(),
        self.var_salary.get(),
        self.var_tax.get(),
        self.var_nino.get(),
        self.var_pension.get(),
        self.var_netsalary.get()
        salary = int(self.var_days.get()) * int(self.var_hours.get())
        self.var_salary.set(salary)
        print(salary)
        net_salary = float(salary) - float(self.var_tax.get()) - float(self.var_nino.get()) - float(
            self.var_pension.get())
        self.var_netsalary.set(net_salary)
        print(net_salary)

    def clear_inputs(self):
        self.var_name.set(""),
        self.var_age.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_contract.set(""),
        self.var_mob.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_department.set("")
        self.var_year.set(""),
        self.var_month.set(""),
        self.var_days.set(""),
        self.var_hours.set(""),
        self.var_salary.set(""),
        self.var_tax.set(""),
        self.var_nino.set(""),
        self.var_pension.set(""),
        self.var_netsalary.set("")

    def add_employee(self):

        employee = Employee(
            self.var_name.get(),
            self.var_age.get(),
            self.var_gender.get(),
            self.var_dob.get(),
            self.var_contract.get(),
            self.var_mob.get(),
            self.var_email.get(),
            self.var_address.get(),
            self.var_department.get()
        )

        self.employee_list.append(employee)
        self.clear_inputs()
        for idx, empl in enumerate(self.employee_list):
            index = self.all_employee_Frame.size()

            if len(self.employee_list) != 0 and idx >= index:
                self.all_employee_Frame.insert(idx, empl)
        print(self.employee_list)


class Employee:
    count = 0

    def __repr__(self):
        visible_text = f"{self.value_name}"
        return visible_text

    def __init__(self, value_name, value_age, value_gender, value_dob, value_contract, value_mob, value_email,
                 value_address, value_department, ):
        self.value_name = value_name
        self.value_age = value_age
        self.value_gender = value_gender
        self.value_dob = value_dob
        self.value_contract = value_contract
        self.value_mob = value_mob
        self.value_email = value_email
        self.value_address = value_address
        self.value_department = value_department
        Employee.count = Employee.count + 1

    def diplay_count(self):
        print("The number of employees is: ", self.count)


root = Tk()
obj = EmployeeeSystem(root)
root.mainloop()
