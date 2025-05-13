---
## Front matter
title: "ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ № 2"
subtitle: "Markdown"
author: "Коняева Марина Александровна"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
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
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Научиться оформлять отчёты с помощью легковесного языка разметки Markdown.

# Теоретическое введение

Markdown — язык текстовой разметки, созданный писателем и блогером Джоном Грубером. Он предназначен для создания красиво оформленных текстов в обычных файлах формата TXT. Вам не нужны громоздкие процессоры вроде Word или Pages,чтобы создавать документы с жирным или курсивным начертанием, цитатами, ссылками и даже таблицами. Достаточно запомнить простые правила Markdown, и можно писать хоть в «Блокноте». Хотя специализированные Markdown-редакторы, конечно, намного удобнее.

# Выполнение лабораторной работы

1. Запишем отчет по лабораторной работе 2 в markdown file

![отчет в markdown](image/1%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA.png){ #fig:001 width=100% }
*Изображение 1.1 отчет в markdown*

2. Затем сконвертируем файл в форматах pdf и docx

![сконвертируем файл в форматах](image/2%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA.png){ #fig:001 width=100% }
*Изображение 2.1 сконвертируем файл в форматах*

![сконвертируем файл в форматах](image/3%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA.png){ #fig:001 width=100% }
*Изображение 2.2 сконвертируем файл в форматах*

3. Проверим читабельное оформление отчета в разных форматах

# Выводы

В ходе данной лабораторной работы научились оформлять отчеты с помощью легковесного языка разметки Markdown.

# Контрольные вопросы

Контрольные вопросы отстутсвуют в лабораторной работе 3