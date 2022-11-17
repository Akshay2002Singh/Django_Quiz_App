from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from home.models import contact,quiz_question,quiz_submissions
import json
import random

# Create your views here.
def index(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,'index.html',context)

def login_user(request):
    return render(request,'login.html')

def login_form(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password= password)
        if user is not None:
            login(request,user)
            return redirect ("/")
        else:
            return redirect("/login")

def create_user(request):
    return render(request,"sign_up.html")

def create_user_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username,email,password)
        user.first_name=name
        user.save()
        return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect("/")

def contact_us(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,"contact_us.html",context)

def submit_contact_form(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        temp_contact = contact(name=name,email=email,phone=phone,message=message)
        temp_contact.save()

        return render(request,'contact_us.html',context)

def add_question(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    
    return render(request,"add_question.html",context)

def add_question_form(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
        context["msg"]="Question Added"

    if request.method == "POST":
        Question = request.POST.get('Question')
        option_1 = request.POST.get('option_1')
        option_2 = request.POST.get('option_2')
        option_3 = request.POST.get('option_3')
        option_4 = request.POST.get('option_4')
        answer = request.POST.get('answer')
        id = quiz_question.objects.all().count()
        temp_question = quiz_question(question_id=id,question=Question,option_1=option_1,option_2=option_2,option_3=option_3,option_4=option_4,answer=answer)
        temp_question.save()

        return render(request,'add_question.html',context)
    
def attempt_quiz(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()

    t_check = quiz_submissions.objects.filter(username=request.user.get_username())
    if(t_check):
        # print("user exist")
        user_data = quiz_submissions.objects.get(username=request.user.get_username())
        t_remain = json.loads(user_data.remain)
        if(len(t_remain)==0):
            return render(request,"done_quiz.html",context)
        q_id = random.choice(t_remain)
        question_data = quiz_question.objects.get(question_id=q_id)
        print(question_data.question)
        context["question"] = question_data

    else:
        # print("user not exist")
        total_questions = quiz_question.objects.all().count()
        remaining = [i for i in range(total_questions)]
        remaining = json.dumps(remaining)
        ans = {}
        ans = json.dumps(ans)
        t_entry = quiz_submissions(username=request.user.get_username(),remain=remaining,my_ans=ans,score=0)
        print(t_entry)
        t_entry.save()
        return redirect('/attempt_quiz')
    
    return render(request,"attempt_quiz.html",context)
    # return redirect("/")

def submit_question(request):
    if request.method == "POST":
        user_ans = request.POST.get('my_ans')
        q_id = request.POST.get('id')
        q_id = int(q_id)
        question = quiz_question.objects.get(question_id=q_id)
        # print(user_ans == question.answer)

        # modifing userdata of submissions table 
        user_data = quiz_submissions.objects.get(username=request.user.get_username())
        t_remain = json.loads(user_data.remain)
        t_remain.remove(q_id)
        t_ans = json.loads(user_data.my_ans)
        t_ans[q_id] = user_ans
        t_score = user_data.score
        if(user_ans == question.answer):
            t_score+=1

        quiz_submissions.objects.filter(username=request.user.get_username()).update(remain=json.dumps(t_remain),score=t_score,my_ans=json.dumps(t_ans))
    
        
    return redirect('/attempt_quiz')

def result(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    
    result = quiz_submissions.objects.all()
    context["users"] = result.order_by('-score').values()
    
    return render(request,"result.html",context)

