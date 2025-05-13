---
## Front matter
lang: ru-RU
title: Лабораторная работа 6
## subtitle: Простейший шаблон
author:
  - Тагиев Б. А.
institute:
  - Российский университет дружбы народов, Москва, Россия
date: 12 апреля 2023

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
figureTitle: "Рис."
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
mainfont: DejaVu Serif
romanfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
---

## Цель работы

Целью данной работы является построение модели хищник-жертва.

## Выполнение лабораторной работы

1. Реализуем модель на xcos. Добавим необходимые блоки.

![Модель «хищник–жертва» в xcos](./image/0.png){width=60%}

## Выполнение лабораторной работы

2. Зададим начальные условия на блоках интегрирования.

![Начальное значение 1](./image/1.png){width=70%}

## Выполнение лабораторной работы

![Начальное значение 2](./image/2.png){width=70%}

## Выполнение лабораторной работы

3. Запустив, мы увидим два графика.

![График изменения численности хищников и численности жертв](./image/3.png){width=70%}

## Выполнение лабораторной работы

![График зависимости численности хищников от численности жертв](./image/4.png){width=70%}

## Выполнение лабораторной работы

4. Перейдем к реализации с блоком modelica. Сдеалаем следующую схему.

![Модель «хищник–жертва» в xcos](./image/7.png){width=50%}

## Выполнение лабораторной работы

5. Добавим "исходный код в наш блок".

![Код](./image/6.png){width=40%}

## Выполнение лабораторной работы

6. Запустив получим аналогичные графики, как и в 3 пунтке.

## Выполнение лабораторной работы

7. Перейдем к OpenModelica. Далее представлен листинг программы.

## Выполнение лабораторной работы

```modelica
model m1
parameter Real a=2,b=1,c=0.3,d=1;
Real x(start=2), y(start=1);
equation
der(x)=a*x-b*x*y;
der(y)=c*x*y-d*y;
annotation(
    experiment(StartTime = 0, StopTime = 30, Tolerance = 1e-6, Interval = 0.06));
end m1;
```

## Выполнение лабораторной работы

8. Запустив, получим следующие графики.

![График изменения численности хищников и численности жертв](./image/9.png){width=70%}

## Выполнение лабораторной работы

![График зависимости численности хищников от численности жертв](./image/10.png){width=70%}

## Выводы

Мы реализовали модель "Хищник-жертва" в xcos, modelica и OpenModelica.

