from django.shortcuts import render
from django.views.generic import View
from utils.mixin import LoginRequiredMixin


class Board(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'board.html')
