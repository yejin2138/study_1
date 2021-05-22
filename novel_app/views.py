from django.shortcuts import redirect, render

def my_novel(request, character1, character2):
     context = {"char_1": character1, "char_2":character2 }
     return render(request, 'novel_html.html', context)

# Create your views here.
