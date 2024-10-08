## Ход ладьи

Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом.

Программа получает на вход четыре числа от 1 до 8 каждое.
Первые 2 числа задают номер столбца и номер строки для первой клетки, вторые 2 числа - для второй клетки.

<img src="/img/problem4.2.10.png" alt="Ход ладьи" width="400">

<br>

### *Тестовые данные:*

| Номер теста | Входные данные   | Выходные данные |
|:-----------:|------------------|-----------------|
|      1      | 4<br>4<br>5<br>4 | YES             |
|      2      | 4<br>4<br>5<br>5 | NO              |
|      3      | 4<br>4<br>4<br>5 | YES             |
|      4      | 4<br>4<br>5<br>3 | NO              |
|      5      | 4<br>4<br>3<br>5 | NO              |
|      6      | 4<br>4<br>3<br>4 | YES             |
|      7      | 1<br>1<br>1<br>8 | YES             |
|      8      | 1<br>1<br>8<br>8 | NO              |
|      9      | 1<br>1<br>8<br>1 | YES             |
|     10      | 1<br>8<br>8<br>1 | NO              |
|     11      | 1<br>8<br>1<br>1 | YES             |
|     12      | 1<br>2<br>3<br>1 | NO              |
|     13      | 4<br>4<br>4<br>3 | YES             |
|     14      | 1<br>8<br>8<br>8 | YES             |
|     15      | 8<br>8<br>8<br>1 | YES             |
|     16      | 8<br>8<br>1<br>1 | NO              |
|     17      | 8<br>8<br>1<br>8 | YES             |
|     18      | 8<br>1<br>1<br>1 | YES             |
|     19      | 8<br>1<br>8<br>8 | YES             |
|     20      | 1<br>1<br>1<br>2 | YES             |
|     21      | 1<br>1<br>2<br>1 | YES             |
|     22      | 4<br>4<br>6<br>6 | NO              |
|     23      | 4<br>4<br>4<br>6 | YES             |
|     24      | 4<br>4<br>2<br>4 | YES             |
|     25      | 1<br>2<br>1<br>3 | YES             |
|     26      | 2<br>1<br>1<br>3 | NO              |
|     27      | 4<br>4<br>3<br>3 | NO              |
|     28      | 8<br>1<br>1<br>8 | NO              |
|     29      | 1<br>1<br>2<br>2 | NO              |
|     30      | 4<br>4<br>2<br>2 | NO              |
|     31      | 4<br>4<br>6<br>2 | NO              |
|     32      | 4<br>4<br>2<br>7 | NO              |