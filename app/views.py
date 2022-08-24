from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    if request.method =="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        designation = request.POST['designation']
        about = request.POST['about']
        age = request.POST['age']
        address = request.POST['address']
        language = request.POST['language']
        skill1 = request.POST['skill1']
        range1 = request.POST['range1']
        skill2 = request.POST['skill2']
        range2 = request.POST['range2']
        skill3 = request.POST['skill3']
        range3 = request.POST['range3']
        skill4 = request.POST['skill4']
        range4 = request.POST['range4']
        company1 = request.POST['company1']
        duration1 = request.POST['duration1']
        role1 = request.POST['role1']
        role_desc1 = request.POST['role_desc1']
        company2 = request.POST['company2']
        duration2 = request.POST['duration2']
        role2 = request.POST['role2']
        role_desc2 = request.POST['role_desc2']
        company3 = request.POST['company3']
        duration3 = request.POST['duration3']
        role3 = request.POST['role3']
        role_desc3 = request.POST['role_desc3']
        degree1 = request.POST['degree1']
        degree2 = request.POST['degree2']
        degree3 = request.POST['degree3']
        course_duration1 = request.POST['course_duration1']
        course_duration2 = request.POST['course_duration2']
        course_duration3 = request.POST['course_duration3']
        course1 = request.POST['course1']
        course2 = request.POST['course2']
        course3 = request.POST['course3']
        university1 = request.POST['university1']
        university2 = request.POST['university2']
        university3 = request.POST['university3']
        course_desc1 = request.POST['course_desc1']
        course_desc2 = request.POST['course_desc2']
        course_desc3 = request.POST['course_desc3']



        education ={'degree1':degree1,'degree2':degree2,'degree3':degree3,'course_duration1':course_duration1,'course_duration2':course_duration2,'course_duration3':course_duration3,'course1':course1,'course2':course2,'course3':course3,'university1':university1,'university2':university2,'university3':university3,'course_desc1':course_desc1,'course_desc2':course_desc2,'course_desc3':course_desc3}


        work= {'company1':company1,'duration1':duration1,'role1':role1,'role_desc1':role_desc1,'company2':company2,'duration2':duration2,'role2':role2,'role_desc2':role_desc2,'company3':company3,'duration3':duration3,'role3':role3,'role_desc3':role_desc3,}


        skill ={'skill1':skill1,'range1':range1,'skill2':skill2,'range2':range2,'range3':range3,'range4':range4,'skill3':skill3,'skill4':skill4}


        data = {'fname':fname,'lname':lname,'email':email,'phone':phone,'designation':designation,'about':about,'age':age,'address':address,'language':language}
        
        print(data)
        content ={'data':data,'skill':skill,'work':work,'education':education}
        return render(request,'resume.html',content)
    return render(request,"home.html")

