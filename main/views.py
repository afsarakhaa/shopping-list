from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Afsar Ganteng Banget',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)