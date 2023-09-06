import threading

from django.shortcuts import render
from .my_bots.bot_1.bot_1 import my_bot_1
from .my_bots.bot_2.bot_2 import my_bot_2


def index(request):
    context = {'error': False}
    return render(request, 'main/index.html', context)


def run_bot(request, pk):
    context = {'message': ''}
    if pk == 1:
        t = threading.Thread(target=polling_bot, args=(my_bot_1,))
        t.daemon = True
        t.start()
        context["message"] = 'Bot 1 run successful'
    elif pk == 2:
        t = threading.Thread(target=polling_bot, args=(my_bot_2,))
        t.daemon = True
        t.start()
        context["message"] = 'Bot 2 run successful'
    else:
        context.message = 'Error!'
    return render(request, 'main/index.html', context)


def polling_bot(bot):
    bot.polling(none_stop=True)