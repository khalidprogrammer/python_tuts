class Electronic:
    name = "Computer"
    model = "HP"
    camera ="Dell 4.5px"
    charger = "Yes"
    display ="Tube LCD"

    def PrintDevice(self):
        return f"Name is {self.name} \n Model is {self.model} \n Charger is {self.charger} \n Display is {self.display} "

class PhoneGadget(Electronic):
    hdmi = "4.5"
    loadspeeaker = "black"
    display  ="LED"

    def PrintDevice(self):
        return f"HDMI is {self.hdmi} and louadspeaker is {self.loadspeeaker} and display is {self.display}"

class phone(PhoneGadget):
    use = "for calling"
    memory =120
    display = "LCD"
    def PrintDevice(self):
        return f"Use is {self.use} and Memory is  {self.memory} and display {self.display}"



E1 = Electronic()
print(E1.PrintDevice())
P1 = PhoneGadget()
print(P1.PrintDevice())
M1 = phone()
print(M1.PrintDevice())
