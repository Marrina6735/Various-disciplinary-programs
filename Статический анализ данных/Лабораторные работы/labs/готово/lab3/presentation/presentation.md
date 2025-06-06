---
## Front matter
lang: ru-RU
title: Лабораторная работа №3 Управляющие структуры
subtitle: Статический анализ данных
author: |
        Коняева Марина Александровна
        \        
        НФИбд-01-21
        \
        Студ. билет: 1032217044
institute: |
           RUDN
date: |
      2024

babel-lang: russian
babel-otherlangs: english
mainfont: Arial
monofont: Courier New
fontsize: 9pt

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

## Цели лабораторной работы

Освоить применение циклов функций и сторонних для Julia пакетов для решения задач линейной алгебры и работы с матрицами.

## Теоретическое введение 

Для различных операций, связанных с перебором индексируемых элементов структур данных, традиционно используются циклы while и for. Синтаксис while:
while <условие>
  <тело цикла>
end

Такие же результаты можно получить при использовании цикла for. Синтаксис for:
for <переменная> in <диапазон>
  <тело цикла>
end

Довольно часто при решении задач требуется проверить выполнение тех или иных условий. Для этого используют условные выражения. Синтаксис условных выражений с ключевым словом:
if <условие 1>
  <действие 1>
elseif <условие 2>
  <действие 2>
else
  <действие 3>
end

## Задачи лабораторной работы

1. Используя Jupyter Lab, повторите примеры из раздела 3.2.
2. Выполните задания для самостоятельной работы (раздел 3.4).

## Выполнение лабораторной работы: циклы while и for 

1. Использование цикла while для формирования элементов массива. 

