import mysql.connector
mydb= mysql.connector.connect(user='root',passwd='yoursqlpassword',host='localhost',database='schoolDB')
mycursor=mydb.cursor(buffered=True)

#to create new database(if not exists)
#mycursor.execute('create database schoolDB')

def menu():
    print('*'*160)
    print(' '*20,'MAIN MENU')
    print(' '*20,'1. Insert new records')
    print(' '*20,'2. Display Records as per Regno.')
    print(' '*20,'     a. Sorted by Regno.')
    print(' '*20,'     b. Sorted by Student name')
    print(' '*20,'3. Display Records as per Gender')
    print(' '*20,'     a. Male students')
    print(' '*20,'     b. Female students')
    print(' '*20,'4. Display Records as per Stream')
    print(' '*20,'     a. Science students')
    print(' '*20,'     b. Commerce students')
    print(' '*20,'     c. Arts students') 
    print(' '*20,'5. Search Record details as per the Regno.')
    print(' '*20,'6. Update Record')
    print(' '*20,'7. Delete Record')
    print(' '*20,'8. Exit')
    print('*'*160)

def menusort():
    print(' '*20,'2. Display Records as per Regno.')
    print(' '*20,'     a. Sorted by Regno.')
    print(' '*20,'     b. Sorted by Student name')
    print(' '*20,'     c. Back')

def menugender():
    print(' '*20,'2. Display Records as per Gender')
    print(' '*20,'     a. Male students')
    print(' '*20,'     b. Female students')
    print(' '*20,'     c. Back')

def menustream():
    print(' '*20,'2. Display Records as per Stream')
    print(' '*20,'     a. Science students')
    print(' '*20,'     b. Commerce students')
    print(' '*20,'     c. Arts students')   
    print(' '*20,'     d. Back') 

def create():
    try:
        mycursor.execute('create table school(REGNO varchar(10),NAME varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20),DOB varchar(10),GENDER varchar(10),STREAM varchar(10))')
        print('Table Created')
        insert()
    except:
        print('Table Exist')
        insert()

def insert():
    while True :
        regno=input('Enter registration no :')
        name=input('Enter name :')
        mob=input('Enter mobile :')
        email=input('Enter email :')
        add=input('Enter address :')
        dob=input('Enter date of birth :')
        gender=input('Enter gender M/F:')
        stream=input('Enter stream:')
        rec=[regno,name.upper(),mob,email.lower(),add.upper(),dob,gender.upper(),stream.upper()]
        cmd='insert into school values(%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(cmd,rec)
        mydb.commit()
        ch=input('Do you want to enter more records(N/Y) :')
        if ch=='N' or ch=='n':
            break
        
def dispsortreg():
    try:
        cmd='select * from school order by REGNO'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('REGNO','NAME','MOBILE','EMAIL','ADDRESS','DOB','GENDER','STREAM'))
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
        cmd='select * from school order by NAME'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('REGNO','NAME','MOBILE','EMAIL','ADDRESS','DOB','GENDER','STREAM'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*125)
    except:
        print("Table doesn't exist")

def dispgenmale():
    try:
        cmd='select * from school where GENDER="M" order by REGNO'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('REGNO','NAME','MOBILE','EMAIL','ADDRESS','DOB','GENDER','STREAM'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*125)
    except:
        print("Table doesn't exist")

def dispgenfemale():
    try:
        cmd='select * from school where GENDER="F" order by REGNO'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('REGNO','NAME','MOBILE','EMAIL','ADDRESS','DOB','GENDER','STREAM'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*125)
    except:
        print("Table doesn't exist")

def dispstrscience():
    try:
        cmd='select * from school where STREAM="SCIENCE" order by REGNO'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('REGNO','NAME','MOBILE','EMAIL','ADDRESS','DOB','GENDER','STREAM'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*125)
    except:
        print("Table doesn't exist")

def dispstrcommerce():
    try:
        cmd='select * from school where STREAM="COMMERCE" order by REGNO'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('REGNO','NAME','MOBILE','EMAIL','ADDRESS','DOB','GENDER','STREAM'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*125)
    except:
        print("Table doesn't exist")

def dispstrarts():
    try:
        cmd='select * from school where STREAM="ARTS" order by REGNO'
        mycursor.execute(cmd)
        F='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('REGNO','NAME','MOBILE','EMAIL','ADDRESS','DOB','GENDER','STREAM'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*125)
    except:
        print("Table doesn't exist")
        
               
def dispsearchreg():
    try:
        cmd='select * from school'
        mycursor.execute(cmd)
        ch=input('Enter the REGNO to be searched :')
        for i in mycursor:
            if i[0]==ch:
                F='%15s %15s %15s %15s %15s %15s %15s %15s'
                print(F % ('ACCN0','NAME','MOBILE','EMAIL','ADDRESS','DOB','GENDER','STREAM'))
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
        cmd='select * from school'
        mycursor.execute(cmd)
        A=input('Enter the registration no whose details to be changed :')
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
                ch=input('Change DOB(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[5]=input('Enter date of birth :')
                    i[5]=i[5].upper()
                ch=input('Change Gender(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[6]=input('Enter Gender :')
                    i[6]=i[6].upper()
                ch=input('Change Stream(Y/N) :')
                if ch == 'y' or ch=='Y':
                    i[7]=input('Enter Stream :')
                cmd='update school set NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,DOB=%s,GENDER=%s,STREAM=%s where REGNO=%s'
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Record Updated")
                break
        else:
            print("Record not found")
    except:
        print('No such table')

def delete():
    try:
        cmd='select * from school'
        mycursor.execute(cmd)
        A=input("Enter the REGNO no whose details to be deleted :")
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                cmd='delete from school where REGNO=%s'
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print('Record Deleted')
                break
        else:
            print('Record not found')
    except:
        print('No such Table')

#MAIN PROGRAM...

while True:
    menu()
    ch=input("Enter your choice :")
    if ch=='1':
        create()
    elif ch=='2':
        while True:
            menusort()
            ch1=input('Enter choice a/b/c :')
            if ch1 in ['a','A']:
                dispsortreg()
            elif ch1 in ['b','B']:
                dispsortname()
            elif ch1 in ['c','C']:
                print('Back to the main menu')
                break
            else:
                print('Invalid Choice')
    elif ch=='3':
        while True:
            menugender()
            ch1=input('Enter choice a/b/c :')
            if ch1 in ['a','A']:
                dispgenmale()
            elif ch1 in ['b','B']:
                dispgenfemale()
            elif ch1 in ['c','C']:
                print('Back to the main menu')
                break
            else:
                print('Invalid Choice')
    elif ch=='4':
        while True:
            menustream()
            ch1=input('Enter choice a/b/c/d :')
            if ch1 in ['a','A']:
                dispstrscience()
            elif ch1 in ['b','B']:
                dispstrcommerce()
            elif ch1 in ['c','C']:
                dispstrarts()
            elif ch1 in ['d','D']:
                print('Back to the main menu')    
                break
            else:
                print('Invalid Choice')             
    elif ch=='5':
        dispsearchreg()
    elif ch=='6':
        update()
    elif ch=='7':
        delete()
    elif ch=='8':
        print('Exiting...')
        break
    else:
        print('Wrong Choice Entered')
