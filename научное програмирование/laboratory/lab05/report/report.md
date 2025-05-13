---
# Front matter
lang: ru-RU
title: "Научное програмирование"
subtitle: "Отчет по лабораторной работе № 5"
author: "Меньшов Иван Сергеевич НПМмд-02-21"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Ознакомление с некоторыми операциями в среде Octave для решения таких задач, как подгонка полиномиальной кривой, матричных преобразований, вращений, отражений и дилатаций.

# Выполнение лабораторной работы

## Подгонка полиномиальной кривой

В статистике часто рассматривается проблема подгонки прямой линии к набору данных. Решим более общую проблему подгонки полинома к множеству точек. Пусть нам нужно найти параболу по методу наименьших квадратов для набора точек, заданных матрицей  

$$
D =
\left(
\begin{array}{cc}
1 & 1 
\\ 
2 & 2 
\\
3 & 5
\\
4 & 4
\\
5 & 2
\\
6 & -3
\end{array}
\right)
$$

В матрице заданы значения $x$ в столбце 1 и значения $y$ в столбце 2.Введём матрицу данных в Octave и извлечём вектора $x$ и $y$. А также нарусуем точки на графике.Данные операции выполнены ниже: 

![Програмный код 01](image/01.PNG){ #fig:001 width=70% height=70%}

![График 01](image/02.PNG){ #fig:002 width=70% height=70%}

Построим уравнение вида $y = ax^2 + bx + c$. Подставляя данные,
получаем следующую систему линейных уравнений.  

$$
\left(
\begin{array}{ccc}
1 & 1 & 1
\\ 
4 & 2 & 1
\\
9 & 3 & 1
\\
16 & 4 & 1
\\
25 & 5 & 1
\\
36 & 6 & 1
\end{array}
\right)
\left(
\begin{array}{c}
a
\\ 
b
\\
c
\end{array}
\right)
=
\left(
\begin{array}{c}
1
\\ 
2
\\
5
\\
4
\\
2
\\
-3
\end{array}
\right).
$$  

Обратим внимание на форму матрицы коэффициентов $A$.Третий столбец – все единицы, второй столбец – значения $x$, а первый столбец – квадрат значений $x$.Правый вектор – это значения $y$. Есть несколько способов построить матрицу коэффициентов в Octave. Один из подходов состоит в том, чтобы использовать команду ones для создания матрицы единиц соответствующего размера, а затем перезаписать первый и второй столбцы необходимыми данными.

![Програмный код 02](image/03.PNG){ #fig:003 width=70% height=70%}

Решение по методу наименьших квадратов получается из решения уравнения $A^T Ab = A^T b$, где $b$ – вектор коэффициентов полинома. Используем Octave для построения уравнений, как показано ниже: 

![Програмный код 03](image/04.PNG){ #fig:004 width=70% height=70%}

Решим задачу методом Гаусса. Для этого запишем расширенную матрицу:

$$
B =
\left(
\begin{array}{cccc}
2275 & 441 & 91 & 60 
\\ 
441 & 91 & 21 & 28 
\\
91 & 21 & 6 & 11
\end{array}
\right).
$$  

Таким образом, искомое квадратное уравнение имеет вид

$$
y = -0.89286 x^2 + 5.65 x - 4.4
$$  

![Програмный код 04](image/05.PNG){ #fig:005 width=70% height=70%}

![Програмный код 05](image/06.PNG){ #fig:006 width=70% height=70%}

После чего построим соответствующий график параболы.

![Програмный код 06](image/07.PNG){ #fig:007 width=70% height=70%}

![Програмный код 07](image/08.PNG){ #fig:008 width=70% height=70%}

![График 02](image/09.PNG){ #fig:009 width=70% height=70%}

Процесс подгонки может быть автоматизирован встроенными функциями Octave. Для этого мы можем использовать встроенную функцию для подгонки полинома polyfit. Синтаксис: polyfit (x, y, order), где order – это степень полинома. Значения полинома P в точках, задаваемых вектором-строкой x можно получить с помощью функции polyval. Синтаксис: polyval (P, x). 

![Програмный код 08](image/10.PNG){ #fig:010 width=70% height=70%}

После чего рассчитаем значения в точках и построим исходные данные.

![График 03](image/11.PNG){ #fig:011 width=70% height=70%}

## Матричные преобразования  
Матрицы и матричные преобразования играют ключевую роль в компьютерной графике. Существует несколько способов представления изображения в виде матрицы. Подход, который мы здесь используем, состоит в том, чтобы перечислить ряд вершин, которые соединены последовательно, чтобы получить ребра простого графа. Мы записываем это как матрицу $2 \times n$, где каждый столбец представляет точку на рисунке. В качестве простого примера, давайте попробуем закодировать граф-домик. Есть много способов закодировать это как матрицу. Эффективный метод состоит в том, чтобы выбрать путь, который проходит по каждому ребру ровно один
раз (цикл Эйлера).  

$$
D =
\left(
\begin{array}{ccccccc}
1 & 1 & 3 & 3 & 2 & 1 & 3
\\ 
2 & 0 & 0 & 2 & 3 & 2 & 2
\end{array}
\right).
$$  

![Програмный код 09](image/12.PNG){ #fig:012 width=70% height=70%}

![График 04](image/13.PNG){ #fig:013 width=70% height=70%}

## Вращение 
 
Рассмотрим различные способы преобразования изображения. Вращения могут быть получены с использованием умножения на специальную матрицу. Вращение точки $(x, y)$ относительно начала координат определяется как  

$$
R
\left(
\begin{array}{c}
x
\\ 
y
\end{array}
\right),
$$

где

$$
R =
\left(
\begin{array}{cc}
cos(\theta) & -sin(\theta)
\\ 
sin(\theta) & cos(\theta)
\end{array}
\right),
$$  

$\theta$ - угол поворота (измеренный против часовой стрелки).

Теперь, чтобы произвести повороты матрицы данных $D$, нам нужно
вычислить произведение матриц $RD$. Повернём граф дома на $90^{\circ}$ и $225^{\circ}$. Вначале переведём угол в радианы.  

![Програмный код 10](image/14.PNG){ #fig:014 width=70% height=70%}

![Програмный код 11](image/15.PNG){ #fig:015 width=70% height=70%}

![Програмный код 12](image/16.PNG){ #fig:016 width=70% height=70%}

![График 05](image/17.PNG){ #fig:017 width=70% height=70%}

## Отражение  

Если $l$ – прямая, проходящая через начало координат, то отражение точки $(x, y)$ относительно прямой $l$ определяется как

$$
R
\left(
\begin{array}{c}
x
\\ 
y
\end{array}
\right),
$$

где

$$
R =
\left(
\begin{array}{cc}
cos(2\theta) & sin(2\theta)
\\ 
sin(2\theta) & -cos(2\theta)
\end{array}
\right),
$$

$\theta$ - угол между прямой $l$ и осью абсцисс (измеренный против часовой стрелки).

![Програмный код 13](image/18.PNG){ #fig:018 width=70% height=70%}

![Програмный код 14](image/19.PNG){ #fig:019 width=70% height=70%}

![График 06](image/20.PNG){ #fig:020 width=70% height=70%}

## Дилатация  

Дилатация (то есть расширение или сжатие) также может быть выполнено путём умножения матриц. Пусть  

$$
T =
\left(
\begin{array}{cc}
k & 0
\\ 
0 & k
\end{array}
\right),
$$  

Тогда матричное произведение $TD$ будет преобразованием дилатации $D$ с коэффициентом $k$. Увеличим граф дома в 2 раза. 

![Програмный код 15](image/21.PNG){ #fig:021 width=70% height=70%}

![График 07](image/22.PNG){ #fig:022 width=70% height=70%}

# Вывод 
В ходе выполнения данной работы я ознакомился с некоторыми операциями в среде Octave для решения таких задач, как подгонка полиномиальной кривой, матричных преобразований, вращений, отражений и дилатаций.