import random

from django.shortcuts import render

from .models import SHAPES, Outcome, Round


MESSAGES = {
    Outcome.draw: 'Draw',
    Outcome.left: 'You win',
    Outcome.right: 'You lose',
}


def index(request):
    if request.method == 'POST':
        round = Round.objects.create(
            left=request.POST.get('choice'),
            right=random.choice(SHAPES)
        )
        message = MESSAGES.get(round.outcome)
    else:
        message = 'Choose a shape'
    return render(request, 'index.html', {
        'message': message,
        'shapes': SHAPES,
        'rounds': list(Round.objects.order_by('id')),
    })
