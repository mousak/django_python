from django.shortcuts import render

def about(request):
	return render(request, "about.html", {})

def reparation(request):
	return render(request, "reparation.html", {})

def accessories(request):
	return render(request, "accessories.html", {})

def maintenance(request):
	return render(request, "maintenance.html", {})

def offers(request):
	return render(request, "offers.html", {})
