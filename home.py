from flask import  Flask ,render_template ,request ,redirect ,url_for,flash
from backend import *
app=Flask(__name__)



@app.route("/",methods=["POST","GET"])
def home():
	if request.method=="POST":
		x=request.form["Uname"]
		y=request.form['Pass']
		if x==y and x=="admin":
			# Admin login
			return render_template('adminsection.html')
		else:
			# Check if user exist
			data=viewmoderator()
			for lst in data:
				if str(lst[0])==str(x) and str(lst[2])==str(y):
					return render_template('moderator_section.html',mode=x)

			return render_template('index.html',status="error")
	return render_template('index.html',status='get')


@app.route('/addsubject',methods=["POST","GET"])
def add_subject():
	lst=viewdatastud()
	if request.method=="POST":
		usn=request.form['mod_del']
		sub1=request.form['inputname']
		sub2=request.form['num']
		sub3=request.form['nu']
		back=request.form['pe']
		try:
			addsubject(usn,sub1,sub2,sub3,back)
			return render_template('/addsubject.html',status="ok",data=lst,lenght=len(lst))
		except Exception as e:
			return render_template('/addsubject.html',status="error",data=lst,lenght=len(lst))

	return render_template('/addsubject.html',status="",data=lst,lenght=len(lst))

@app.route('/add_student',methods=["POST","GET"])
def add_student():
	print(viewmoderator(),"\n\n\n\n\n\n\n")
	if request.method=="POST":
		usn=request.form['usnno']
		name=request.form['inputname']

		# paswd=request.form['exampleInputPassword1']
		add=request.form['add']
		mail=request.form['exampleInputEmail1']
		phone=request.form['num']
		if len(str(phone))!=10:
			return render_template('add_student.html',status="Phone")

		print(request.form)
		add=request.form['add']
		mail=request.form['exampleInputEmail1']
		phone=request.form['num']
		print(usn,name,add,mail,phone)

		try:
			addstdrec(usn,name,phone,add,mail)
			return render_template('add_student.html',status="ok")
		except Exception as e:

			print("check1**********************************************")

			print("check1**********************************************",e)

			return render_template('add_student.html',status="error")

	return render_template('add_student.html',status="")
	
@app.route('/add_moderator',methods=["POST","GET"])
def moderator():

	if request.method=="POST":
		idd=request.form['mod_id']
		name=request.form['Inputname']
		paswd=request.form['exampleInputPassword1']
		email=request.form['exampleInputEmail1']
		phone=request.form['num']
		print(type(phone),"****************************")
		if len(str(phone))!=10:
			return render_template('add_mod.html',msg="phone")
		try:
			addmoderator(idd,name,paswd,str(email),phone)
			return render_template('add_mod.html',msg="success")
		except Exception as e:
			print(e,"========================================")

			
			return render_template('add_mod.html',msg="error")

		
		print(viewmoderator())


	return render_template('add_mod.html',msg="GET")


@app.route('/addfeedetails',methods=["POST","GET"])
def add_fee_details():
	lst=viewdatastud()

	if request.method=="POST":
		usn=request.form['usnno']
		ammt=int(request.form['inputname'])
		sts=request.form['num']
		date=request.form['add']
		penalty=request.form['pe']

		try:
			addfeedetails(usn,int(ammt),sts,str(date),penalty)
			print(type(usn),type(ammt),type(sts),type(date),type(penalty))
			return render_template('addfeedetails.html',status="success",data=lst,lenght=len(lst))

		except Exception as e:
			print(type(usn),type(ammt),type(sts),type(date),type(penalty))
			print(e,"============================")
			return render_template('addfeedetails.html',status="error",data=lst,lenght=len(lst))

			
	return render_template('addfeedetails.html',status="get",data=lst,lenght=len(lst))


@app.route('/update',methods=['GET','POST'])
def update():
	lst=viewdatastud()
	try:
		usn=request.form['usnno']
		iat1=request.form['num1']
		iat2=request.form['num2']
		iat3=request.form['num3']
		ex=int(request.form['ex'])
		avg=(int(iat1)+int(iat2)+int(iat3))
		# avg=0
		print(ex,avg)
		# avg//=3
		total=0
		print("testing2=========")
	
		updatemark(usn,int(iat1),int(iat2),int(iat3),int(ex),int(avg),int(total))
		return render_template('addmarks.html',status='success',data=lst,lenght=len(lst))
		
	except Exception as e:
		print("Exception:",e)
	else:
		return render_template('addmarks.html',status="error",data=lst,lenght=len(lst))
		



@app.route('/add_marks',methods=["POST","GET"])
def addmarks():
	lst=viewdatastud()
	if request.method=="GET":
		return render_template('addmarks.html',status="get",data=lst,lenght=len(lst))

	print("testing==========")
	try:
		usn=request.form['usnno']
		iat1=request.form['num1']
		iat2=request.form['num2']
		iat3=request.form['num3']
		ex=int(request.form['ex'])
		avg=(int(iat1)+int(iat2)+int(iat3))
		# avg=0
		print(ex,avg)
		# avg//=3
		total=0
		print("testing2=========")
	
		addmark(usn,int(iat1),int(iat2),int(iat3),int(ex),int(avg),int(total))
		return render_template('addmarks.html',status='success',data=lst,lenght=len(lst))
		
	except Exception as e:
		print("Exception:",e)
	else:
		return render_template('addmarks.html',status="error",data=lst,lenght=len(lst))
		



	# return render_template('addmarks.html',status="POST",data=lst,lenght=len(lst))
	


@app.route('/moderator_section',methods=["POST","GET"])
def modesection():
	nam="Moderator"
	if request.method=="POST":
		nam=str(request.form['Uname'])
	return render_template('moderator_section.html',mode=nam)



@app.route('/performance')
def performance():
	lst=check_marks()
	return render_template('performance.html',data=lst,lenght=len(lst))

@app.route('/view_data')
def view_stud():
	return render_template('view.html')



# @app.route('/temp')
# def temp_std_data():
# 	return redirect(url_for('view_std_data',flag="del"))



@app.route('/view_std_data',methods=["POST","GET"])
def view_std_data():
	
	if request.method=="POST":
		print(request.form)
		usn=request.form['usn_del']
		deletestdrec(usn)
	lst=viewdatastud()
	return render_template('view_std_data.html',data=lst,lenght=len(lst))

	print("**********************************")
	

@app.route('/viewmoddata',methods=["POST","GET"])
def view_mod_data():
	# print("check1==================================",viewmoderator())

	if request.method=="POST":
		mod=request.form['mod_del']
		print(mod,"==============")
		deleterecmoderator(mod)

		
	lst=viewmoderator()
	return render_template('view_mod.html',data=lst,lenght=len(lst))

	

@app.route('/view_sub_data')
def view_subject():
	lst=viewsubject()
	return render_template('view_subject.html',data=lst,lenght=len(lst))


@app.route('/score')
def score():
	return render_template('scores.html')

@app.route('/view_fees_details')
def view_fees():
	lst=viewfeedetails()
	return render_template('view_fees.html',data=lst,lenght=len(lst))


# @app.route('/viewdata',methods=["POST","GET"])
# def view():
# 	return f"<h1>{viewmoderator()}</h1>"
# @app.route("/<usr>",methods=["POST","GET"])
# def user(usr):
# 	print("ok",usr)
# 	return  f"<h1>Welcome :{usr}</h1>"


app.run(debug=True)