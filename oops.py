class employee:

    def __init__(self,name,email ):
        self.name = name
        self.email = email

    def get_info(self):
        print(self.name,self.email)


per = employee("MOHAMED MUFARIS",' xyz.y@gmail.com')
print(per.get_info())


