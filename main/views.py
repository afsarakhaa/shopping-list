from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Afsar Rakha Farrasandi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)