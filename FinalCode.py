menu='''
1.Reservation
2.Todays Flights
3.Aircraft Validations
4.Passenger Validations
5.Reports Generation
6.Confirm a waitlisted booking
7.Cancel a waitlisted booking
0.Exit
'''

import csv
from datetime import date
today=date.today()
a=str(today)
pname='P'+a[-2:]+a[-5:7]+a[2:4]
import os.path
file_exists = os.path.exists(pname+'.csv')
if file_exists==False:
    f2=open(pname+'.csv','a+',newline='')
    f2w=csv.writer(f2)
    f2r=csv.reader(f2)
    header=['Flight Number','PNR Number','Seat Number','Departure City','Arrival City','Name of the passenger','Age','Sex','Email','Mobile','Amount Paid','Status']
    f2w.writerow(header)
else:
    f2=open(pname+'.csv','r+',newline='')
    f2w=csv.writer(f2)
    f2r=csv.reader(f2)
    bf2=[]
    for i in f2r:
        bf2.append(i)
    if len(bf2)>1:
        if bf2[0]==['Flight Number','PNR Number','Seat Number','Departure City','Arrival City','Name of the passenger','Age','Sex','Email','Mobile','Amount Paid','Status']:
            pass
        else:
            header=['Flight Number','PNR Number','Seat Number','Departure City','Arrival City','Name of the passenger','Age','Sex','Email','Mobile','Amount Paid','Status']
            f2w.writerow(header)
    else:
        if bf2==['Flight Number','PNR Number','Seat Number','Departure City','Arrival City','Name of the passenger','Age','Sex','Email','Mobile','Amount Paid','Status']:
            pass
        else:
            header=['Flight Number','PNR Number','Seat Number','Departure City','Arrival City','Name of the passenger','Age','Sex','Email','Mobile','Amount Paid','Status']
            f2w.writerow(header)
import csv
from datetime import date
today=date.today()
a=str(today)
fname='F'+a[-2:]+a[-5:7]+a[2:4]
file_exists = os.path.exists(fname+'.csv')
if file_exists==False:
    f1=open(fname+'.csv','w',newline='')
    f=open("Aircraft.csv","r")
    b=csv.reader(f)
    a1=csv.writer(f1)
    a1.writerow(["Fl_No",'Occupied'])
    for record in b:
        if str(record[2]).isdigit()==True:   
            flno2=record[0]
            recflight=[flno2,0]
            a1.writerow(recflight)
    f1.close()
else:
    pass
f2=open(pname+'.csv','r+',newline='')
f2w=csv.writer(f2)
f2r=csv.reader(f2)
bf2=[]
for i in f2r:
    bf2.append(i)
