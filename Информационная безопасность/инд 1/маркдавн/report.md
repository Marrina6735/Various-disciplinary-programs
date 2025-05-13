---
## Front matter
title: "Отчёт по индивидуальному проекту 


Информационная безопасность"
subtitle: "Этап 1. Установка Kali Linux"
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

# Цель работы

Установите дистрибутив Kali Linux в виртуальную машину.
В качестве среды виртуализации предлагается использовать VirtualBox.
Сайт Kali Linux: https://www.kali.org/
Учётные данные по умолчанию: логин: root; пароль: toor.

# Выполнение работы

1. Создание виртуальной машины

![(Создание виртуальной машины](image/1.PNG){ #fig:001 width=70% height=70% }


2. Скачивание дитрибутива  Kali Linux

![(Скачивание дитрибутива  Kali Linux](image/2.PNG){ #fig:002 width=70% height=70% }


3. Добавление дитрибутива  Kali Linux

![(Добавление дитрибутива  Kali Linux](image/4.PNG){ #fig:003 width=70% height=70% }


4. Завершение установки дитрибутива  Kali Linux с учетными данными

![(учетные данные](image/3.PNG){ #fig:006 width=70% height=70% }

![(окно Kali Linux](image/5.PNG){ #fig:010 width=70% height=70% }

# Вывод

В ходе выполнения работы была установка Kali Linux в виртуальную машину с учетными данными.

# Список литературы. Библиография

[1] Операционные системы: https://blog.skillfactory.ru/glossary/operaczionnaya-sistema/

[2] Права доступа: https://codechick.io/tutorials/unix-linux/unix-linux-permissions