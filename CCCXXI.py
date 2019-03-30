'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python CCCXXI.py
    or if it doesn't work use this one:
        python3 CCCXXI.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''

from mpmath import *
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry, Radiobutton, Button, Style

mp.dps = 50000; mp.pretty = True

class CCCXXI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("CCCXXI")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global v
        v = IntVar()
        v.set(1)
        
        global exp
        exp = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self,style='My.TFrame')
        frame1.pack(fill=X)
		
        
        rb1 = Radiobutton(frame1, text = "3*2^n-1", variable = v, value = 1,style='My.TRadiobutton')
        rb1.pack( anchor = W )
		
        rb2 = Radiobutton(frame1, text = "3*2^n+1", variable = v, value = 2,style='My.TRadiobutton')
        rb2.pack( anchor = W )
		
        
       
		
        frame2 = Frame(self,style='My.TFrame')
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Enter the exponent :", width=18,background='orange')
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2,textvariable=exp,style='My.TEntry')
        entry2.pack(fill=X, padx=5, expand=True)

        
        frame3 = Frame(self,style='My.TFrame')
        frame3.pack(fill=X)

        result = Label(frame3, textvariable=res, width=42,background='orange')
        result.pack(side=LEFT, padx=60, pady=5)

		
        frame4 = Frame(self,style='My.TFrame')
        frame4.pack(fill=X)

        btntest = Button(frame4, text="Test", width=10, command=self.test,style='My.TButton')
        btntest.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclear = Button(frame4, text="Clear", width=10, command=self.clear,style='My.TButton')
        btnclear.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclose = Button(frame4, text="Close", width=10, command=self.quit,style='My.TButton')
        btnclose.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
        
        elif msg == 'erre':
            tkinter.messagebox.showerror('Error!', 'Exponent must be greater than two')
			
    
        
    

    def test(self):
        try:
            
            
            n = int(exp.get())
			
           
            if n<3:
                self.errorMsg('erre')
            else:
				
               
                def jacobi(a,q):
                    j=1
                    while a != 0:
                        while a%2==0:
                            a=a/2
                            if q%8==3 or q%8==5:
                                j=-j
                        #interchange(a,q)
                        c=a
                        a=q
                        q=c
                        if a%4==3 and q%4==3:
                            j=-j
                        a=fmod(a,q)
                    if q==1:
                        return j
                    else:
                        return 0
            
                if v.get()==1:
                    M=3*2**n-1
                    if n%4==1:
                        value="3*2^"+str(n)+"-1 is composite"
                        res.set(self.makeAsItIs(value))
                    else:
                        if n%4==0 or n%4==3:
                            s=18
                        elif n%12==2 or n%12==6:
                            s=110
                        elif n%24==10:
                            s=3330
                        elif n%48==22:
                            s=57511298
                        else:
                            d=3
                            while not(jacobi(d-2,M)==1 and jacobi(d+2,M)==-1):
                                d=d+1
                            s=d**3-3*d
                        s=s%M
                        ctr=1
                        while ctr<=n-2:
                            s=(s**2-2)%M
                            ctr=ctr+1
                        if int(s)==0:
                            value="3*2^"+str(n)+"-1 is prime"
                            res.set(self.makeAsItIs(value))
                        else:
                            value="3*2^"+str(n)+"-1 is composite"
                            res.set(self.makeAsItIs(value))
					
                else:
                    N=3*2**n+1
                    if n%4==3:
                        value="3*2^"+str(n)+"+1 is composite"
                        res.set(self.makeAsItIs(value))
                    else:
                        if n%4==1:
                            s=32672
                        elif n%12==2:
                            s=1692
                        elif n%12==6 or n%12==10:
                            s=21868
                        elif n%12==8:
                            s=50542
                        else:
                            d=3
                            while not(jacobi(d-2,N)==-1 and jacobi(d+2,N)==-1):
                                d=d+1
                            s=d**3-3*d
                        s=s%N
                        ctr=1
                        while ctr<=n-2:
                            s=(s**2-2)%N
                            ctr=ctr+1
                        if int(s)==0:
                            value="3*2^"+str(n)+"+1 is prime"
                            res.set(self.makeAsItIs(value))
                        else:
                            value="3*2^"+str(n)+"+1 is composite"
                            res.set(self.makeAsItIs(value))
          
        except:
            self.errorMsg('error')
			
    def clear(self):
        try:
            res.set('')
            exp.set('')
        except:
            self.errorMsg('error')
			
    
    def makeAsItIs(self, value):
        return value

def main():
    root = Tk()
    root.resizable(0,0)
    s = Style()
    s.configure('My.TFrame', background='orange')
    s.configure('My.TButton', background='light gray')
    s.configure('My.TEntry', fieldbackground='light gray')
    s.configure('My.TRadiobutton', background='orange')
    s.map('My.TRadiobutton', background=[('active', '#FFC133')])
    root.geometry("300x125")
    cccxxi = CCCXXI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
