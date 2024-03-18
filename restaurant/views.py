from django.shortcuts import render, redirect
from .forms import ReservationForm

def index(request):
    if request.method == "POST":
        form_data = ReservationForm(data=request.POST)
        if form_data.is_valid():
            reservation = form_data.save()
            return redirect("reservations")
    context = {"form": ReservationForm}
    return render(request, "index.html", context=context)

def rest1(request):
    if request.method == "POST":
        form_data = ReservationForm(data=request.POST)
        if form_data.is_valid():
            print(form_data)
            reservation = form_data.save()
            return redirect("rest1")
    context = {"form": ReservationForm}
    return render(request, "rest1.html", context=context)

def rest2(request):
    if request.method == "POST":
        form_data = ReservationForm(data=request.POST)
        if form_data.is_valid():
            reservation = form_data.save()
            return redirect("rest2")
    context = {"form": ReservationForm}
    return render(request, "rest2.html", context=context)

def rest3(request):
    if request.method == "POST":
        form_data = ReservationForm(data=request.POST)
        if form_data.is_valid():
            reservation = form_data.save()
            return redirect("rest3")
    context = {"form": ReservationForm}
    return render(request, "rest3.html", context=context)

def rest4(request):
    if request.method == "POST":
        form_data = ReservationForm(data=request.POST)
        if form_data.is_valid():
            reservation = form_data.save()
            return redirect("rest4")
    context = {"form": ReservationForm}
    return render(request, "rest4.html", context=context)

# Create your views here.
