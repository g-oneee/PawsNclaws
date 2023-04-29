from unicodedata import category
from django.shortcuts import render,redirect,HttpResponse
from app.models import Adopt, Product,Order,product_Category,Responses,contact_us,pet_Category,Services,ServiceResponses
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# import modules (chinmay)
from django.shortcuts import render,redirect,HttpResponse
from pyexpat.errors import messages
from pet_adoption import settings
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from json import dumps
from django.views.decorators.csrf import csrf_exempt

from pet_adoption.forms import AdoptForm


# login code
def Master(request):
    return render(request, 'master.html')


def Index(request):
    product = Product.objects.all()
    context = {
        'product' : product,
    }
    return render(request, 'index.html',context)
   


def signup(request):
    if request.method == "POST":
        global username
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']

    if User.objects.filter(username=username):
        messages.error(request, "Username already exist! Please try some other username.")
        return redirect('Index')

    # if User.objects.filter(email=email).exists():
    #         messages.error(request, "Email Already Registered!!")
    #         return redirect('home')

    if len(username) > 20:
        messages.error(request, "Username must be under 20 charcters!!")
        return redirect('signup')

    # if pass1 != pass2:
    #         messages.error(request, "Passwords didn't matched!!")
    #         return redirect('home')

    if not username.isalnum():
        messages.error(request, "Username must be Alpha-Numeric!!")
        return redirect('signup')

    myuser = User.objects.create_user(username, email, pass1, )
    myuser.is_active = False
    myuser.save()

    messages.success(request, "Your account has been succesfully created.")
    # Welcome Email
    subject = "Welcome to pawsnclaws!!"
    message = "Hello !! \n Welcome to pawsnclaws!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n Team Rocket"
    from_email = settings.EMAIL_HOST_USER
    to_list = [myuser.email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)

    # Email Address Confirmation Email
    current_site = get_current_site(request)
    email_subject = "Confirm your Email @ pawsnclaws!!"
    message2 = render_to_string('email_confirmation.html', {

        'name': myuser.username,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token': generate_token.make_token(myuser)
    })
    email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
    )
    email.fail_silently = True
    email.send()
    user = authenticate(username=username, password=pass1)

    if user is not None:
        signin(request, user)
        fname = user.first_name
        # messages.success(request, "Logged In Sucessfully!!")
        dataJSON = dumps("true")

        return render(request, "port.html", {'data': dataJSON})
    else:
        messages.error(request, "Bad Credentials!!")
        return render (request,'index.html')


def login1(request):
    return render(request, 'login.html')


def signin_2(request):
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            dataJSON = dumps("true")
            username = request.user.get_username()
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            dataJSON = dumps("true")
            # return redirect('index.html')
            return redirect('index')
            # return render(request, 'index.html', {'data': dataJSON, 'user': username})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('index.html')

    return redirect('index')
    # return render(request, 'index.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index')

# render prod page
def product_page(request):

    product = Product.objects.all()
    category = product_Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    else:
        product = Product.objects.all()
    context = {
        'product' : product,
        'category': category,
    }
    return render(request,'product.html' , context)


# try html
def product_page2(request):
    product = Product.objects.all()
    context = {
        'product' : product,
    }
    return render(request,'products2.html' , context)



def adopt(request):
    adopt = Adopt.objects.all()
    category = pet_Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
       adopt = Adopt.objects.filter(petCategory=categoryID).order_by('-id')
    else:
        adopt = Adopt.objects.all()
    context = {
        'adopt' : adopt,
        'category': category,
    }
    return render(request,'adopt.html' , context)

def service(request):
    return render(request,'service.html')



def about(request):
    return render(request,'about.html')

def product_details(request,id):
    product1 = Product.objects.get(id=id)
    product2 = Product.objects.all()
    category = product_Category.objects.all()
    context = {
        'product1' : product1,
        'product2' : product2,
        'category': category,

    }
    return render(request,'product_details.html' , context)

def adopt_details(request,id):
    adopt = Adopt.objects.get(id=id)
    context = {
        'adopt' : adopt,
    }
    return render(request,'adopt_details.html' , context)
# cart
@login_required(login_url="/login1")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product")


@login_required(login_url="/login1")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login1")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login1")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login1")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login1")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


# def Order(user, product, price, quantity, image, total):
#     pass


def CheckOut(request):
    if request.method == 'POST':

        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)

        print(cart)
        # print(new_variable)

        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b

            order = Order(
                user=user,
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
            #     # phone = phone,
            #     # address= address,
            #     # first_name= first_name,
            #     # last_name = last_name,
            #     # city = city,
            #     # pincode = pincode,
                total=total,
            )
            order.save()
        request.session['cart'] = {}

        return redirect('index')
    return HttpResponse("this is checkout")


