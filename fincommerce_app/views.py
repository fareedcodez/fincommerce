from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Renders the home page
    """
    #products = Product.objects.all()
    #context = {'products': products}
    return render(request, 'fincommerce_app/home.html')