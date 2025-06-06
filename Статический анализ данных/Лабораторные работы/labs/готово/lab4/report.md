---
## Front matter
title: "Отчёт по лабораторной работе №4


Линейная алгебра"
subtitle: "Статический анализ данных"
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


# Цели лабораторной работы

Изучение возможностей специализированных пакетов Julia для выполнения и оценки эффективности операций над объектами линейной алгебры.

# Теоретическое введение 

![](1231.png){ #fig:002 width=40% }

![](1233.png){ #fig:002 width=40% }

![](1232.png){ #fig:002 width=40% }

В математике факторизация (или разложение) объекта — его декомпозиция (например, числа, полинома или матрицы) в произведение других объектов или факторов, которые, будучи перемноженными, дают исходный объект.

# Задачи лабораторной работы

1. Используя Jupyter Lab, повторите примеры из раздела 4.2.
2. Выполните задания для самостоятельной работы (раздел 4.4).

# Выполнение лабораторной работы

## Поэлементные операции над многомерными массивами

1. Изучим информацию о поэлементных операциях над многомерными массивами.
 
2. Повторим примеры с поэлементными операциями над многомерными массивами: Для матрицы 4 × 3 рассмотрим поэлементные операции сложения её элементов:

![Матрица 4×3, сложения её элементов](1.png){ #fig:002 width=40% }

3. Повторим примеры с поэлементными операциями над многомерными массивами: Для матрицы 4 × 3 рассмотрим поэлементные операции произведения её элементов:

![Матрица 4×3, произведение её элементов](2.png){ #fig:002 width=40% }

4. Для работы со средними значениями можно воспользоваться возможностями пакета
Statistics.

![Добавление пакета](3.png){ #fig:002 width=40% }

5. Повторим примеры с нахождением среднего значения массива, его среднего значения по столбцам и строкам.

![Среднее значение массива](4.png){ #fig:002 width=40% }

## Транспонирование, след, ранг, определитель и инверсия матрицы

6. Для выполнения таких операций над матрицами, как транспонирование, диагонализация, определение следа, ранга, определителя матрицы и т.п. можно воспользоваться библиотекой (пакетом) LinearAlgebra.

![Добавление пакета](5.png){ #fig:002 width=40% }

7. Повторим пример создание массива 4x4 со случайными целыми числами (от 1 до 20).

![Массив 4x](6.png){ #fig:002 width=40% }

8. Повторим примеры с массивом: транспонирование, след матрицы.

![Транспонирование, след матрицы](7.png){ #fig:002 width=40% }

9. Повторим примеры с массивом: извлечение диагональных элементов как массив,  ранг матрицы.

![Извлечение диагональных элементов, ранг матрицы](8.png){ #fig:002 width=40% }

10. Повторим примеры с массивом: инверсия матрицы (определение обратной матрицы), определитель матрицы.

![Инверсия матрицы, определитель матрицы](9.png){ #fig:002 width=40% }

11. Повторим примеры с массивом: псевдобратная функция для прямоугольных матриц

![Псевдобратная функция для прямоугольных матриц](10.png){ #fig:002 width=40% }

##  Вычисление нормы векторов и матриц, повороты, вращения

![](1231.png){ #fig:002 width=40% }

12. Повторим пример с вычилением нормы, а именно создаем вектор, высчитываем евклидовую норму и р-норму.

![Вектор](11.png){ #fig:002 width=40% }

![Нормы](12.png){ #fig:002 width=40% }

![ ](1233.png){ #fig:002 width=40% }

13. Повторим примеры с вычислением евклидово расстояния между двумя векторами. 

![Расстояние](13.png){ #fig:002 width=40% }

![ ](1232.png){ #fig:002 width=40% }

14. Повторим примеры с вычислением угла между двумя веткорами. 

![Угол](14.png){ #fig:002 width=40% }

15. Повторим пример с вычилением нормы для двумерной мтарицы, а именно создаем матрицу, высчитываем евклидовую норму и р-норму.

![Матрица и нормы](15.png){ #fig:002 width=40% }

16. Выполним примеры с поворотом и переворачиваем по строкам и столбцам.

![Примеры с поворотом и переворачиваем по строкам и столбцам](16.png){ #fig:002 width=40% }

## Матричное умножение, единичная матрица, скалярное произведение

17. Повторим примеры: создадим дву матрицы и заполним случайными значения и вычислим произвидение этих матриц.

![Матрицы и их произведение](17.png){ #fig:002 width=40% }

18. Повторим пример создания единичной матрицы.

![Матрица](18.png){ #fig:002 width=40% }

19. Повторим примеры: вычислим скалярное произведение двух векторов разными способами.

![Скалярное произведение](19.png){ #fig:002 width=40% }

## Факторизация. Специальные матричные структуры

В математике факторизация (или разложение) объекта — его декомпозиция (например, числа, полинома или матрицы) в произведение других объектов или факторов, которые, будучи перемноженными, дают исходный объект.
Матрица может быть факторизована на произведение матриц специального вида для приложений, в которых эта форма удобна. К специальным видам матриц относят ортогональные, унитарные и треугольные матрицы.

20. Повторим пример решение систем линейный алгебраических уравнений 𝐴𝑥 = 𝑏: зададим все начальные условия и найдем решение.

![Начальные условия](20.png){ #fig:002 width=40% }

![Решение](21.png){ #fig:002 width=40% }

21. Вычислим факторизацию: Julia позволяет вычислять LU-факторизацию и определяет составной тип факторизации для его хранения:

![LU-факторизация](22.png){ #fig:002 width=40% }

Различные части факторизации могут быть извлечены путём доступа к их специальным свойствам:
Матрица перестановок:
Alu.P
Вектор перестановок:
Alu.p
Матрица L:
Alu.L
Матрица U:
Alu.U

22. Повторим пример: исходная система уравнений 𝐴𝑥 = 𝑏 может быть решена или с использованием исходной матрицы, или с использованием объекта факторизации:

![Решение](23.png){ #fig:002 width=40% }

23. Повторим пример и найдем детерминат матрицы.

![Детерминат](24.png){ #fig:002 width=40% }

24. Выполним пример: Julia позволяет вычислять QR-факторизацию и определяет составной тип факторизации для его хранения.

![QR-факторизация](25.png){ #fig:002 width=40% }

25. По аналогии с LU-факторизацией различные части QR-факторизации могут быть извлечены путём доступа к их специальным свойствам.

![Q](26.png){ #fig:002 width=40% }

![R](27.png){ #fig:002 width=40% }

![Проверка ортогональности](28.png){ #fig:002 width=40% }

26. Выполним примеры собственной декомпозиции матрицы А, а именно симметризация матрицы A, спектральное разложение симметризованной матрицы, посик собственных значений и векторов.

![Симметризация матрицы A](29.png){ #fig:002 width=40% }

![Спектральное разложение симметризованной матрицы](30.png){ #fig:002 width=40% }

![Собственные значения, векторы и проверка](31.png){ #fig:002 width=40% }

27. Далее рассмотрим примеры работы с матрицами большой размерности и специальной структуры: матрица 1000 х 1000.

![Матрица 1000 х 1000](32.png){ #fig:002 width=40% }

28. Выполним для данной матрицы симметризацию, и проверку на симметрию.

![Симметризация](33.png){ #fig:002 width=40% }

![Проверка](34.png){ #fig:002 width=40% }

29. Выполним пример добавления шума в симметричную матрицу (матрица уже не будет симметричной).

![Добавление шума и проверка](35.png){ #fig:002 width=40% }

30. В Julia можно объявить структуру матрица явно, например, используя Diagonal, Triangular, Symmetric, Hermitian, Tridiagonal и SymTridiagonal.

![Указание на симметричность](36.png){ #fig:002 width=40% }

31. Далее для оценки эффективности выполнения операций над матрицами большой
размерности и специальной структуры воспользуемся пакетом BenchmarkTools, добавим его.

![Добавление пакета](37.png){ #fig:002 width=40% }

32. Выполним оценку эффективности выполнения операции по нахождению собственных значений для различных матриц.

![Оценка эффективности 1](38.png){ #fig:002 width=40% }

![Оценка эффективности 2](39.png){ #fig:002 width=40% }

![Оценка эффективности 3](40.png){ #fig:002 width=40% }

33.  Далее рассмотрим примеры работы с разряженными матрицами большой размерности. Использование типов Tridiagonal и SymTridiagonal для хранения трёхдиагональных матриц позволяет работать с потенциально очень большими трёхдиагональными матрицами. Выполним оценку эффективности.

![Матрица 1000000х1000000](41.png){ #fig:002 width=40% }

![Оценка эффективности](42.png){ #fig:002 width=40% }

34. При попытке задать подобную матрицу обычным способом и посчитать её собственные
значения, мы получим ошибку переполнения памяти.

![Ошибка](43.png){ #fig:002 width=40% }

## Общая линейная алгебра

Обычный способ добавить поддержку числовой линейной алгебры - это обернуть подпрограммы BLAS и LAPACK. Собственно, для матриц с элементами Float32,Float64, Complex {Float32} или Complex {Float64} разработчики Julia использовали такое же решение. Однако Julia также поддерживает общую линейную алгебру, что позволяет, например, работать с матрицами и векторами рациональных чисел.

35. В следующем примере показано, как можно решить систему линейных уравнений с рациональными элементами без преобразования в типы элементов с плавающей запятой (для избежания проблемы с переполнением используем BigInt).

![Матрица с рациональными элементами](44.png){ #fig:002 width=40% }

![Решение и LU-разложение](45.png){ #fig:002 width=40% }

## Задания для самостоятельного выполнения

### Произведение векторов

36. Выполним 1.1 задание: задайте вектор v. Умножьте вектор v скалярно сам на себя и сохраните результат
в dot_v.

![1.1 задание](46.png){ #fig:002 width=40% }

37. Выполним 1.2 задание: умножьте v матрично на себя (внешнее произведение), присвоив результат переменной outer_v.

![1.2 задание](47.png){ #fig:002 width=40% }

### Системы линейных уравнений

38. Выполним 2 задание: Решить СЛАУ с двумя/тремя неизвестными.

![Функция для решения](48.png){ #fig:002 width=40% }

![Функция для решения](49.png){ #fig:002 width=40% }

a) Решение существует (система линейно независима)

$$
\begin{cases}
x+y=2,\\
x-y=3.
\end{cases}
$$

![а)](50.png){ #fig:002 width=40% }

b) Бесконечное количество решений (вся система линейно зависима и коэффициенты и ветокры ответов)

$$
\begin{cases}
x+y=2,\\
2x+2y=4.
\end{cases}
$$

![b)](51.png){ #fig:002 width=40% }

c) Нет решений (матрица коэффициентов линейно зависима, при этом векторы нет)

$$
\begin{cases}
x+y=2,\\
2x+2y=5.
\end{cases}
$$

![c)](52.png){ #fig:002 width=40% }

d) Бесконечное количество решений (вся система линейно зависима)

$$
\begin{cases}
x+y = 1,\\
2x+2y = 2,\\
3x+3y = 3.
\end{cases}
$$

![d)](53.png){ #fig:002 width=40% }

e) Нет решений

$$
\begin{cases}
x+y=2,\\
2x+y=1,\\
x-y=3.
\end{cases}
$$

![e)](54.png){ #fig:002 width=40% }

f) Решение существует

$$
\begin{cases}
x+y=2,\\
2x+y=1,\\
3x+2y=3.
\end{cases}
$$

![f)](55.png){ #fig:002 width=40% }

Решить СЛАУ с тремя неизвестными:

a)

$$
\begin{cases}
x+y+z=2,\\
x-y-2z=3.
\end{cases}
$$

![а)](56.png){ #fig:002 width=40% }

b)

$$
\begin{cases}
x+y+z=2,\\
2x+2y-3z=4,\\
3x+y+z=1.
\end{cases}
$$

![b)](57.png){ #fig:002 width=40% }

c)

$$
\begin{cases}
x+y+z=1,\\
x+y+2z=0,\\
2x+2y+3z=1.
\end{cases}
$$

![c)](58.png){ #fig:002 width=40% }

d)

$$
\begin{cases}
x+y+z=1,\\
x+y+2z=0,\\
2x+2y+3z=0.
\end{cases}
$$

![d)](59.png){ #fig:002 width=40% }

### Операции с матрицами

39. Приведите приведённые ниже матрицы к диагональному виду:

![Функция для решения](60.png){ #fig:002 width=40% }

![а,b,c)](61.png){ #fig:002 width=40% }

- Вычислите:

![Функция для решения](62.png){ #fig:002 width=40% }

![a,b,c,d)](63.png){ #fig:002 width=40% }

- Найдите собственные значения матрицы 𝐴, если:

![A](64.png){ #fig:002 width=40% }

- Создайте диагональную матрицу из собственных значений матрицы 𝐴. Создайте нижнедиагональную матрицу из матрица 𝐴. Оцените эффективность выполняемых операций.

![A из собственных значений](65.png){ #fig:002 width=40% }

### Линейные модели экономики

40. Выполним задание: 1. Матрица 𝐴 называется продуктивной, если решение 𝑥 системы при любой неотрицательной правой части 𝑦 имеет только неотрицательные элементы 𝑥𝑖. Используя это определение, проверьте, являются ли матрицы продуктивными.

![Функция для решения](66.png){ #fig:002 width=40% }

![a,b)](67.png){ #fig:002 width=40% }

![c)](68.png){ #fig:002 width=40% }

41. Выполним задание: 2. Критерий продуктивности: матрица 𝐴 является продуктивной тогда и только тогда, когда все элементы матрица (𝐸 − 𝐴)−1 являются неотрицательными числами. Используя этот критерий, проверьте, являются ли матрицы продуктивными.

![Функция для решения](69.png){ #fig:002 width=40% }

![a,b)](70.png){ #fig:002 width=40% }

![c)](71.png){ #fig:002 width=40% }

42. Выполним задание: Спектральный критерий продуктивности: матрица 𝐴 является продуктивной тогда и только тогда, когда все её собственные значения по модулю меньше 1. Используя этот критерий, проверьте, являются ли матрицы продуктивными.

![a,b)](72.png){ #fig:002 width=40% }

![c,d)](73.png){ #fig:002 width=40% }

# Выводы по проделанной работе

## Вывод

В результате выполнения работы мы изучили возможностей специализированных пакетов Julia для выполнения и оценки эффективности операций над объектами линейной алгебры.
Были записаны скринкасты выполнения , создания отчета, презентации и защиты лабораторной работы.

# Список литературы

- Julia: https://ru.wikipedia.org/wiki/Julia
- https://julialang.org/packages/
- https://juliahub.com/ui/Home
- https://juliaobserver.com/
- https://github.com/svaksha/Julia.jl
