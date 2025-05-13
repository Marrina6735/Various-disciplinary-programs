---
## Front matter
title: "Отчёт по третьему этапу индивидуального проекта


"
subtitle: "Информационная безопасность"
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

Приобретение практических навыков по использованию инструмента Hydra для брутфорса паролей.

# Задание

Реализовать эксплуатацию уязвимости с помощью брутфорса паролей.

# Теоретическое введение

- Hydra используется для подбора или взлома имени пользователя и пароля.
- Поддерживает подбор для большого набора приложений [@brute, @force, @parasram].[1]

**Пример работы**:

Исходные данные:

- IP сервера 178.72.90.181;

- Сервис http на стандартном 80 порту;

- Для авторизации используется html форма, которая отправляет по адресу http://178.72.90.181/cgi-bin/luci методом POST запрос вида username=root&password=test_password;

- В случае неудачной аутентификации пользователь наблюдает сообщение Invalid username and/or password! Please try again.

- Запрос к Hydra будет выглядеть примерно так:

`hydra -l root -P ~/pass_lists/dedik_passes.txt -o ./hydra_result.log -f -V -s 80 178.72.90.181 http-post-form "/cgi-bin/luci:username=^USER^&password=^PASS^:Invalid username"`

- Используется http-post-form потому, что авторизация происходит по http методом post.

- После указания этого модуля идёт строка /cgi-bin/luci:username=^USER^&password=^PASS^:Invalid username, у которой через двоеточие (:) указывается:

- путь до скрипта, который обрабатывает процесс аутентификации (/cgi-bin/luci);

- строка, которая передаётся методом POST, в которой логин и пароль заменены на ^USER^ и ^PASS^ соответственно (username=^USER^&password=^PASS^);

- строка, которая присутствует на странице при неудачной аутентификации; при её отсутствии Hydra поймёт, что мы успешно вошли (Invalid username).


# Выполнение лабораторной работы

 Чтобы пробрутфорсить пароль, нужно сначала найти большой список частоиспользуемых паролей. Его можно найти в открытых источниках, я взяла стандартный список паролей `rockyou.txt` для kali linux (рис. 1).

![Распаковка архива со списком паролей](image/1.PNG){#fig:001 width=70%}

Захожу на сайт DVWA, полученный в ходе предыдущего этапа проекта. Для запроса hydra мне понадобятся параметры cookie с этого сайта (рис. 2).
 
![Сайт, с которого получаем информацию о параметрах Cookie](image/2.PNG){#fig:002 width=70%}

Чтобы получить информацию о параметрах cookie я установила соответствующее расширение для браузера [@cookies], теперь могу не только увидеть параметры cookie, но и скопировать их (рис. 3).

![Информация о параметрах Cookie](image/3.PNG){#fig:003 width=70%}

Ввожу в Hydra запрос нужную информацию. Пароль будем подбирать для пользователя admin, используем GET-запрос с двумя параметрами cookie: безопасность и PHPSESSID, найденными в прошлом пункте (рис. 4).

![Запрос Hydra](image/4.PNG){#fig:004 width=70%}

Спустя некоторое время в результат запроса появится результат с подходящим паролем (рис. 5).

![Результат запроса](image/5.PNG){#fig:005 width=70%}

Вводим полученные данные на сайт для проверки (рис. 6).

![Ввод полученного результата в уязвимую форму](image/6.PNG){#fig:006 width=70%}

Получаем положительный результат проверки пароля. Все сделано верно (рис. 7).

![Результат](image/7.PNG){#fig:007 width=70%}

# Выводы

В результате выполнения 3 этапа индивидуального проекта были приобретены практические навыки по использованию инструмента Hydra для брутфорса паролей.

# Список литературы

[1] Методические материалы курса

[2] Kali Linux Tool Documentation: Hydra (URL: https://www.kali.org/tools/hydra/)