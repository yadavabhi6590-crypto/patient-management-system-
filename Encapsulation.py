
class pitient :
    def __init__(Self,name,age):
        Self.name=name
        Self.age=age
        Self.__report=[]
        Self.__disease=[]
        Self.__bill=0

    def update_report(Self ,doctor_id,report):
        if doctor_id=="DOC123":
            Self.__report.append(report)
        else:
            print("You are not allowed")

    def add_update(self, doctor_id,amount,new_disease):
        if doctor_id=="DOC123":
            self.__disease.append(new_disease)
            self.__bill +=amount
            print("Update successfully")
        else:
            print("You cannot update  ")

    def get_report(Self):
        print(f"You report is  {Self.__report}")

    def get_bill(Self):
        print(f"Your diseas {Self.__disease} and bill: {Self.__bill}")
    def get_details(Self):
        print(f"Your name is:{Self.name} Age :{Self.age} ")


p1=pitient("Satish",27)

# p1.get_details()
p1.add_update(doctor_id="DOC123",amount=500, new_disease= "fever")
p1.add_update(doctor_id="DOC123",amount=300, new_disease= "cold")

p1.update_report("DOC123","Patient is recovering")

p1.get_report()
p1.get_bill()

