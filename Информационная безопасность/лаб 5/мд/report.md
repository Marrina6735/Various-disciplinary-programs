---
## Front matter
title: "Отчёт по лабораторной работе №5


Информационная безопасность"
subtitle: "Дискреционное разграничение прав в Linux. Исследование влияния дополнительных атрибутов"
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

Дискреционное разграничение доступа — управление доступом субъектов к объектам на основе списков управления доступом или матрицы доступа. Также используются названия дискреционное управление доступом, контролируемое управление доступом и разграничительное управление доступом. [2]

## SetUID

setuid и setgid (сокращения от англ. set user ID upon execution — «установка ID пользователя во время выполнения» и англ. set group ID upon execution — «установка ID группы во время выполнения») являются флагами прав доступа в Unix, которые разрешают пользователям запускать исполняемые файлы с правами владельца или группы исполняемого файла.  [3]

## Sticky

Sticky bit используется в основном для каталогов, чтобы защитить в них файлы. Из такого каталога пользователь может удалить только те файлы, владельцем которых он является. Примером может служить каталог /tmp, в который запись открыта для всех пользователей, но нежелательно удаление чужих файлов. [4]


# Цель работы

Изучение механизмов изменения идентификаторов, применения SetUID- и Sticky-битов. Получение практических навыков работы в консоли с дополнительными атрибутами. Рассмотрение работы механизма смены идентификатора процессов пользователей, а также влияние бита Sticky на запись и удаление файлов.

# Выполнение лабораторной работы

## Подготовка лабораторного стенда

![(рис. 1. Установка gss)](image/0.PNG){ #fig:001 width=70% height=70% }

## Создание программы

1. Зашли в систему от имени пользователя guest.

2. Создали файл simpleid.c, записали в него программу, скоплировали и запустили его. Программа дала те же результаты, что и консольная команда id. (@fig:001, @fig:002)

![Работа в консоли с файлом simpleid.c](image/1.png){ #fig:001 width=70%}

![Содержимое файла simpleid.c](image/2.png){ #fig:002 width=70%}

3. Создали файл simpleid2.c, записали в него программу, скоплировали и запустили его. (@fig:003, @fig:004)

![Работа в консоли с файлом simpleid2.c](image/3.png){ #fig:003 width=70%}

![Содержимое файла simpleid2.c](image/4.png){ #fig:004 width=70%}

4. Изменили права файла simpleid2 от имени суперпользователя. (@fig:005)

![Изменение прав файла simpleid2](image/5.png){ #fig:005 width=70%}

5. Выполнили проверку установки правил. Запустили simpleid2 и id. Получили одинаковы результаты с id=0. (@fig:006)

![Проверка прав файла simpleid2, его запуск и команда id](image/6.png){ #fig:006 width=70%}

6. Повторили п.5 для SetGID-бита. (@fig:007)

![Выполнения файла с SetGID-битом](image/.png){ #fig:007 width=70%}

7. Создали программу readfile.c и откомпелировали ее. (@fig:008, @fig:009)

![Содержимое файла readfile.c](image/8.png){ #fig:008 width=70%}

![Создание и компелирование readfile.c](image/9.png){ #fig:009 width=70%}

8. Изменили права так, чтобы только суперпользователь (root) мог прочитать readfile.c, a guest не мог. (@fig:010)

![Изменение прав файла readfile.c](image/10.png){ #fig:010 width=70%}

9. Проверили, что guest не модет прочитать файл. (@fig:011)

![Чтение readfile.c пользователем guest](image/11.png){ #fig:011 width=70%}

10. Сменили у программы readfile владельца и установили SetU’D-бит. (@fig:012)

![Смена прав у readfile](image/12.png){ #fig:012 width=70%}

11. Считали программой readfile readfile.c и /etc/shadow. (@fig:013, @fig:014)

![Чтение readfile.c через readfile](image/13.png){ #fig:013 width=70%}

![Чтение /etc/shadow через readfile](image/14.png){ #fig:014 width=70%}

## Исследование Sticky-бита

1. Проверили установлени ли на директории tmp атрибут Sticky. От имени пользователя guest создали file01.txt в директории /tmp  со словом test. Просмотрели атрибуты у файла и разрешили чтение и запись для категории пользователей «все остальные». (@fig:015)

![Создание и изменение прав файла /tmp/file01.txt](image/15.png){ #fig:015 width=70%}

2. От имени пользователя guest2 попробовали прочитать, дозаписать, переписать и удалить файл file01.txt. (@fig:016)

![Взаймдействие с file01.txt пользователем guest2 c Sticky-bit](image/16.png){ #fig:016 width=70%}

3. Суперпользователем сняли Sticky-bit с каталога tmp. Повторили действия с файлом из п.2. (@fig:017)

![Взаймдействие с file01.txt пользователем guest2 без Sticky-bit](image/17.png){ #fig:017 width=70%}

4. Вернули каталогу tmp Sticky-bit суперпользователем. (@fig:018)

![Возвращеник Sticky-bit каталогу tmp](image/18.png){ #fig:018 width=70%}

# Вывод

В ходе выполнения лабораторной работы были опробованы действия на практике SetUID- и Sticky-битов и рассмотрен механизм смены идентификатора процессов пользователей.

# Список литературы. Библиография

[1] Методические материалы курса.
[2] Wikipedia: Избирательное управление доступом. (URL: https://ru.wikipedia.org/wiki/%D0%98%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BE%D0%BC)
[3] Wikipedia: suid (URL: https://ru.wikipedia.org/wiki/Suid)
[4] Wikipedia: Stiky bit (URL: https://ru.wikipedia.org/wiki/Sticky_bit)4. 