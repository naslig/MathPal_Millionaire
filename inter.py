""" NAFIU GARBA (+2348078395691) gnasleeg@hotmail.com """
from tkinter import*
import pygame

from tkinter import messagebox

pygame.init()


root = Tk()
root.title("Kids game")
root.geometry('1352x652+0+0')
root.configure(background ='')
#root.image = PhotoImage(file='back.png')
root.image = pygame.image.load("back.png")

current = 0
#===============================Frames------------------------------------------
photoww = PhotoImage(file=r"back.png")
ABC = Button(root, bg='white', width=900, height=600, image=photoww)
ABC.grid()


ABC1= Button(root, bd=20, width=900, height=600, image=photoww)
ABC1.grid(row=0,column=0)


ABC2= Frame(root, bg='', bd=20, width=452, height=600)
ABC2.grid(row=0,column=1)

ABC1a= Frame(ABC1, bg='', bd=20, width=900, padx=150, height=200)
ABC1a.grid(row=0,column=0)
ABC1b= Frame(ABC1, bg='', bd=20, width=900, height=200)
ABC1b.grid(row=1,column=0)
ABC1c= Frame(ABC1, bg='', bd=20, width=900, height=200)
ABC1c.grid(row=2,column=0)

#===============================---Images--------------------------------------------------------

def Change50_50():
    canvas = Canvas(ABC1a, bg='white', width=180, height=80)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'no50.png')
    canvas.create_image(90,40, image=image1)
    canvas.image = image1

def PeopleChange():
    canvas = Canvas(ABC1a, bg='white', width=180, height=80)
    canvas.grid(row=0, column=1)
    canvas.delete('all')
    image1 = PhotoImage(file = 'noPeople.png')
    canvas.create_image(90,40, image=image1)
    canvas.image = image1

def PhoneChange():
    canvas = Canvas(ABC1a, bg='white', width=180, height=80)
    canvas.grid(row=0, column=2)
    canvas.delete('all')
    image1 = PhotoImage(file = 'noPhone.png')
    canvas.create_image(90,40, image=image1)
    canvas.image = image1

def MillionPicture0():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture0.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1

def MillionPicture1():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture1.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture2():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture2.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture3():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture3.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture4():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture4.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture5():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture5.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture6():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture6.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture7():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture7.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture8():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture8.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture9():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture9.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture10():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture10.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture11():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture11.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture12():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture12.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture13():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture13.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture14():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture14.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1

def MillionPicture15():
    canvas = Canvas(ABC2, bg='white', width=350, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file = 'Picture15.png')
    canvas.create_image(215,300, image=image1)
    canvas.image = image1


#==================================Images---------------------------------------------------------


CentreImage = PhotoImage(file = 'milloo.png')
LogoCentre  = Button(ABC1b, image = CentreImage, bg='white', width=300, height=200)
LogoCentre.grid()

Image50_50 = PhotoImage(file = 'pifty_pifty.png')
Live50_50  = Button(ABC1a, image = Image50_50, bg='white', width=180, height=80, command=Change50_50)
Live50_50.grid(row=0,column=0)

ImagePeople = PhotoImage(file = 'people_people.png')
LivePeople  = Button(ABC1a, image = ImagePeople, bg='white', width=180, height=80, command=PeopleChange)
LivePeople.grid(row=0,column=1)

ImagePhone = PhotoImage(file = 'phone_phone.png')
LivePhone  = Button(ABC1a, image = ImagePhone, bg='white', width=180, height=80, command=PhoneChange)
LivePhone.grid(row=0,column=2)

MillionImage = PhotoImage(file = 'Picture0.png')
MillionImg  = Button(ABC2, image = MillionImage, bg='white', width=350, height=600)
MillionImg.grid(row=0,column=0)

#===============================Million Questions ---------------------------------------

Question1 = StringVar()
Question2 = StringVar()
Question3 = StringVar()
Question4 = StringVar()
Question5 = StringVar()

Answer1 = StringVar()
Answer2 = StringVar()
Answer3 = StringVar()
Answer4 = StringVar()

