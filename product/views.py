from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import uploads


def index(request):
    close_list=Closebid.objects.all()
    all_product = Auction.objects.all()
    return render(request, "user/index.html",{
        'ima' : all_product,
        'ik': close_list,
    })


def watch(request,id):
    comments = comment.objects.filter(listid=id)
    all_product = Auction.objects.filter(id=id)
    return render(request, "user/watch.html",{
        "auctions": all_product,
        "commente": comments,
        "error": request.COOKIES.get('error')
    })


@login_required(login_url='/login')
def upload(request):

    if request.method == 'POST':
        form = uploads(request.POST,request.FILES)
        if form.is_valid():
            ok=form.save(commit=False)
            ok.user=request.user
            ok.save()
            return redirect(index)
    else:
        form = uploads()
        all = Auction.objects.all()
        return render(request,'user/form.html',{
            'form' : form, 'all' : all
        })
    
    
@login_required(login_url='/login')
def watchlist(request,productid):
    obj = watchs.objects.filter(
        auctionh=productid, user=request.user.username)
    if obj:
        obj.delete()
        product = Auction.objects.filter(id=productid)
        added = watchs.objects.filter(
            auctionh=productid, user=request.user.username)
        return HttpResponseRedirect(reverse("index"))

    else:
        obj = watchs()
        obj.user = request.user.username
        obj.auctionh = productid
        obj.save()
        product = Auction.objects.get(id=productid)
        added = watchs.objects.filter(
            auctionh=productid, user=request.user.username)
        return render(request,"user/watchlist.html",{
            "i" : product,
            "added" : added
        })



@login_required(login_url='/login')
def update(request):
    lst = watchs.objects.filter(user=request.user.username)
    # list of products available in WinnerModel
    present = False
    prodlst = []
    i = 0
    if lst:
        present = True
        for item in lst:
            product = Auction.objects.get(id=item.auctionh)
            prodlst.append(product)
    print(prodlst)
    return render(request, "user/cart.html", {
        "product_list": prodlst,
        "present": present
    })


@login_required(login_url='/login')
def bids(request,bidid):
    if request.method == "POST":
        item = Auction.objects.get(id=bidid)
        new = int(request.POST.get('new'))
        if item.bid >= new :
            product = Auction.objects.get(id=bidid)
            response = redirect('watch', id=bidid)
            response.set_cookie('error', 'Bid should be greater than previous one', max_age=3)
            return response
        else:
            item.bid = new
            item.save()
            bids = Bid.objects.filter(id=bidid)
            if bids:
                bids.delete()
            k = Bid()
            k.user = request.user.username
            k.title = item.title
            k.id = bidid
            k.Bid = new
            k.save()
            product = Auction.objects.get(id=bidid)
            return redirect('watch', id=bidid)

    else:
        product = Auction.objects.get(id=bidid)
        ok = Bid.objects.filter(id=bidid)
        added = watchlist.objects.filter(
            auctionh=bidid, user=request.user.username)
        return render(request, "user/watch.html", {
            "i": product,
            "added": added,
            "ok":ok
        })
    
@login_required(login_url='/login')

def comments(request,pid):
    if request.method == "POST":
        c = comment()
        c.comments = request.POST.get('commentsa')
        print(c.comments)
        c.user = request.user.username
        c.listid = pid
        c.save()
        return redirect('watch', id=pid)
    else :
        return redirect('index')
    
@login_required(login_url='/login')

def close(request,cid):
    c= Closebid()
    x = Auction.objects.get(id=cid)
    bids = Bid.objects.filter(id=cid)

    c.user = request.user.username
    c.listid = x.id
    c.bidprice = x.bid
    c.title = x.title
    c.image1 = x.image
    c.save()
    message = "Bid closed"

    if Auction.objects.filter(id=cid):
        a = Auction.objects.filter(id=cid)
        a.delete()
    if comment.objects.filter(id=cid):
        f= comment.objects.filter(id=cid)
        f.delete()
    return redirect('index')


def win(request,title):
    ok=Bid.objects.filter(title=title)
    print(ok)
    win = Closebid.objects.filter(title=title)
    return render(request, "user/close.html", {
        "ok": ok,
        "winner": win
    })

@login_required
def categories(request):
    return render(request, 'user/categories.html', {
        "categories": choice,
    })





def show_category_listings(request, category):
    return render(request, "user/specfic.html", {
        'ima': Auction.objects.filter(category=category)
    })
