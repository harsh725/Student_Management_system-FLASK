import sqlite3
def studentData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student(usn INTEGER PRIMARY KEY,
        name TEXT,
        mobileno INTEGER,
        address TEXT,
        email TEXT)""")
    con.commit()
    con.close()

def addstdrec(usn,name,mobileno,address,email):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO student VALUES (:usn,:name,:mobileno,:address,:email)""",{'usn':usn,'name':name,'mobileno':mobileno,'address':address,'email':email})
    con.commit()
    con.close()

def viewdatastud():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    con.close()
    return rows


def deletestdrec(usn):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("DELETE FROM student WHERE usn=:usn",{'usn':usn})
    con.commit()
    con.close()


def updatestddata(usn,name,mobileno,address,email):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("UPDATE student SET name=:name,mobileno=:mobileno,address=:address,email=:email WHERE usn=:usn",{'name':name,'mobileno':mobileno,'address':address,'email':email,'usn' : usn})
    con.commit()
    con.close()


print(viewdatastud())
def moderatordata():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS moderator(idm INTEGER PRIMARY KEY,
        namem TEXT,
        password TEXT,
        emailm TEXT,
        contactno INTEGER)""")
    con.commit()
    con.close()

moderatordata()

def addmoderator(idm,namem,password,emailm,contactno):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO moderator VALUES (:idm,:namem,:password,:emailm,:contactno)""",{'idm':idm,'namem':namem,'password':password,'emailm':emailm,'contactno':contactno})
    con.commit()
    con.close()

addmoderator(1,"harsh","hd","fk@gmail.com",111)
addmoderator(2,"gsgg","kl","fs@gmail.com",21)

def viewmoderator():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM moderator")
    rows=cur.fetchall()
    con.close()
    return rows
def deleterecmoderator(idm):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM moderator WHERE idm=:idm",{'idm':idm})
     con.commit()
     con.close()



def updaterecmoderator(idm,namem,password,emailm,contactno):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("UPDATE moderator SET namem=:namem,password=:password,emailm=:emailm,contactno=:contactno WHERE idm=:idm",{'namem':namem,'password':password,'emailm':emailm,'contactno':contactno,'idm':idm})
     con.commit()
     con.close()

print(viewmoderator())



def feedata():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS fee(usn INTEGER PRIMARY KEY,
    amount INTEGER,
    status TEXT,
    date DATE,
    penalty TEXT)""")
    con.commit()
    con.close()


def addfeedetails(usn,amount,status,date,penalty):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("""INSERT INTO fee VALUES (:usn,:amount,:status,:date,:penalty)""",{'usn':usn,'amount':amount,'status':status,'date':date,'penalty':penalty})
     con.commit()
     con.close()

def viewfeedetails():
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("SELECT * FROM fee")
     rows=cur.fetchall()
     con.close()
     return rows



def deletefeerec(usn):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM fee WHERE usn=:usn",{'usn':usn})
     con.commit()
     con.close()

 
def updatefeerec(usn,amount,status,date,penalty):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("UPDATE fee SET amount=:amount,status=:status,date=:date,penalty=:penalty WHERE usn=:usn",{'amount':amount,'status':status,'date':date,'penalty':penalty,'usn':usn})
     con.commit()
     con.close()



def subjectdata():
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("""CREATE TABLE IF NOT EXISTS subject(usn INTEGER PRIMARY KEY,
     sub1 TEXT,
     sub2 TEXT,
     sub3 TEXT,
     backlogs TEXT)""")
     con.commit()
     con.close()


def addsubject(usn,sub1,sub2,sub3,backlogs):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("""INSERT INTO subject VALUES (:usn,:sub1,:sub2,:sub3,:backlogs)""",{'usn':usn,'sub1':sub1,'sub2':sub2,'sub3':sub3,'backlogs':backlogs})
     con.commit()
     con.close()

def viewsubject():
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("SELECT * FROM subject")
     rows=cur.fetchall()
     con.close()
     return rows

      

def deletesubjectrec(usn):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM subject WHERE usn=:usn",{'usn':usn})
     con.commit()
     con.close()


def updaterecsubject(usn,sub1,sub2,sub3,backlogs):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("UPDATE subject SET sub1=:sub1,sub2=:sub2,sub3=:sub3,backlogs=:backlogs WHERE usn=:usn",{'sub1':sub1,'sub2':sub2,'sub3':sub3,'backlogs':backlogs,'usn':usn})
     con.commit()
     con.close()



def performancedata():
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("""CREATE TABLE IF NOT EXISTS performance(usn INTEGER PRIMARY KEY,
     iat1 INTEGER,
     iat2 INTEGER,
     iat3 INTEGER,
     AVG REAL,
     external REAL,
     total INTEGER)""")
     con.commit()
     con.close()