Question1.set("Q1: What is 2 + 32")
Answer1.set("22")
Answer2.set("32")
Answer3.set("31")
Answer4.set("34")
#global current
current = 1

def Question2():
    Question1.set("Q2: What is the product of 256 and 134")
    Answer1.set("34 304")
    Answer2.set("43 403")
    Answer3.set("54 504")
    Answer4.set("65 605")
    global current
    current = 2
    MillionPicture1()


def Question3():
    Question1.set("Q3: Divide 6729 by 50 ")
    Answer1.set("181 remainder 11")
    Answer2.set("314 remainder 1")
    Answer3.set("134 remainder 29")
    Answer4.set("300 remainder 31")
    global current
    current = 3
    MillionPicture2()

def Question4():
    Question1.set("Q4: Find the sum of 2.578km, 0.690km and 1.004km")
    Answer1.set("4.182 km")
    Answer2.set("4.272 km")
    Answer3.set("4.282 km")
    Answer4.set("4.172 km")
    global current
    current = 4
    MillionPicture3()

def Question5():
    Question1.set("Q5: A boy's pace is 0.64m How many metres does he walk in 400 paces ?")
    Answer1.set("625")
    Answer2.set("265")
    Answer3.set("400.64")
    Answer4.set("399.36")
    global current
    current = 5
    MillionPicture4()

def Question6():
    Question1.set("Q6: 1 metre of cutton material cost 4.50 naira. what is the cost of 7.5 ?")
    Answer1.set("1.67")
    Answer2.set("12.0")
    Answer3.set("7.45")
    Answer4.set("33.75")
    global current
    current = 6
    MillionPicture5()

def Question7():
    Question1.set("Q7: Change 12 (1/2) % to decimal ")
    Answer1.set("3.125")
    Answer2.set("2.125")
    Answer3.set("6.125")
    Answer4.set("0.125")
    global current
    current = 7
    MillionPicture6()

def Question8():
    Question1.set("Q8: Change 1 (1/3) to percentage")
    Answer1.set("15 (1/3)%")
    Answer2.set("75 (1/3)%")
    Answer3.set("125 (1/3)%")
    Answer4.set("133 (1/3)%")
    global current
    current = 8
    MillionPicture7()

def Question9():
    Question1.set("Q9: Which is greater 0.05 and 4% ")
    Answer1.set("same")
    Answer2.set("4")
    Answer3.set("error")
    Answer4.set("0.05")
    global current
    current = 9
    MillionPicture8()

def Question10():
    Question1.set("Q10: 1 plus 1")
    Answer1.set("1")
    Answer2.set("11")
    Answer3.set("111")
    Answer4.set("2")
    global current
    current = 10
    MillionPicture9()

def Question11():
    Question1.set("Q11: What is the cube root of 81")
    Answer1.set("3")
    Answer2.set("6561")
    Answer3.set("9")
    Answer4.set("4.3")
    global current
    current = 11
    MillionPicture10()

def Question12():
    Question1.set("Q12: Solve (3 power 4) divide by  (3 power 2)")
    Answer1.set("81")
    Answer2.set("2")
    Answer3.set("729")
    Answer4.set("9")
    global current
    current = 12
    MillionPicture11()

def Question13():
    Question1.set("Q13: How many months have 28 days")
    Answer1.set("1")
    Answer2.set("2")
    Answer3.set("6")
    Answer4.set("12")
    global current
    current = 13
    MillionPicture12()

def Question14():
    Question1.set("Q14: find X    -15 + (-5x) = 0 ")
    Answer1.set("+5")
    Answer2.set("+3")
    Answer3.set("0")
    Answer4.set("-3")
    global current
    current = 14
    MillionPicture13()

def Question15():
    Question1.set("Q15: What is 1.92 divided by 3")
    Answer1.set("0.46")
    Answer2.set("6.04")
    Answer3.set("5.76")
    Answer4.set("0.64")
    global current
    current = 15
    MillionPicture14()


