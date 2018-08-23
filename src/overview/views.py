from django.shortcuts import render

# Create your views here.
def overview(request): 
    context = {
        "title":"Dashboard"
        }
    return render(request, "overview.html", context)
