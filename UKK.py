from tkinter import*
import math

root = Tk()
blank_space = " "
root.title(50 * blank_space + "Calculator") 
root.resizable(width = False, height = False )
#mengatur size apknya
root.geometry("438x573+460+40")

# create a frame
coverFrame = Frame (root, bd=20, pady=2, relief=RIDGE)
coverFrame.grid()

# child of coverFrame
coverMainFrame = Frame (coverFrame, bd=10, pady=2, bg='Black', relief=RIDGE)
coverMainFrame.grid()

# mainFrame child of coverMainFrame
MainFrame = Frame (coverMainFrame, bd=5, pady=2, relief=RIDGE)
MainFrame.grid()

# membuat class
class Calculator():
       # membuat function namanya self
       def __init__(self):
              # manggilfunctionnya 'self'
              self.total = 0
              self.current = ""
              self.input_value = True
              self.check_sum = False
              self.op=""
              self.result = False

       # membuat function biar button nya berfungsi
       # num:parameter
       def numberEnter(self,num):
              self.result = False
              firstnum = entDisplay.get() 
              secondnum = str(num)
              if self.input_value:
                     self.current = secondnum
                     self.input_value = False
              else:
                     if secondnum == '.':
                            if secondnum in firstnum():
                                   return
                     self.current = firstnum +secondnum
              self.display(self.current)

       def display(self,value):
              entDisplay.delete(0, END)
              entDisplay.insert(0, value)

       def sum_of_total(self):
              self.result = True
              self.current = float(self.current)
              if self.check_sum == True:
                     self.valid_function()
              else:
                     self.total= float(entDisplay.get())
       def valid_function(self):
              if self.op == "Add":
                     self.total += self.current
              if self.op == "Pengurangan":
                     self.total -= self.current
              if self.op == "Kali":
                     self.total *= self.current
              if self.op == "Bagi":
                     self.total /= self.current
              if self.op == "Persen":
                     self.total %= self.current
              self.input_value = True
              self.check_sum = False
              self.display(self.total)
       def operation(self, op):
              self.current = float(self.current)
              if self.check_sum:
                     self.valid_function()
              elif not self.result:
                     self.total = self.current
                     self.input_value = True
              self.check_sum = True
              self.op = op
              self.result = False

       def backspace(self):
              numLen = len(entDisplay.get())
              entDisplay.delete(numLen - 1, 'end')
              if numLen == 1:
                     entDisplay.insert(0,"0")
       def Clear_Entry(self):
              self.result= False
              self.current = "0"
              self.display(0)
              self.input_value = True

       def all_Clear_Entry(self):
              self.Clear_Entry()
              self.total = 0

       def mathsPM(self):
              self.result = False
              self.current = -(float(entDisplay.get()))
              self.display(self.current)

       def squared(self):
              self.result = False
              self.current = math.sqrt(float(entDisplay.get()))
              self.display(self.current)

       def cos(self):
              self.result = False
              self.current = math.cos(math.radians(float(entDisplay.get())))
              self.display(self.current)

       def tan(self):
              self.result = False
              self.current = math.tan(math.radians(float(entDisplay.get())))
              self.display(self.current)

       def sin(self):
              self.result = False
              self.current = math.sin(math.radians(float(entDisplay.get())))
              self.display(self.current)


# memanggil class calculator
added_value = Calculator()
# Child of MainFrame
# ini desain buat yg form calculatornya
entDisplay = Entry(MainFrame, font=('arial',18, 'bold'), bd=14, width=26,bg='white', justify=RIGHT)
entDisplay.grid(row =0, column=0, columnspan=4, pady=1)
entDisplay.insert(0, "0")

numpad = "789456123"
i = 0
btn =[]

for j in range(3,6):
       # ini tu nanti pas ngatur column manggil k berarti columnnya 3
       for k in range(3):
              # letaknya dlm mainFrame
              btn.append(Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text=numpad[i] ))
              # bd :border
              btn[i].grid(row=j,column=k, pady=1)
              #kan ngambil dari numpad, abis itu kita tampilin nih si [i] nya
              # kaya gitu terus sambil i nya itu ditambah 1 +1 terus, jadi dia menampilkan semua datanya, systemnya kayanya dia array deh
              
              # biar angkanya mau diketik,make function number enter
              btn[i]["command"] = lambda x=numpad[i]: added_value.numberEnter(x)
              i += 1

       # BACKSPACE
       # membuat button backspace, 
       btnBackSpace=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="←" , bg='Orange'
                           , command = added_value.backspace) #command : memberikan perintah ketika button ini diketik,memanggil functio yan kita buat
       #posisi buttonnya
       btnBackSpace.grid(row=1,column=0,pady=1)
   
       # CLEAR
       btnClear=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text=chr(67) , bg='Orange'
                       , command = added_value.Clear_Entry)
       btnClear.grid(row=1,column=1,pady=1)
   
       
       btnClearAll=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text=chr(67)+chr(69) , bg='Orange'
                         , command = added_value.all_Clear_Entry )
       btnClearAll.grid(row=1,column=2,pady=1)
   
       btnPM=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text=chr(177) , bg='Orange'
                    , command = added_value.mathsPM)#plus min function
       #posisi buttonnya
       btnPM.grid(row=1,column=3,pady=1)
# ===================================================================================================================================================
       btnSq=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="√"
                    , command = added_value.squared) #akar
       #posisi buttonnya
       btnSq.grid(row=2,column=0,pady=1)
       
       btnSin=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="Sin"
                    , command = added_value.sin)
       #posisi buttonnya

       btnSin.grid(row=2,column=1,pady=1)
       
       btnCos=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="Cos"
                   , command = added_value.cos )
       #posisi buttonnya
       btnCos.grid(row=2,column=2,pady=1)
       
       btnTan=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="Tan", bg='Orange'
                    , command = added_value.tan)
       #posisi buttonnya
       btnTan.grid(row=2,column=3,pady=1)
# ===============================================================SCIENTIFIC============================================================================
       btnTambah=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="+" , bg='Orange'
                        , command = lambda:added_value.operation("Add"))
       #posisi buttonnya
       btnTambah.grid(row=3,column=3,pady=1)

       # Pengurangan
       btnPengurangan=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="-" , bg='Orange'
                            , command = lambda:added_value.operation("Pengurangan"))
       #posisi buttonnya
       btnPengurangan.grid(row=4,column=3,pady=1)

       # Perkalian
       btnKali=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="*" , bg='Orange'
                       , command = lambda:added_value.operation("Kali"))
       #posisi buttonnya
       btnKali.grid(row=5,column=3,pady=1)

       # Pembagian
       btnPembagian=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text=chr(247) , bg='Orange'
                           , command = lambda:added_value.operation("Bagi"))
       #posisi buttonnya
       btnPembagian.grid(row=6,column=3,pady=1)

       btnZero=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="0" , bg='Orange'
                       , command = lambda:added_value.numberEnter(0))
       #posisi buttonnya
       btnZero.grid(row=6,column=0,pady=1)

       btnDesimal=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="." , bg='Orange'
                          , command = lambda:added_value.numberEnter("."))
       #posisi buttonnya
       btnDesimal.grid(row=6,column=1,pady=1)

       btnHasil=Button(MainFrame, width=6, height=2, font=('arial',16,'bold'),bd=4, text="=" , bg='Orange'
                        , command = added_value.sum_of_total)
       #posisi buttonnya
       btnHasil.grid(row=6,column=2,pady=1)
# ======================================================================================================================================================

root.mainloop()