![Формирования элементов массива](1.png){ #fig:002 width=40% }

2. Работе со строковыми элементами массиват с цилом while, подставляя имя из массива в заданную строку приветствия и выводя
получившуюся конструкцию на экран.

![while при работе со строковыми элементами массива](2.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: циклы while и for 

3. Использование цикла for для формирования элементов массива. 

![Формирования элементов массива](3.png){ #fig:002 width=40% }

4. Работе со строковыми элементами массиват с цилом for, подставляя имя из массива в заданную строку приветствия и выводя
получившуюся конструкцию на экран.

![for при работе со строковыми элементами массива](4.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: циклы while и for 

5. Создания двумерного массива цикла for для создания двумерного массива, в котором значение каждой записи является суммой индексов строки и столбца.

![Создания двумерного массива](5.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: условные выражения 

6. Пример: пусть для заданного числа 𝑁 требуется вывести слово «Fizz», если 𝑁 делится на 3, «Buzz», если 𝑁 делится на 5, и «FizzBuzz», если 𝑁 делится на 3 и 5.

![Примеры с условными выражениями](6.png){ #fig:002 width=40% }

7. Пример с условными выражениями с тернарными операторами. Синтаксис: a ? b : c.
Такая запись эквивалентна записи условного выражения с ключевым словом:
if a
    b
else
    c
end

![Пример с условными выражениями с тернарными операторами](7.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: функции 

8. Изучим информацию о функция и повторим примеры их задания, использования и вызов.

![Функции (задание и вызов) 1](8.png){ #fig:002 width=40% }

9. Повторим примеры с функциями, где можно объявить любую из выше определённых функций в одной строке, а также выполним пример, где можно объявить выше определённые функции как «анонимные».

![Функции (задание и вызов) 2-3](9.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: функции 

10. Выполним примеры с sort и sort!.

![Примеры с sort и sort!](10.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: функции

11. Повторим примеры с функцией map.

![Примеры с map](11.png){ #fig:002 width=40% }

12. Повторим примеры с функцией maр, в map можно передать и анонимно заданную, а не именованную функцию.

![Примеры с map](12.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: функции 

13. Выполним примеры с функцией broadcast. Синтаксис для вызова broadcast такой же, как и для вызоваmap, например применение функции f к элементам массива [1, 2, 3]:
f(x) = x^2
broadcast(f, [1, 2, 3])
или
f.([1, 2, 3])

![Примеры с broadcast](13.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: функции 

14. Выполним примеры с функцией broadcast, точечный синтаксис для broadcast() позволяет записать относительно сложные составные поэлементные выражения в форме, близкой к математической записи.

![Примеры с broadcast](14.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: сторонние библиотеки 

15. Изучим информацию о сторонних библиотеках. Julia имеет более 2000 зарегистрированных пакетов, что делает их огромной частью экосистемы Julia. Есть вызовы функций первого класса для других языков, обеспечивающие интерфейсы сторонних функций. Можно вызвать функции из Python или R, например, с помощью PyCall или Rcall. 

– https://julialang.org/packages/
– https://juliahub.com/ui/Home
– https://juliaobserver.com/
– https://github.com/svaksha/Julia.jl

16. Добавим необходимые пакеты для дальнейшего использования.

![Сторонние библиотеки (пакеты)](15.png){ #fig:002 width=40% } 

## Выполнение лабораторной работы: сторонние библиотеки 

17. Создадим палитру из 100 разных цветов, а затем определим матрицу 3 × 3 с элементами в форме случайного цвета из палитры, используя функцию rand.

![Пример со сторонними библиотеками](16.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

18. Выполним 1 задание: Используя циклы while и for:

– выведите на экран целые числа от 1 до 100 и напечатайте их квадраты;

![1 задания: часть 1](17.png){ #fig:002 width=40% }

– создайте словарь squares, который будет содержать целые числа в качестве ключей и квадраты в качестве их пар-значений;

![1 задания: часть 2](18.png){ #fig:002 width=40% }

![1 задания: часть 3](19.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

19. Выполним 2 задание: напишите условный оператор, который печатает число, если число чётное, и строку «нечётное», если число нечётное. Перепишите код, используя тернарный оператор.

![Выполнение 2 задания](20.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

20. Выполним 3 задание: напишите функцию add_one, которая добавляет 1 к своему входу.

![Выполнение 3 задания](21.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

21. Выполним 4 задание: используйте map() или broadcast() для задания матрицы 𝐴, каждый элемент которой увеличивается на единицу по сравнению с предыдущим.

![Задание 4](22.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

22. Выполним 5 задание: задайте матрицу $A$ следующего вида:

$$
A = \begin{pmatrix}
1 & 1 & 3 \\
5 & 2 & 6 \\
-2 & -1 & -3
\end{pmatrix}
$$ 

![Задание 5](23.png){ #fig:002 width=40% }

- Найдите $A^3$ 

![Задание 5: часть 1](24.png){ #fig:002 width=40% }

- Замените третий столбец матрицы $A$ на сумму 2-го и 3-го столбцов

![Задание 5: часть 2](25.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

23. Выполним 6 задание: создайте матрицу $B$ с элементами $B_{i1} = 10, B_{i2} = −10, B_{i3} = 10, \quad i = 1, 2, … , 15$.

![Задание 6](26.png){ #fig:002 width=40% }

- Вычислите матрицу $C = B^T B$.

![Задание 6](27.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

24. Выполним 7 задание: создайте матрицу $Z$ размерности $6\times 6$, все элементы которой равны нулю, и матрицу $E$, все элементы которой равны $1$.

![Задание 7](28.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

- Используя цикл `while` или `for` и закономерности расположения элементов, создайте следующие матрицы размерности $6\times 6$:

$$
Z_1 = \begin{pmatrix}
0 & 1 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0 & 1 \\
0 & 0 & 0 & 0 & 1 & 0
\end{pmatrix}, \qquad
Z_2 = \begin{pmatrix}
1 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 & 0 & 0 \\
1 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 & 0 & 1 \\
0 & 0 & 1 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0 & 1
\end{pmatrix},
$$

$$
Z_3 = \begin{pmatrix}
0 & 0 & 0 & 1 & 0 & 1 \\
0 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 & 0
\end{pmatrix}, \qquad
Z_4 = \begin{pmatrix}
1 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 & 0 & 1
\end{pmatrix}.
$$

## Выполнение лабораторной работы: самостоятельная работа 

![Задание 7: часть 1](29.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

25. Выполним 8 задание: в языке R есть функция outer(). 

- Напишите свою функцию, аналогичную функции outer() языка R. Функция должна иметь следующий интерфейс: `outer(x,y,operation)`. Таким образом, функция вида `outer(A,B,*)` должна быть эквивалентна произведению матриц $A$ и $B$ размерностями $L\times M$ и $M\times N$ соответственно, где элементы результирующей матрицы $C$ имеют вид $C_{ij} = \sum_{k=1}^{M} A_{ik}B_{kj}$ (или в тензорном виде $C_i^j = \sum_{k=1}^{M} A^i_kB^k_j$)

## Выполнение лабораторной работы: самостоятельная работа 

![Задание 8: часть 1](30.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

![Задание 8: часть 1 (вывод)](31.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

- Используя написанную вами функцию `outer()`, создайте матрицы следующей структуры:

$$
A_1 = \begin{pmatrix}
0 & 1 & 2 & 3 & 4 \\
1 & 2 & 3 & 4 & 5 \\
2 & 3 & 4 & 5 & 6 \\
3 & 4 & 5 & 6 & 7 \\
4 & 5 & 6 & 7 & 8
\end{pmatrix}, \qquad
A_2 = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 \\
1 & 1 & 1 & 1 & 1 \\
2 & 4 & 8 & 16 & 32 \\
3 & 9 & 27 & 81 & 243 \\
4 & 16 & 64 & 256 & 1024
\end{pmatrix},
$$

$$
A_3 = \begin{pmatrix}
0 & 1 & 2 & 3 & 4 \\
1 & 2 & 3 & 4 & 0 \\
2 & 3 & 4 & 0 & 1 \\
3 & 4 & 0 & 1 & 2 \\
4 & 0 & 1 & 2 & 3
\end{pmatrix}, \qquad
A_4 = \begin{pmatrix}
0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
8 & 9 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
9 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8
\end{pmatrix},
$$

$$
A_5 = \begin{pmatrix}
0 & 8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
1 & 0 & 8 & 7 & 6 & 5 & 4 & 3 & 2 \\
2 & 1 & 0 & 8 & 7 & 6 & 5 & 4 & 3 \\
3 & 2 & 1 & 0 & 8 & 7 & 6 & 5 & 4 \\
4 & 3 & 2 & 1 & 0 & 8 & 7 & 6 & 5 \\
5 & 4 & 3 & 2 & 1 & 0 & 8 & 7 & 6 \\
6 & 5 & 4 & 3 & 2 & 1 & 0 & 8 & 7 \\
7 & 6 & 5 & 4 & 3 & 2 & 1 & 0 & 8 \\
8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 & 0
\end{pmatrix}.
$$

В каждом случае ваше решение должно быть легко обобщаемым на случай создания матриц большей размерности, но той же структуры.

## Выполнение лабораторной работы: самостоятельная работа

![Задание 8: часть 2](32.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

![Задание 8: часть 2 (вывод)](33.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа

26. Выполним 9 задание: решите следующую систему линейных уравнений с 5 неизвестными

$$
\begin{cases}
x_1 + 2x_2 + 3x_3 + 4x_4 + 5x_5 = 7, \\
2x_1 + x_2 + 2x_3 + 3x_4 + 4x_5 = −1, \\
3x_1 + 2x_2 + x_3 + 2x_4 + 3x_5 = −3, \\
4x_1 + 3x_2 + 2x_3 + x_4 + 2x_5 = 5, \\
5x_1 + 4x_2 + 3x_3 + 2x_4 + x_5 = 17,
\end{cases}
$$

рассмотрев соответствующее матричное уравнение $Ax = y$. Обратите внимание на особый вид матрицы $A$.
Метод, используемый для решения данной системы уравнений, должен быть легко обобщаем на случай большего числа уравнений,
где матрица $A$ будет иметь такую же структуру.

Решение будет осуществлено методом Гаусса.

## Выполнение лабораторной работы: самостоятельная работа 

![Задание 9: метод Гаусса](34.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа

![Задание 9: метод Гаусса (решение)](35.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа

27. Выполним 10 задание: создайте матрицу $M$ размерности $6 \times 10$, элементами которой являются целые числа, выбранные случайным образом с повторениями из совокупности $1, 2,\dots, 10$.

![Задание 10](36.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

- Найдите число элементов в каждой строке матрицы $M$, которые больше числа $N$ (например, $N = 4$).

![Задание 10: часть 1](37.png){ #fig:002 width=40% }

- Определите, в каких строках матрицы $M$ число $T$ (например, $T = 7$) встречается ровно 2 раза?

![Задание 10: часть 2](38.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

- Определите все пары столбцов матрицы $M$, сумма элементов которых больше $K$ (например, $K = 75$).

![Задание 10: часть 3](39.png){ #fig:002 width=40% }

## Выполнение лабораторной работы: самостоятельная работа 

28. Выполним 11 задание: вычислите:

- $$\sum_{i=1}^{20} \sum_{j=1}^{5} \frac{i^4}{(3+j)}$$

![Задание 11: часть 1](40.png){ #fig:002 width=40% }

- $$\sum_{i=1}^{20} \sum_{j=1}^{5} \frac{i^4}{(3+ij)}$$

![Задание 11: часть 1](41.png){ #fig:002 width=40% }

## Выводы по проделанной работе

В результате выполнения работы мы освоили применение циклов функций и сторонних для Julia пакетов для решения задач линейной алгебры и работы с матрицами.
Были записаны скринкасты выполнения , создания отчета, презентации и защиты лабораторной работы.

## Список литературы

- Julia: https://ru.wikipedia.org/wiki/Julia
- https://julialang.org/packages/
- https://juliahub.com/ui/Home
- https://juliaobserver.com/
- https://github.com/svaksha/Julia.jl

