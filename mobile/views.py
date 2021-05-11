from django.shortcuts import render, redirect
from .models import Product, Order, Cart
from .forms import CreateProductForm, UserRegistrationForm, LoginForm, OrderForm, CartForm
from django.contrib.auth import authenticate, login, logout
from .decorators import login_required, admin_only

# Create your views here.

@login_required
def index(request):
    return render(request, "mobile/base.html")

@admin_only
def index_admin(request):
    return render(request, "mobile/adminbase.html")


@login_required
def list_mobiles(request):
    mobiles = Product.objects.all()
    context = {}
    context = {"mobiles": mobiles}
    return render(request, "mobile/listmobiles.html", context)

@admin_only
def admin_mobile_list(request):
    mobiles=Product.objects.all()
    context={}
    context['mobiles']=mobiles
    return render(request,'mobile/adminlist.html',context)

@admin_only
def add_product(request):
    form = CreateProductForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CreateProductForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "mobile/createmobile.html", context)


def get_mobile_object(id):
    return Product.objects.get(id=id)

@login_required
def mobile_detail(request, id):
    mobile = get_mobile_object(id)
    context = {}
    context["mobile"] = mobile
    return render(request, "mobile/mobiledetail.html", context)

@admin_only
def admin_mobile_details(request,id):
    mobile=get_mobile_object(id)
    context={}
    context['mobile']=mobile
    return render(request,'mobile/adminmobiledetail.html',context)

@admin_only
def mobile_delete(request, id):
    mobile = get_mobile_object(id)
    mobile.delete()
    return redirect("index")

@admin_only
def update(request, id):
    mobile = get_mobile_object(id)
    form = CreateProductForm(instance=mobile)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CreateProductForm(instance=mobile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "mobile/mobileupdate.html", context)


def registration(request):
    form = UserRegistrationForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "mobile/login.html")
        else:
            form = UserRegistrationForm(request.POST)
            context["form"] = form
            return redirect("userlogin")
    return render(request, "mobile/register.html", context)


def login_user(request):
    context = {}
    form = LoginForm()
    context["form"] = form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if not user.is_superuser:
                    return render(request, "mobile/base.html")
                else:
                    return render(request,"mobile/adminbase.html")
    return render(request, "mobile/login.html", context)


def signout(request):
    logout(request)
    return redirect("userlogin")

def order(request,id):
    prod=get_mobile_object(id)
    form=OrderForm(initial={'user':request.user,'product': prod})
    context={}
    context["form"]=form
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listmobiles")
        else:
            context["form"]=form
            return render(request, "mobile/orderitem.html", context)
    return render(request,"mobile/orderitem.html",context)


def view_my_orders(request):
    orders=Order.objects.filter(user=request.user)
    context={}
    context["orders"]=orders
    return render(request,"mobile/vieworder.html",context)

def cancel_order(request,id):
    order=Order.objects.get(id=id)
    order.status='Cancelled'
    order.save()
    return redirect("vieworder")



@login_required
def add_to_cart(request,id):
    prod = get_mobile_object(id)
    form = CartForm(initial={'user': request.user, 'product': prod})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listmobiles")
        else:
            context["form"] = form
            return render(request, "mobile/mobiledetail.html", context)
    return render(request, "mobile/cartitem.html", context)

@login_required
def view_cart(request):
    cart_items=Cart.objects.filter(user=request.user)
    context={}
    context["cart_items"]=cart_items
    return render(request,"mobile/cartview.html",context)

@login_required
def remove_cart_item(request,id):
    carts = Cart.objects.get(id=id)
    carts.delete()
    return redirect('viewcart')