from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import pymysql

db=pymysql.connect("localhost","root","","dbOnroad")
c=db.cursor()

######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"index.html")
######################################################################
#                           LOAD REGISTRATION PAGE
######################################################################
def commonuser(request):
    """ 
        The function to load registration page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        contact=request.POST["txtContact"]
        email= request.POST["txtEmail"]
        pwd=request.POST["txtPassword"]
        s="insert into tbluser(uName,uContact,uEmail) values('"+name+"','"+contact+"','"+email+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry registration error"
        else:
            s="insert into tbllogin(username,password,utype,status) values('"+email+"','"+pwd+"','user','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry login error"
            else:
                msg="Registration successfull"
            
    return render(request,"commonuser.html",{"msg":msg})
######################################################################
#                           LOAD MECHANIC REGISTRATION PAGE
######################################################################
def commonmechanic(request):
    """ 
        The function to load mechanic registration page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        contact=request.POST["txtContact"]
        email= request.POST["txtEmail"]
        location=request.POST["txtLocation"]
        l1=request.POST["l1"]
        l2=request.POST["l2"]
        pwd=request.POST["txtPassword"]
        s="insert into tblmechanic(mName,mContact,mEmail,mLocation,lat,lon) values('"+name+"','"+contact+"','"+email+"','"+location+"','"+l1+"','"+l2+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry registration error"
        else:
            s="insert into tbllogin(username,password,utype,status) values('"+email+"','"+pwd+"','mechanic','0')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry login error"
            else:
                msg="Registration successfull"
    return render(request,"commonmechanic.html",{"msg":msg})

######################################################################
#                           LOAD LOGIN PAGE
######################################################################
def commonlogin(request):
    """ 
        The function to load login page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where username='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="user"):
                        return HttpResponseRedirect("/userhome")
                    elif(i[2]=="mechanic"):
                        return HttpResponseRedirect("/mechanichome")
                else:
                    msg="You are not authenticated to login"
            else:
                msg=i[1]
        else:
            msg="User doesnt exist"
    return render(request,"commonlogin.html",{"msg":msg})
######################################################################
#                           LOAD ADMIN HOME PAGE
######################################################################
def adminhome(request):
    """ 
        The function to load admin home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"adminhome.html")
######################################################################
#                           LOAD MECHANICS FOR ADMIN
######################################################################
def adminmechanic(request):
    """ 
        The function to load mechanics for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblmechanic where mEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data1=c.fetchall()
    s="select * from tblmechanic where mEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data2=c.fetchall()
    return render(request,"adminmechanic.html",{"data1":data1,"data2":data2})
######################################################################
#                           APPROVE MECHANIC
######################################################################
def adminapproveuser(request):
    """ 
        The function to approve user
        -----------------------------------------------
        Parameters: 
            HTTP request with get parameter
          
        Returns: 
            html page
    """
    msg=""
    mid=request.GET.get("id")
    status=request.GET.get("status")
    s="update tbllogin set status='"+status+"' where username='"+mid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg="Sorry some error occured"
    else:
        return HttpResponseRedirect("/adminmechanic")
    return render(request,"adminmechanic.html",{"msg":msg})
######################################################################
#                           LOAD MECHANICS FOR ADMIN
######################################################################
def adminuser(request):
    """ 
        The function to load mechanics for admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tbluser where uEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data1=c.fetchall()
    return render(request,"adminuser.html",{"data1":data1})
######################################################################
#                     LOAD FEEDBACK
######################################################################
def adminfeedback(request):
    """ 
        The function to load feedback for mechanic
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    
    s1="select tblworkrequest.*,tbluser.*,tblfeedback.feedback,tblmechanic.mName from tblworkrequest,tbluser,tblfeedback,tblmechanic where tblworkrequest.wEmail=tblmechanic.mEmail and tblworkrequest.uEmail=tbluser.uEmail and tblfeedback.workId=tblworkrequest.workId"
    c.execute(s1)
    data=c.fetchall()
    return render(request,"adminfeedback.html",{"data":data})

######################################################################
#                           LOAD MECHANIC HOME
######################################################################
def mechanichome(request):
    """ 
        The function to load mechanic home page
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    s1="select * from tblmechanic where mEmail='"+email+"'"
    c.execute(s1)
    data=c.fetchall()
    if(request.POST):
        name=request.POST["txtName"]
        contact=request.POST["txtContact"]
        email= request.POST["txtEmail"]
        location=request.POST["txtLocation"]
        s="update tblmechanic set mName='"+name+"', mContact='"+contact+"',mLocation='"+location+"' where mEmail='"+email+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Updation successfull"
    c.execute(s1)
    data=c.fetchall()
    return render(request,"mechanichome.html",{"data":data,"msg":msg})