def adopt_page(request):
    adopt = Adopt.objects.all()
    if request.method == 'POST':
        form = AdoptForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            adopt_name = form.cleaned_data.get('name')
            messages.success(request, f'{adopt_name} has been added')
            return redirect('adopt_page')
    else:
        form = AdoptForm()
    context = {
        'adopt': adopt,
        'form': form,
    }
    return render(request,'adopt_page.html',context)




# try html only for trial.

def try1(request):
    adopt = Adopt.objects.all()
    category = pet_Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
       adopt = Adopt.objects.filter(petCategory=categoryID).order_by('-id')
    else:
        adopt = Adopt.objects.all()
    context = {
        'adopt' : adopt,
        'category': category,
    }
    return render(request,'try.html' , context)


# trial ends


# services
def services(request):
    services = Services.objects.all()
    context = {
        'services' :services,
    }
    return render(request,'services.html',context)
    
def Servicesumbit(request):
     if request.method == "POST":
         name = request.POST['name'],
         email=request.POST['email'],
         detailedreq= request.POST['detailedreq'],
         service=request.POST['service'],
         contact_info=request.POST['number'],
         subject= request.POST['subject'],
         from_email = settings.EMAIL_HOST_USER
         objuser2=ServiceResponses.objects.create(name=name,email=email,subject=subject,detailedreq=detailedreq,service=service,contact_info=contact_info)
         objuser2.save()
         send_mail(
         '\n'.join(subject) , 
         '\n'.join(detailedreq) ,
         from_email,
         ['pythontesting5018@gmail.com'],
         fail_silently=False,
         )
         return redirect('index')

# adoption form start
def adoptform(request):
    adopt = Adopt.objects.all()
    context = {
        'adopt' : adopt,
    }
    return render(request,'adoptform.html',context)

def formsubmition(request):
     if request.method == "POST":
         username = request.user.get_username()
         responsibilty = request.POST['responsibilty']
         scaretaker=request.POST['scaretaker']
         lalone=request.POST['lalone']
         firstime=request.POST['firstime']
         petname=request.POST['petname'] 
         adopt = Adopt.objects.get(name=petname)
         from_email = settings.EMAIL_HOST_USER
        #  print(firstime)
        #  print(username)
         adopt.is_available = 'In process'
         adopt.save()
         objuser=Responses.objects.create(username=username,responsibilty=responsibilty,scaretaker=scaretaker,lalone=lalone,firstime=firstime,petname=petname)
         objuser.save()
         send_mail(
        'Adopt request from '+username, 
        'I want to adopt '+petname+' and in my abscence '+scaretaker+' will take care. And during the day my pet will be '+lalone+' hours alone and '+responsibilty+' will be responsible',
        from_email,
        ['pythontesting5018@gmail.com'],
        fail_silently=False,
        )
         return redirect('adopt')

# adoption form end

# blog start

def blog(request):
    return render(request,'blog/blog.html')

def trainpuppy(request):
    return render(request,'blog/trainpuppy.html')
def dognames(request):
    return render(request,'blog/dognames.html')
def catbreed(request):
    return render(request,'blog/catbreed.html')
def dogbreeder(request):
    return render(request,'blog/dogbreeder.html')
def nerdycat(request):
    return render(request,'blog/nerdycat.html')


# blog end


def Search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains = query)
    # product = Product.objects.all()
    context = {
        'product':product,
    }
    return render(request,'search.html',context)


def contact_page(request):
    if request.method=='POST':
        # contact = contact_us(
        #     name = request.POST.get('name'),
        #     email=request.POST.get('email'),
        #     subject= request.POST.get('subject'),
        #     message=request.POST.get('message'),
            

        # )
        name = request.POST.get('name'),
        email=request.POST.get('email'),
        subject= request.POST.get('subject'),
        message=request.POST.get('message'),
        from_email = settings.EMAIL_HOST_USER
        objuser1=contact_us.objects.create(name=name,email=email,subject=subject,message=message)
        objuser1.save()
        send_mail(
       '\n'.join(subject) , 
        '\n'.join(message) ,
        from_email,
        ['pythontesting5018@gmail.com'],
        fail_silently=False,
        )
        # contact.save()

    return render(request,'contact.html')
@csrf_exempt
def success(request):
    if request.method=='POST':
        a = request.POST
        cart = request.session.get('cart')

        request.session['cart'] = {}
        print(cart)
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
    #
    #     # user = Order.objects.filter( payment_id= order_id).first()
    #     # user.paid = True
    #     # user.save()

    return render(request, 'success.html')

# def video(request):
#     return render(request, 'video.html')
#
# def audio(request):
#     return render(request, 'audio.html')
