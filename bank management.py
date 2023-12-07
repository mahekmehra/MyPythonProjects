import mysql.connector
mydb= mysql.connector.connect(user='root',passwd='yoursqlpassword',host='localhost',database='BankDB')
mycursor=mydb.cursor(buffered=True)

#to create new database(if not exists)
#mycursor.execute('create database BankDB')

def menu():
    print('*'*160)
    print(' '*20,'MAIN MENU')
    print(' '*20,'1. Insert Record(s)')
    print(' '*20,'2. Display Records as per A/C no.')
    print(' '*20,'     a. Sorted by A/C no.')
    print(' '*20,'     b. Sorted by Customer Name')
    print(' '*20,'     c. Sorted by Customer Balance')
    print(' '*20,'3. Search Record details as per the A/C no.')
    print(' '*20,'4. Update Record')
    print(' '*20,'5. Delete Record')
    print(' '*20,'6. Transactions Withdraw/Debit from the account')
    print(' '*20,'     a. Withdraw/Debit from the account')
    print(' '*20,'     b. Credit into the account')
    print(' '*20,'7. Exit')
    print('*'*160)

def menusort():
    print(' '*20,'2. Display Records as per A/C no.')
    print(' '*20,'     a. Sorted by A/C no.')
    print(' '*20,'     b. Sorted by Customer Name')
    print(' '*20,'     c. Sorted by Customer Balance')
    print(' '*20,'     d. Back')

def menutransaction():
    print(' '*20,'     a. Withdraw/Debit from the account')
    print(' '*20,'     b. Credit into the account')
    print(' '*20,'     c. Back')

def create():
    try:
        mycursor.execute('create table bank(ACCNO varchar(10),NAME varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20),CITY varchar(10),COUNTRY varchar(10),BALANCE varchar(10))' )
        print('Table Created')
        insert()
    except:
        print('Table Exist')
        insert()

def insert():
    while True :
        acc=input('Enter account no :')
        name=input('Enter name :')
        mob=input('Enter mobile :')
        email=input('Enter email :')
        add=input('Enter address :')
        city=input('Enter city :')
        country=input('Enter country :')
        bal=float(input('Enter Balance :'))
        rec=[acc,name.upper(),mob,email.lower(),add.upper(),city.upper(),country.upper(),bal]
        cmd='insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(cmd,rec)
        mydb.commit()
        ch=input('Do you want to enter more records(N/Y) :')
        if ch=='N' or ch=='n':
            break 
def dispsortacc():
    try:
        cmd='select * from Bank order by ACCNO'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('ACCN0','NAME','MOBILE','EMAIL ADDRESS','HOME ADRESS','CITY','COUNTRY','BALANCE'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*125)
    except:
        print("Table doesn't exist")

def dispsortname():
    try:
        cmd='select * from Bank order by NAME'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('ACCN0','NAME','MOBILE','EMAIL ADDRESS','HOME ADRESS','CITY','COUNTRY','BALANCE'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*125)
    except:
        print("Table doesn't exist")

def dispsortbalance():
    try:
        cmd='select * from Bank order by BALANCE'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('ACCN0','NAME','MOBILE','EMAIL ADDRESS','HOME ADRESS','CITY','COUNTRY','BALANCE'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*125)
    except:
        print("Table doesn't exist")

def dispsearchacc():
    try:
        cmd='select * from bank'
        mycursor.execute(cmd)
        ch=input('Enter the A/C no to be searched :')
        for i in mycursor:
            if i[0]==ch:
                F='%15s %15s %15s %15s %15s %15s %15s %15s'
                print(F % ('ACCN0','NAME','MOBILE','EMAIL ADDRESS','HOME ADRESS','CITY','COUNTRY','BALANCE'))
                print('='*125)
                for j in i:
                    print('%14s' % j, end=' ')
                print()
                break
        else:
            print('record not found')
    except:
        print("Table doesn't exist")

def update():
    try:
        cmd='select * from bank'
        mycursor.execute(cmd)
        A=input('Enter the account no whose details to be changed :')
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                ch=input('Change Name(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[1]=input('Enter Name :')
                    i[1]=i[1].upper()
                ch=input('Change Mobile Number(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[2]=input('Enter Number :')
                ch=input('Change Email(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[3]=input('Enter Email :')
                    i[3]=i[3].lower()
                ch=input('Change Address(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[4]=input('Enter Address :')
                    i[4]=i[4].upper()
                ch=input('Change City(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[5]=input('Enter City :')
                    i[5]=i[5].upper()
                ch=input('Change Country(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[6]=input('Enter Country :')
                    i[6]=i[6].upper()
                ch=input('Change Balance(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[7]=float(input('Enter Balance :'))
                cmd='update bank set NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s where ACCNO=%s'
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated")
                break
        else:
            print("Record not found")
    except:
        print('No such table')

def delete():
    try:
        cmd='select * from BANK'
        mycursor.execute(cmd)
        A=input("Enter the A/C no whose details to be deleted :")
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                cmd='delete from bank where ACCNO=%s'
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print('Account Deleted')
                break
        else:
            print('Record not found')
    except:
        print('No such Table')

def debit():
    try:
        cmd="select * from bank"
        mycursor.execute(cmd)
        print("Please note that the money can only be debited if min balance of Rs 500 exists")
        acc=input("Enter the account no from which the money is to be debited :")
        for i in mycursor:
            i=list(i)
            if i[0]==acc:
                amt=float(input("Enter the amount to be withdrawn :"))
                if i[7]-amt>=500:
                    i[7]-=amt
                    cmd='update bank set BALANCE=%s where ACCNO=%s'
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print('Amount Debited')
                    break
                else:
                    print('There must be min balance of Rs 500')
                    break
        else:
            print('Record not found')
        
def credit()
    try:
    cmd='select * from bank'
        mycursor.execute(cmd)
        acc=input("Enter the account no from which the money is to be credited :")
        for i in mycursor:
            i=list(i)
            if i[0]==acc:
                amt=float(input("Enter the amount to be credited :"))
                i[7]+=amt
                cmd='update bank set BALANCE=%s where ACCNO=%s'
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Amount Credited")
                break
        else:
            print('Record not found')

#MAIN PROGRAM...

while True:
    menu()
    ch=input("Enter your choice :")
    if ch=='1':
        create()
    elif ch=='2':
        while True:
            menusort()
            ch1=input('Enter choice a/b/c/d :')
            if ch1 in ['a','A']:
                dispsortacc()
            elif ch1 in ['b','B']:
                dispsortname()
            elif ch1 in ['c','C']:
                dispsortbalance()
            elif ch1 in ['d','D']:
                print('Back to the main menu')
                break
            else:
                print('Invalid Choice')
    elif ch=='3':
        dispsearchacc()
    elif ch=='4':
        update()
    elif ch=='5':
        delete()
    elif ch=='6':
        while True:
            menutransaction()
            ch1=input('Enter choice a/b/c :')
            if ch1 in ['a','A']:
                debit()
            elif ch1 in ['b','B']:
                credit()
            elif ch1 in ['c','C']:
                print('Back to main menu')
                break
            else:
                print('Invalid choice')
    elif ch=='7':
        print('Exiting...')
        break
    else:
        print('Wrong Choice Entered')

        
                    
  






















