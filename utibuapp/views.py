from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Medication, Order, Statement
from django.contrib import messages

@login_required
def place_order(request):
    if request.method == 'POST':
        medication_id = request.POST.get('medication')
        quantity = int(request.POST.get('quantity'))
        medication = Medication.objects.get(pk=medication_id)
        if medication.stock_quantity >= quantity:
            order = Order.objects.create(
                customer=request.user,
                medication=medication,
                quantity=quantity,
                is_confirmed=False,
                is_paid=False
            )
            # Update stock quantity
            medication.stock_quantity -= quantity
            medication.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('order_history')
        else:
            messages.error(request, 'Insufficient stock for the selected medication.')
    medications = Medication.objects.all()
    return render(request, 'place_order.html', {'medications': medications})

@login_required
def order_history(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def statement(request):
    statements = Statement.objects.filter(customer=request.user)
    return render(request, 'statement.html', {'statements': statements})
