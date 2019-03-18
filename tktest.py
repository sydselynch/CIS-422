from tkinter import *
contacts=['Justin Day']

class Contact_manager (Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Contact Manager")
        self.pack(fill=BOTH, expand=1)

        #New contact grid
        Label (self, text = "New Contact").grid (row=0, column=2, columnspan=2, sticky=W)
        Label (self, text = "First Name:").grid (row=1, column=1, sticky=E)
        Label (self, text = "Last Name:").grid (row=2, column=1, sticky=E)
        Label (self, text = "Phone#").grid (row=3, column=1, sticky=E)

        self.entry1 = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)
        self.entry1.grid (row=1, column=2)
        self.entry2.grid (row=2, column=2)
        self.entry3.grid (row=3, column=2)

        friend_check = IntVar()
        self.friend_check = Checkbutton (self, variable = friend_check,
                                 command = self.friend_box,
                                 text = "Friend")
        self.friend_check.grid (row=4, column=2, columnspan=2)

        Label (self, text = "Email:").grid (row=5, column=1, sticky=E)
        Label (self, text = "Birthday:").grid (row=6, column=1, sticky=E)

        self.entry4 = Entry(self)
        self.entry5 = Entry(self)
        self.entry4.grid (row=5, column=2)
        self.entry5.grid (row=6, column=2)

        #Contact listbox
        Label (self, text = "Contact List").grid(row=0)
        contact_lb = Listbox(self)
        for i in contacts:
            contact_lb.insert(END, i)

        contact_lb.bind("<<ListboxSelect>>", self.onSelect)
        contact_lb.grid(row=1, rowspan=5)

    def onSelect(self, val):

        sender = val.widget
        idk = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)

    def friend_box():
        if friend_check.get() == 1:
            contacts.append(Friend(f, l, p, e, bd))
        else:
            contacts.append(Person(f, l, p))
def main():

    root = Tk()
    ex = Contact_manager(root)
    root.geometry('600x700+200+100')
    root.mainloop()

if __name__ == '__main__':
    main()