def Quest(args):
    global current
    if current==1 and args ==4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question2()
    elif current == 1 and args == 1:
        top = Tk()
        top.geometry("100x100")
        messagebox.showerror("WRONG OPTION", "Oooopx... You are wrong!!! TRY AGAIN ?")
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 1 and args == 2:
        top = Tk()
        top.geometry("100x100")
        messagebox.showerror("WRONG OPTION", "Oooopx... You are wrong!!! TRY AGAIN ?")
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 1 and args == 3:
        top = Tk()
        top.geometry("100x100")
        messagebox.showerror("WRONG OPTION", "Oooopx... You are wrong!!! TRY AGAIN ?")
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 2 and args == 1:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question3()
    elif current == 2 and args == 4:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 2 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 2 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 3 and args == 3:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question4()
    elif current == 3 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 3 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 3 and args == 4:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()


    elif current == 4 and args == 2:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question5()
    elif current == 4 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 4 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 4 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 5 and args == 2:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question6()
    elif current == 5 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 5 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 5 and args == 4:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 6 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question7()
    elif current == 6 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 6 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 6 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 7 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question8()
    elif current == 7 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 7 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 7 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 8 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question9()
    elif current == 8 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 8 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 8 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 9 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question10()
    elif current == 9 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 9 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 9 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()


    elif current == 10 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question11()
    elif current == 10 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 10 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 10 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()


    elif current == 11 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question12()
    elif current == 11 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 11 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 11 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 12 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question13()
    elif current == 12 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 12 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 12 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 13 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question14()
    elif current == 13 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 13 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 13 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 14 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("BRAVO...!!!", "You are absolutely right!!! Click to proceed")
        Question15()
    elif current == 14 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 14 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 14 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()

    elif current == 15 and args == 4:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("YOU WON", "CONGRATULATIONS YOU ARE A MILLIONAIRE...!!!")
        Question15()
    elif current == 15 and args == 1:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 15 and args == 2:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    elif current == 15 and args == 3:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()
    else:
        Question1.set("Q1: What is 2 + 32")
        Answer1.set("22")
        Answer2.set("32")
        Answer3.set("31")
        Answer4.set("34")
        current = 1
        MillionPicture0()



#===============================Text,Label,buttons---------------------------------------




txtQuestion = Entry(ABC1c, font=('arial', 18, 'bold'), bg='purple', fg='white', bd=5, width=44, justify=CENTER, textvariable =Question1)

txtQuestion.grid(row=0, column=0, columnspan=4, pady=4)

lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'),text='A: ', bg='maroon', fg='white', bd=5, justify=CENTER)
lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

txtQuestion1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='maroon', fg='white', bd=1, width=17, height=2, justify=CENTER, textvariable =Answer1, command =lambda:Quest(1))
txtQuestion1.grid(row=1, column=1, pady=4)


lblQuestB = Label(ABC1c, font=('arial', 14, 'bold'),text='B: ', bg='blue', fg='white', bd=5, justify=LEFT)
lblQuestB.grid(row=1, column=2, pady=4, sticky=W)

txtQuestion2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2, justify=CENTER, textvariable =Answer2, command =lambda:Quest(2))
txtQuestion2.grid(row=1, column=3, pady=4)


lblQuestC = Label(ABC1c, font=('arial', 14, 'bold'),text='C: ', bg='orange', fg='white', bd=5, justify=LEFT)
lblQuestC.grid(row=2, column=0, pady=4, sticky=W)

txtQuestion3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='orange', fg='white', bd=1, width=17, height=2, justify=CENTER, textvariable =Answer3, command =lambda:Quest(3))
txtQuestion3.grid(row=2, column=1, pady=4)


lblQuestD = Label(ABC1c, font=('arial', 14, 'bold'),text='D: ', bg='lime', fg='white', bd=5, justify=LEFT)
lblQuestD.grid(row=2, column=2, pady=4, sticky=W)

txtQuestion4 = Button(ABC1c, font=('arial', 14, 'bold'), bg='lime', fg='white', bd=1, width=17, height=2, justify=CENTER, textvariable =Answer4, command =lambda:Quest(4))
txtQuestion4.grid(row=2, column=3, pady=4)


root.mainloop()
