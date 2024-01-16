import logging

from django.shortcuts import render
from django.http import HttpResponse
from logging import Logger

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index got response')
    return HttpResponse(f'<h2>Главная страница</h1><br><h2>Контент главной страницы</h2><br><p>Подвал</p>')


def about_me(request):
    logger.info('about me got response')
    return HttpResponse(f'<h2>Обо мне</h2><br><p>Информация обо мне</p>')

