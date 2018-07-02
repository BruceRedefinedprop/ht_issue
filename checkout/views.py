from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe


"""
Defined user checkout function.   The system relies on Stripe for Credit Card
processing.

The main checkout functions are: 
a. if order form and payment forms are valid, saves the order in database
b. process credit card, if valid excepts payment.  If not rejects credit card
c. If view function is responding a get, display blank forms.


"""


# stripe key is env.py file.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        # complete forms returned
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        # check if returned forms are valid
        if order_form.is_valid() and payment_form.is_valid():
            # create an instance of an order and save it memory, add a date then save to disk.
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            # Get cart from session - context defined in context.py
            cart = request.session.get('cart', {})
            total = 0
            # build order_line records for database and associate with Order
            # order can have many line items - one to many relationship.
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()
            # try to charge the customer's credit card via stripe
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "USD",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            #  if card rejected by Stripe
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            # send message if card accepted. Return to products page. 
            # customer is stripe object.
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        # if new html page, create blank forms
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
                
            