f2.close()
def op1():
    #f2=open('Passenger.csv','a+',newline='')
    import csv
    f2=open(pname+'.csv','r+',newline='')
    f2w=csv.writer(f2)
    f2r=csv.reader(f2)
    bf2=[]
    for i in f2r:
        bf2.append(i)
    import csv
    f=open('Aircraft.csv','r')
    f2w=csv.writer(f2)
    b=csv.reader(f)
    a=[]
    for i in b:
        a.append(i)
    initq=input("Do you want to have a look report of the flights before reservation?(Y/N)")
    if initq.upper()=='Y':
        op2()
    else:
         pass
    Dep=input('Enter Departure City:')
    while True:
        found=0
        for i in a:
            if Dep.upper()==i[3].upper():
                found=1
            '''elif Dep.upper()=='R':
                op1()'''
        if found==0:
            print("Oops! No flights are departing from this city today! Try Again")
            Dep=input('Enter Departure City:')
        if found==1:
            break  
    Arr=input('Enter Arrival City:')
    while True:
        found=0
        for i in a:
            if Arr.upper()==i[4].upper() and Dep.upper()==i[3].upper():
                found=1
                break
        if found==1:
            break  
        if found==0:
            print("Oops! No flights are arriving to this city today from",Dep,"! Try Again")
            Arr=input('Enter Arrival City:')
    Name=input('Enter Name of the passenger:')
    Age=input('Enter Age:')
    Sex=input('Enter Sex:')
    Email=input('Enter Email:')
    mobile=input('Enter Mobile Number:')
    for i in a:
        if Arr.upper()==i[4].upper() and Dep.upper()==i[3].upper():
            flno=i[0]
            amount=i[7]
            capacity=i[2]
    print('Choose the number of your seat:')
    circles=[]
    cap=[]
    for i in range(1,int(capacity)+1):
        cap.append(i)
    bookeds=[]
    for i in bf2:
        if i[2]=='Seat Number' :
            pass
        elif Arr.upper()==i[4].upper() and Dep.upper()==i[3].upper():
            bookeds.append(int(i[2]))
    bookeds=sorted(bookeds)
    for i in range(1,len(cap)+1):
        if i in bookeds:
            circles.append('⚫')
        else:
            circles.append('⚪')                   
    print('Seats Booked-⚫   Seats Empty-⚪')
    coun=1
    for i in range(len(cap)//10):
        for k in range(i,i+10):
            if coun<=9:
                print("  "+str(coun)+'-'+circles[coun-1],end='')
            elif coun>9 and coun<100:
                print(" "+str(coun)+'-'+circles[coun-1],end='')
            else:
                print(str(coun)+'-'+circles[coun-1],end='')
            coun+=1
        print('\n')
    for i in range(coun+1,len(cap)+1):
        print(str(coun)+'-'+circles[coun],end='')
        coun+=1
    print(str(int(capacity))+'-'+circles[int(capacity)-1],end='')
    print('\n')
    print('Capcity:',capacity)
    sn=int(input('Enter the seat you want to choose:'))
    while True:
        if sn>int(capacity):
            print("Sorry maximum capacity is",len(cap))
            sn=int(input('Enter the seat you want to choose:'))
        if sn<=0:
            print("Invalid Input")
            sn=int(input('Enter the seat you want to choose:'))
        if sn in bookeds:
            print('Sorry already booked!')
            sn=int(input('Enter the seat you want to choose:'))
        else:
            break
    bookeds.append(sn)
    confirmation=input('Confirm Reservation?(C/W):')
    print('Your flight number will be:',flno)
    print('Amount to be paid:',amount)
    if confirmation.upper()=='C':
        lc=[]
        c=1
        for i in bf2:
            if i[1]=='PNR Number':
                pass
            else:
                lc.append(c)
            c+=1
        pnr=len(lc)+1
        print('You are Passenger Number',pnr)
    else:
        pnr=':'
    rec=[flno,pnr,sn,Dep.upper(),Arr.upper(),Name,Age,Sex,Email,mobile,amount,confirmation.upper()]
    f2w.writerow(rec)
    f2.close()
    f.close()
    import os
    fnname=fname+'1'
    with open(fname+'.csv','r+') as old, open(fnname+'.csv','w+',newline='') as new:   
        writer=csv.writer(new)
        for i in csv.reader(old):
            if i[0]==flno.upper():
                newrow=[i[0],int(i[1])+1]
                writer.writerow(newrow)
            else:
                writer.writerow(i)
    new.close()
    old.close()
    os.remove(fname+'.csv')
    os.rename(fnname+'.csv', fname+'.csv')
def op2():
    f=open('aircraft.csv','r')
    a=csv.reader(f)
    gap=' '*3
    sgap=' '
    heading=f"{'Fl_No':5s}{gap}{'Aircraft':3s}{gap}{'Capcity':3s}{gap}{'From':15s}{gap}{'Destination':15s}{gap}{'Departure':5s}{gap}{'Arrival':5s}{gap}{'Total':5s}"
    print("="*93)
    print(heading)
    print("-"*93)
    for i in a:
        if i[0]=='Fl_No':
            continue
        else:
            rec=f"{i[0]:5s}{gap}{i[1]:3s}{gap}{gap}{gap}{i[2]:3s}{gap}{gap}{i[3]:15s}{gap}{i[4]:15s}{gap}{i[5]:5s}{gap}{gap}{sgap}{i[6]:5s}{gap}{sgap}{sgap}{i[7]:5s}"
            print(rec)
    print("-"*93)
    print("="*93)
def op3():
    menu2='''
1.Check for sequence of flight number
2.Time validations for Departure Time and Arrival Time
3.Modification of fields(except Flight Number and Aircraft)
0.Exit'''
    def op_3_1():
        f3_1=open("Aircraft.csv",'r')
    def op_3_2():
        f2=open(pname+'.csv','a+',newline='')
        import csv
        f=open('Aircraft.csv','r')
        b=csv.reader(f)
        a=[]
        for i in b:
            a.append(i)
        timev=input("Enter flight number:")
        while True:
            found=0
            for i in a:
                if timev.upper()==i[0].upper():
                    Dept=i[5]
                    Arrt=i[6]
                    print("Your flight will commence from",i[3],"at",Dept,"and land at",i[4],"at",Arrt)
                    found=1
            if found==1:
                break
            if found!=1:
                print("Invalid flight number, Try Again")
                prompt31=input("Do you wanna go back or try again?(B/T)")
                if prompt31=='B':
                    op3()
                    break
                elif prompt31=='T':
                    timev=input("Enter flight number:")
                else:
                    print('Invalid Input')
        f2.close()
        f.close()
    def op_3_3():
        fln33=input("Enter flight number:")
        f=open('Aircraft.csv','r')
        b=csv.reader(f)
        a=[]
        for i in b:
            a.append(i)
        prompt31='T'
        while True:
            found=0
            for i in a:
                if fln33.upper()==i[0].upper():
                    found=1
            if found==1 or prompt31=='B':
                break
            else:
                print('Invalid Flight Number,Try Again')
                prompt31=input("Do you wanna go back or try again?(B/T)")
                if prompt31=='B':
                        break
                elif prompt31=='T':
                    timev=input("Enter flight number:")
                else:
                    print('Invalid Input')
                    prompt31=input("Do you wanna go back or try again?(B/T)")
        if prompt31=='B':
            op3()
        input33=input('''
    1.Capacity
    2.From (Starting Place)
    3.Destination Place
    4.Departure Time
    5.Arrival Time
    6.Total Expenses
    Which field would you like to change?
    ''')
        while True:
            found=0
            for i in a:
                if input33=='1':
                    input33v='Capacity'
                elif input33=='2':
                    input33v='From (Starting Place)'
                elif input33=='3':
                    input33v='Destination Place'
                elif input33=='4':
                    input33v='Departure Time'
                elif input33=='5':
                    input33v='Arrival Time'
                elif input33=='6':
                    input33v='Total Expenses'
                found=1
            if found==1:
                break
            else:
                print('Invalid Input,Try Again')
                input33=input('''
                1.Capacity
                2.From (Starting Place)
                3.Destination Place
                4.Departure Time
                5.Arrival Time
                6.Total Expenses
                Which field would you like to change?
                ''')
        ch33=input("Please enter the new value of "+input33v+': ')
        #i[int(input33)+1]=ch33
        f.close()
        import os
        with open('Aircraft.csv', 'r+') as old, open('Aircraft1.csv', 'w+',newline='') as new:   
            writer=csv.writer(new)
            for i in csv.reader(old):
                if i[0]==fln33.upper():
                    newrow=[]
                    for j in i:
                        index=i.index(j)
                        if index==int(input33)+1:
                            newrow.append(ch33)
                        else:
                            newrow.append(j)
                    writer.writerow(newrow)
                else:
                    writer.writerow(i)
        new.close()
        old.close()
        os.remove('Aircraft.csv')
        os.rename('Aircraft1.csv', 'Aircraft.csv')
    while True:
        print(menu2)
        op3f=int(input("Enter an option for validation:"))
        if op3f==1:
            op_3_1()
        elif op3f==2:
            op_3_2()
        elif op3f==3:
            op_3_3()
        elif op3f==0:
            break
        else:
            print('Invalid input!')
def op4():
    menu='''
1) Check whether the Fl_No existing in the Air Master or not
2) Check whether the Dplace is valid destination place or not (from Aircraft)
0)Break
'''
    def op4_1():
        fln33=input("Enter flight number:")
        f=open('Aircraft.csv','r')
        b=csv.reader(f)
        a=[]
        for i in b:
            a.append(i)
        found=0
        for i in a:
            if fln33.upper()==i[0].upper():
                found=1
        if found==1:
            print('Flight number exists')
        else:
            print('Flight Number does not exist')
    def op4_2():
        dp=input("Enter Destination Place:")
        f=open('Aircraft.csv','r')
        b=csv.reader(f)
        a=[]
        found=0
        for i in b:
            a.append(i)
        for i in a:
            if dp.upper()==i[4].upper():
                found=1
        if found==1:
            print('Destination Place exists')
        else:
            print('Destination Place does not exist')
    while True:
        print(menu)
        op=int(input('Enter option:'))
        if op==1:
            op4_1()
        elif op==2:
            op4_2()
        elif op==0:
            break
        else:
            print('Invlid Input')
def op5():
    def op5_1():
        from datetime import date
        today=date.today()
        datee=str(today)
        f=open(pname+'.csv','r')
        f1=open('Aircraft.csv','r')
        b=csv.reader(f1)
        a=csv.reader(f)
        inputfn=input("Enter Flight Number")
        inputpn=input("Enter Passenger Number")
        gap=' '*6
        sgap=' '
        title=f"{gap}*20{'Air Goes International Airlines'}{gap}*20"
        heading=f"{'Fl_No':5s}{gap}{'Aircraft':3s}{gap}{'Capcity':3s}{gap}{'From':15s}{gap}{'Destination':15s}{gap}{'Departure':5s}{gap}{'Arrival':5s}{gap}{'Total':5s}"
        found=0
        for i in a:
            if i[0]=='Fl_No':
                continue
            elif i[1]==inputpn and i[0]==inputfn:
                pnr=i[1].upper()
                fno=i[0].upper()
                status=i[11].upper()
                seatn=i[2].upper()
                fromp=i[3].upper()
                top=i[4].upper()
                name=i[5].upper()
                age=i[6].upper()
                cont=i[9].upper()
                fare=i[10].upper()
                found=1
                #rec=f"{i[0]:5s}{gap}{i[1]:3s}{gap}{gap}{gap}{i[2]:3s}{gap}{gap}{i[3]:15s}{gap}{i[4]:15s}{gap}{i[5]:5s}{gap}{gap}{sgap}{i[6]:5s}{gap}{sgap}{sgap}{i[7]:5s}"
                #print(rec)
        if found==1:
            for i in b:
                if i[0]=='Fl_No':
                    continue
                else:
                    if i[0]==inputfn:
                        aircraft=i[1]
            doj=datee
            print('                                Air Goes International Airlines                                    ')
            print('Reservation Slip')
            print('-'*93)
            line1=f"{'PNR Number':15s}{gap}{gap}{pnr:10s}{gap}{gap}{gap}{'Flight Number':15s}{gap}{fno:10s}"
            line2=f"{'Status':15s}{gap}{gap}{status:10s}{gap}{gap}{gap}{'Aircraft':15s}{gap}{aircraft:10s}"
            line3=f"{'Seat Number:':15s}{gap}{gap}{seatn:10s}{gap}{gap}{gap}{'Date of Journey':15s}{gap}{doj:10s}"
            line4=f"{'From':15s}{gap}{gap}{fromp:10s}{gap}{gap}{gap}{'To':15s}{gap}{top:10s}"
            line5=f"{'Name:':15s}{gap}{gap}{name:10s}{gap}{gap}{gap}{'Age':15s}{gap}{age:10s}"
            line6=f"{'Contact':15s}{gap}{gap}{cont:10s}{gap}{gap}{gap}{'Fare':15s}{gap}{fare:10s}"
            print(line1)
            print(line2)
            print(line3)
            print(line4)
            print(line5)
            print(line6)
            print("-"*93)
        else:
            print('Sorry! The PNR or Flight Number is wrong!')
            try1=input("Do you wanna try again or exit?(T or E)")
            if try1=='T':
                op5_1()
            else:
                main()
    def op5_2():
        from datetime import date
        today=date.today()
        datee=str(today)
        f=open(pname+'.csv','r')
        f1=open('Aircraft.csv','r')
        b=csv.reader(f1)
        a=csv.reader(f)
        inputfn=input("Enter Flight Number")
        inputpn=input("Enter Passenger Number")
        gap=' '*6
        sgap=' '
        heading=f"{'Fl_No':5s}{gap}{'Aircraft':3s}{gap}{'Capcity':3s}{gap}{'From':15s}{gap}{'Destination':15s}{gap}{'Departure':5s}{gap}{'Arrival':5s}{gap}{'Total':5s}"
        for i in a:
            if i[0]=='Fl_No':
                continue
            elif i[1]==inputpn:
                pnr=i[1].upper()
                fno=i[0].upper()
                status=i[11].upper()
                seatn=i[2].upper()
                fromp=i[3].upper()
                top=i[4].upper()
                name=i[5].upper()
                age=i[6].upper()
                cont=i[9].upper()
                fare=i[10].upper()
                #rec=f"{i[0]:5s}{gap}{i[1]:3s}{gap}{gap}{gap}{i[2]:3s}{gap}{gap}{i[3]:15s}{gap}{i[4]:15s}{gap}{i[5]:5s}{gap}{gap}{sgap}{i[6]:5s}{gap}{sgap}{sgap}{i[7]:5s}"
                #print(rec)
        for i in b:
            if i[0]=='Fl_No':
                continue
            else:
                if i[0]==inputfn:
                    aircraft=i[1]
        doj=datee
        print("-"*93)
        line0='                                Air Goes International Airlines                                    '
        line1=f"{'Ticket Number':20s}{gap}{gap}{str(int(pnr)+2000):10s}{gap}{gap}{gap}{'Date of Issue':15s}{gap}{doj:10s}"
        line4=f"{'From':20s}{gap}{gap}{fromp:10s}{gap}{gap}{gap}{'To':15s}{gap}{top:10s}"
        line5=f"{'Name:':20s}{gap}{gap}{name:10s}{gap}{gap}{gap}{'Fare':15s}{gap}{fare:10s}"
        print(line0)
        print('Passenger Ticket')
        print(line1)
        print(line4)
        print(line5)
        print("-"*93)
    def op5_3():
        from datetime import date
        today=date.today()
        datet=str(today)   
        rd=datet[8:]+'/'+datet[5:7]+'/'+datet[2:4]
        f=open(pname+'.csv','r')
        fln53=input("Enter flight number:")
        a=csv.reader(f)
        f1=open('Aircraft.csv','r')
        b=csv.reader(f1)
        gap=' '*3
        sgap=' '
        heading=f"{'Seat No':10s}{gap}{'Name':15s}{gap}{gap}{gap}{'Age':3s}{gap}{gap}{'Destination':15s}{gap}{'PNR':5s}{gap}{'Status':5s}"
        for i in b:
            aircraft=i[1]
            departt=i[5]
        line1=f"{'Flight Number':15s}{gap}{fln53:10s}{gap}{gap}{gap}{gap}{'Date of Journey':20s}{gap}{rd:20s}"
        line2=f"{'Aircraft':15s}{gap}{aircraft:10s}{gap}{gap}{gap}{gap}{'Departure Time':20s}{gap}{departt:20s}"
        print("-"*93)
        print('                                Air Goes International Airlines                                    ')
        print('Reservation Chart')
        print(line1)
        print(line2)
        print("-"*93)
        print(heading)
        recwl=[]
        for i in a:
            if i[0]=='Fl_No':
                continue
            elif i[0]==fln53 and i[11].upper()=='C':
                rec=f"{i[2]:10s}{gap}{i[5]:15s}{gap}{gap}{gap}{i[6]:3s}{gap}{gap}{i[4]:15s}{gap}{i[1]:5s}{gap}{i[11]:5s}"
                print(rec)
            elif i[0]==fln53 and i[11].upper()=='W':
                recw=f"{i[2]:10s}{gap}{i[5]:15s}{gap}{gap}{gap}{i[6]:3s}{gap}{gap}{i[4]:15s}{gap}{i[1]:5s}{gap}{i[11]:5s}"
                recwl+=[recw]
        Blank=f"{':':10s}{gap}{':':15s}{gap}{gap}{gap}{':':3s}{gap}{gap}{':':15s}{gap}{':':5s}{gap}{':':5s}"
        print(Blank)
        for i in recwl:
            print(i)
        print("-"*93)
        f.close()
        f1.close()
    menureport='''
1.Reservation Slip
2.Passenger Ticket
3.Reservation Chart
0.Exit
'''
    while True:
        print(menureport)
        op=input("Enter an option:")
        if op=='1':
            op5_1()
        elif op=='2':
            op5_2()
        elif op=='3':
            op5_3()
        elif op=='0':
            break
        else:
            print('Invalid input!')
def op6():
    fln33=input("Enter flight number:")
    name=input('Enter name:')
    found=0
    f1=open(pname+'.csv','r')
    f1.close()
    import os
    pnname=pname+'1'
    with open(pname+'.csv','r+') as old, open(pnname+'.csv','w+',newline='') as new:
        writer=csv.writer(new)
        pnr=0
        l1old=[]
        for i in csv.reader(old):
            l1old.append(i)
            pnr+=1
        pnr=pnr-1
        for i in l1old:
            if i[0].upper()==fln33.upper() and i[5].upper()==name.upper() and i[11].upper()=='W':
                input33=10
                newrow=[]
                for j in i:
                    index=i.index(j)
                    if index==11:
                        newrow.append('C')
                    elif index==1:
                        newrow.append(pnr)
                    else:
                        newrow.append(j)
                writer.writerow(newrow)
            else:
                writer.writerow(i)
    new.close()
    old.close()
    os.remove(pname+'.csv')
    os.rename(pnname+'.csv',pname+'.csv')
    if fln33.upper()==i[0].upper() and name.upper()==i[5].upper() and i[11].upper()=='W':
        found=1
    if found==0:
        print('Invalid Flight Number or Flight or Flight is already confirmed!')
        prompt31=input("Do you wanna go back or try again?(B/T)")
        if prompt31=='B':
                main()
        elif prompt31=='T':
            op6()
        else:
            print('Invalid Input')
            prompt31=input("Do you wanna go back or try again?(B/T)")
def op7():
    fln33=input("Enter flight number:")
    name=input('Enter name:')
    found=0
    f1=open(pname+'.csv','r')
    f1.close()
    import os
    pnname=pname+'1'
    with open(pname+'.csv', 'r+') as old, open(pnname+'.csv', 'w+',newline='') as new:  
        writer=csv.writer(new)
        #pnr=len(csv.reader(old))-1
        for i in csv.reader(old):
            if i[0].upper()==fln33.upper() and i[5].upper()==name.upper() and i[11].upper()=='W':
                found=1
                pass
            else:
                writer.writerow(i)
    new.close()
    old.close()
    os.remove(pname+'.csv')
    os.rename(pnname+'.csv',pname+'.csv')
    if found==0:
        print('Invalid Flight Number or Flight or Flight is already confirmed!')
        prompt31=input("Do you wanna go back or try again?(B/T)")
        if prompt31=='B':
                main()
        elif prompt31=='T':
            op6()
        else:
            print('Invalid Input')
            prompt31=input("Do you wanna go back or try again?(B/T)")
    else:
        print("Your flight is cancelled")
    import os
    fnname=fname+'1'
    with open(fname+'.csv','r+') as old, open(fnname+'.csv','w+',newline='') as new:   
        writer=csv.writer(new)
        for i in csv.reader(old):
            if i[0]==fln33.upper():
                newrow=[i[0],int(i[1])-1]
                writer.writerow(newrow)
            else:
                writer.writerow(i)
    new.close()
    old.close()
    os.remove(fname+'.csv')
    os.rename(fnname+'.csv', fname+'.csv')
def main():
    while True:
        print(menu)
        op=input("Enter an option:")
        if op=='1':
            op1()
        elif op=='2':
            op2()
        elif op=='3':
            op3()
        elif op=='4':
            op4()
        elif op=='5':
            op5()
        elif op=='6':
            op6()
        elif op=='7':
            op7()
        elif op=='0':
            break
        else:
            print('Invalid input!')
main()
