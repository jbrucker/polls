from django.shortcuts import render

# Create your views here.

def show_request(request):
    """Display details of the HttpRequest object"""
    context = {"request":request, "fields": [] }

    for field in dir(request):
        context["fields"].append(field)
    return render(request, 'info/detail.html', context)
