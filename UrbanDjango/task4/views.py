from django.shortcuts import render

# Create your views here.
def shop(request):
    h1text = 'Игры'
    games = ["Atomic Heart", "Cyberpunk 2077", "PayDay2"]
    context = {
        'h1text': h1text,
        'games': games,
    }
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    h1text = 'Корзина'
    context = {
        'h1text': h1text,
    }
    return render(request, 'fourth_task/cart.html', context)

def platform(request):
    h1text = 'Главная страница'
    context = {
        'h1text': h1text,
    }
    return render(request, 'fourth_task/platform.html', context)