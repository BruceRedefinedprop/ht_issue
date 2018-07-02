from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")
    
# add item to cart context    
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity=int(request.POST.get('quantity'))
    #retrieve cart context object
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    #reset cart values
    request.session['cart'] = cart
    return redirect(reverse('index'))
    
    
def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    # .... add check, for quantity being a interger.  If not set quantity to zero....
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    # readjust cart quantity
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    #reset cart value and show shopping cart.    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))