######################################################################
#                     LOAD MECHANIC WORK REQUEST
######################################################################
def mechanicworkrequest(request):
    """ 
        The function to load work request for mechanic
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s1="select tblworkrequest.*,tbluser.* from tblworkrequest,tbluser where tblworkrequest.wEmail='"+email+"' and tblworkrequest.uEmail=tbluser.uEmail and status='Requested'"
    c.execute(s1)
    data=c.fetchall()
    return render(request,"mechanicwork.html",{"data":data})
######################################################################
#                     APPROVE WORK
######################################################################
def mechanicapprovework(request):
    """ 
        The function to approve work request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    wid=request.GET.get("id")
    status=request.GET.get("status")
    s="update tblworkrequest set status='"+ status +"' where workId='"+ wid +"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg="sorry some error occured"
    else:
        return HttpResponseRedirect("/mechanicworkrequest")
    return render(request,"mechanicwork.html",{"msg":msg})
######################################################################
#                     LOAD MECHANIC WORK 
######################################################################
def mechanicwork(request):
    """ 
        The function to load work request for mechanic
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s1="select tblworkrequest.*,tbluser.* from tblworkrequest,tbluser where tblworkrequest.wEmail='"+email+"' and tblworkrequest.uEmail=tbluser.uEmail and status='accepted'"
    c.execute(s1)
    data=c.fetchall()
    return render(request,"mechanicworkdetails.html",{"data":data})
######################################################################
#                     LOAD ALL WORK 
######################################################################
def mechanicallwork(request):
    """ 
        The function to load all work for mechanic
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s1="select tblworkrequest.*,tbluser.* from tblworkrequest,tbluser where tblworkrequest.wEmail='"+email+"' and tblworkrequest.uEmail=tbluser.uEmail"
    c.execute(s1)
    data=c.fetchall()
    return render(request,"mechanicallwork.html",{"data":data})
######################################################################
#                     LOAD FEEDBACK
######################################################################
def mechanicfeedback(request):
    """ 
        The function to load feedback for mechanic
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s1="select tblworkrequest.*,tbluser.*,tblfeedback.feedback from tblworkrequest,tbluser,tblfeedback where tblworkrequest.wEmail='"+email+"' and tblworkrequest.uEmail=tbluser.uEmail and tblfeedback.workId=tblworkrequest.workId"
    c.execute(s1)
    data=c.fetchall()
    return render(request,"mechanicfeedback.html",{"data":data})

######################################################################
#                           LOAD USER HOME
######################################################################
def userhome(request):
    """ 
        The function to load user home page
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    s1="select * from tbluser where uEmail='"+email+"'"
    c.execute(s1)
    data=c.fetchall()
    if(request.POST):
        name=request.POST["txtName"]
        contact=request.POST["txtContact"]
        email= request.POST["txtEmail"]
        s="update tbluser set uName='"+name+"', uContact='"+contact+"' where uEmail='"+email+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Updation successfull"
    c.execute(s1)
    data=c.fetchall()
    return render(request,"userhome.html",{"data":data,"msg":msg})
