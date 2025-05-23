---
## Front matter
title: "Отчёт по лабораторной работе №6


Информационная безопасность"
subtitle: "Мандатное разграничение прав в Linux"
author: "Выполнила: Коняева Марина Александровна, 


НФИбд-01-21, 1032217044"



## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
  - spelling=modern
  - babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Теоретическое введение

SELinux (англ. Security-Enhanced Linux — Linux с улучшенной безопасностью) — реализация системы принудительного контроля доступа, которая может работать параллельно с классической избирательной системой контроля доступа. [2]

Apache HTTP-сервер — свободный веб-сервер. Apache является кроссплатформенным ПО, поддерживает операционные системы Linux, BSD, macOS, Microsoft Windows, Novell NetWare, BeOS.

Основными достоинствами Apache считаются надёжность и гибкость конфигурации. Он позволяет подключать внешние модули для предоставления данных, использовать СУБД для аутентификации пользователей, модифицировать сообщения об ошибках и т. д. Поддерживает IPv4. [3]


# Цель работы

Развить навыки администрирования ОС Linux. Получить первое практическое знакомство с технологией SELinux. Проверить работу SELinux на практике совместно с веб-сервером Apache.


# Выполнение лабораторной работы

## Подготовка лабораторного стенда

1. Установили httpd. (@fig:001)

![Установка httpd](image/1.png){ #fig:001 width=70%}

2. В конфигурационном файле /etc/httpd/httpd.conf необходимо задали параметр ServerName. (@fig:002)

![Задача параметра ServerName](image/2.png){ #fig:002 width=70%}

3. Отключили фильтры. (@fig:003)

![Отключение фильтров](image/3.png){ #fig:003 width=70%}

## Основная часть

1. Убедились, что SELinux работает в режиме enforcing политики targeted. (@fig:004)

![Режим работы SELinux](image/4.png){ #fig:004 width=70%}

2. Увидели, что сервер не работает и запустили его. (@fig:005, @fig:006 )

![Проверка работы сервера](image/5.png){ #fig:005 width=70%}

![Запуск сервера](image/6.png){ #fig:006 width=70%}

3. Определили контекст безопасности Appache - unconfined_u:unconfined_r:unconfined_t. (@fig:007)

![Определение контекста безопасности](image/7.png){ #fig:007 width=70%}

4. Посмотрели текущее состояние переключателей SELinux для Apache. (@fig:008)

![Текущее состояние переключателей SELinux для Apache](image/8.png){ #fig:008 width=70%}

5. Посмотрели статистику по политике с помощью команды seinfo. (@fig:009)

![Статистика по политике](image/9.png){ #fig:009 width=70%}

6. Определили тип файлов и поддиректорий, находящихся в директории /var/www. (@fig:010)

![Тип файлов и поддиректорий в /var/www](image/10.png){ #fig:010 width=70%}

7. Определили тип файлов и поддиректорий, находящихся в директории /var/www/html. (@fig:011)

![Тип файлов и поддиректорий в /var/www/html](image/11.png){ #fig:011 width=70%}

8. Создали файл test.html и проверили его контест. (@fig:012)

![Создание test.html](image/12.png){ #fig:012 width=70%}

9. Обратились к файлу через веб-сервер. (@fig:013)

![Обращение к файлу через браузер](image/13.png){ #fig:013 width=70%}

10. Изменили контекст файла и проверили что он поменялся. (@fig:014)

![Смена контекста test.html](image/14.png){ #fig:014 width=70%}

11. Попробовали получить доступ к файлу через браузер. (@fig:015)

![Обращение к файлу через браузер после смены контекста](image/15.png){ #fig:015 width=70%}

12. Просмотрели системный лог-файл. Увидели, что проблема в смененном контексте. (@fig:016)

![Просмотр системного лог-файла](image/16.png){ #fig:016 width=70%}

13. Поменяли прослушивание TCP-порта на 81. (@fig:017)

![Изменение прослушивания TCP-порта](image/17.png){ #fig:017 width=70%}

14. Перезапустили Apache, не получили ошибки. (@fig:018)

![Перезапуск Apache](image/18.png){ #fig:018 width=70%}

15. Добавили порт 81 и проверили, что он появился в списке. (@fig:019)

![Добавление порта 81](image/19.png){ #fig:019 width=70%}

16. Перезапустили Apache, вернули изначальный контекст test.html. (@fig:020)

![Перезапуск Apache, возвращение изначального контекста test.html](image/20.png){ #fig:020 width=70%}

17. Обратились к файлу через веб-сервер. (@fig:021)

![Обращение к файлу через браузер после возвращения контекста](image/21.png){ #fig:021 width=70%}

18. Вернули порт 80. (@fig:022)

![Возвращение порта 80 в httpd.conf](image/22.png){ #fig:022 width=70%}

19. Ввели команду для удаления порта 81 из списка. Удалили файл test.html. (@fig:023)

![Работа команды удаления порта 81 и удаление test.html](image/23.png){ #fig:023 width=70%}

# Вывод

В ходе выполнения лабораторной работы были развиты навыки администрирования ОС Linux и проверена работа SELinux на практике совместно с веб-сервером Apache.


# Список литературы. Библиография

[1] Методические материалы курса.

[2] Wikipedia: SELinux (URL: https://ru.wikipedia.org/wiki/SELinux)

[3] Wikipedia: Apache HTTP Server (URL: https://ru.wikipedia.org/wiki/Apache_HTTP_Server)3. 