######################################################################
#                           WORK REQUEST
######################################################################
def userworkrequest(request):
    """ 
        The function to load work request page for user
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        l1=request.POST["l1"]
        l2=request.POST["l2"]
        req=request.POST["txtWork"]
        l11=str(float(l1)+5)
        l12=str(float(l1)-5)
        l21=str(float(l2)+5)
        l22=str(float(l2)-5)

        print(l11,l12,l21,l22)
        # s="select count(*) from tblmechanic where lat > '"+str(l12)+"' and lat<'"+str(l11)+"' and lon> '"+str(l22)+"' and lon<'"+str(l21)+"' and mEmail in(select username from tbllogin where status='1')"
        # s="select count(*) from tblmechanic where (lat between '"+str(l12)+"' and '"+str(l11)+"') and (lon between '"+str(l22)+"' and '"+str(l21)+"') "
        s="SELECT count(*) FROM `tblmechanic` WHERE (lat between %s and %s ) and (lon between %s and %s) and mEmail in(select username from tbllogin where status=1)"%(float(l12),float(l11),float(l22),float(l21))
        print(s)
        c.execute(s)
        i=c.fetchone()
        
        print("*"*100)
        print(i)
        print("*"*100)

        if(i[0]>0):
            s="insert into tblworkrequest (uEmail,wDesc,lat,lon,status) values('"+email+"','"+req+"','"+l1+"','"+l2+"','Requested')"
            c.execute(s)
            db.commit()
            return HttpResponseRedirect("/userchooseworker")
        else:
            msg="Mechanic is not available in this area"
            # msg=s
    return render(request,"userworkrequest.html",{"msg":msg})
######################################################################
#                          CHOOSE WORKER
######################################################################
def userchooseworker(request):
    """ 
        The function to load workers 
        -----------------------------
        Parameters: 
            HTTP request with get parameter
          
        Returns: 
            html page
    """
    s="select * from tblworkrequest where workId in(select max(workId) from tblworkrequest)"
    c.execute(s)
    i=c.fetchone()
    l1=i[3]
    l2=i[4]
    # l11=l1+5
    # l12=l1-5
    # l21=l2+5
    # l22=l2-5
    l11=str(float(l1)+5)
    l12=str(float(l1)-5)
    l21=str(float(l2)+5)
    l22=str(float(l2)-5)
    s="SELECT * FROM `tblmechanic` WHERE (lat between %s and %s) and (lon between %s and %s) and mEmail in(select username from tbllogin where status=1)"%(float(l12),float(l11),float(l22),float(l21))
    print(s)
    c.execute(s)
    d=c.fetchall()
    return render(request,"userworker.html",{"data":d})

######################################################################
#                     BOOK WORKER
######################################################################
def userbookworker(request):
    """ 
        The function to book a worker
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    # email=request.session["email"]
    wemail=request.GET.get("id")
    s="select max(workId) from tblworkrequest"
    c.execute(s)
    i=c.fetchone()
    wid=i[0]
    s="update tblworkrequest set wEmail='"+ str(wemail) +"' where workId='"+ str(wid) +"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg="sorry some error occured"
    else:
        return HttpResponseRedirect("/userwork")
    return render(request,"userworker.html",{"msg":msg})
######################################################################
#                     LOAD USER WORK REQUEST
######################################################################
def userwork(request):
    """ 
        The function to load all workers
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s1="select tblworkrequest.*,tblmechanic.* from tblworkrequest,tblmechanic where tblworkrequest.uEmail='"+email+"' and tblworkrequest.wEmail=tblmechanic.mEmail "
    c.execute(s1)
    data=c.fetchall()
    return render(request,"userwork.html",{"data":data})
######################################################################
#                     LOAD USER WORK REQUEST
######################################################################
def usercompletedwork(request):
    """ 
        The function to load all workers
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s1="select tblworkrequest.*,tblmechanic.* from tblworkrequest,tblmechanic where tblworkrequest.uEmail='"+email+"' and tblworkrequest.wEmail=tblmechanic.mEmail and (tblworkrequest.status='completed' or tblworkrequest.status='partial' or tblworkrequest.status='incomplete')"
    c.execute(s1)
    data=c.fetchall()
    return render(request,"usercompletedwork.html",{"data":data})
######################################################################
#                     USER FEEDBACK
######################################################################
def userfeedback(request):
    """ 
        The function to add feedback of user
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    wid=request.GET.get("id")
    s="select count(*) from tblfeedback where workId='"+wid+"'"
    c.execute(s)
    i=c.fetchone()
    if(i[0]>0):
        msg="Feedback already entered"
        return HttpResponseRedirect("/usercompletedwork")
    if(request.POST):
        feedback=request.POST["txtFeedback"]
        s="insert into tblfeedback(workId,feedback,fdate) values('"+wid+"','"+feedback+"',(select sysdate()))"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            return HttpResponseRedirect("/userallfeedback")
    return render(request,"userfeedback.html",{"msg":msg})
######################################################################
#                     USER ALL FEEDBACK
######################################################################
def userallfeedback(request):
    """ 
        The function to view feedback of user
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblworkrequest.wDesc,tblmechanic.mName,tblfeedback.feedback,tblfeedback.fdate from tblworkrequest,tblfeedback,tblmechanic where tblworkrequest.wEmail=tblmechanic.mEmail and tblworkrequest.uEmail='"+email+"' and tblfeedback.workId=tblworkrequest.workId"
    c.execute(s)
    data=c.fetchall()
    return render(request,"userallfeedback.html",{"data":data})