1.2 Sistem Persamaan Linear
Menghitung dan mempelajari solusi persamaan, serta sistem persamaan, tanpa diragukan lagi memainkan peran penting dalam matematika; meskipun kami segera menambahkan bahwa ini bukan satu-satunya hal yang dilakukan para matematikawan! Dalam bab ini, kita akan mengembangkan teori yang pada dasarnya lengkap untuk persamaan matematis yang relatif sederhana: yaitu, persamaan linear.
Hal ini akan menjadi pengantar secara tidak langsung bagi studi aljabar linear kita, karena di balik deskripsi parametrik solusi sistem linear tersirat konsep-konsep ruang vektor seperti subruang, rentangan (span), dan kebebasan linear.

1.2.1 Sistem Persamaan Linear
Definition 1.2.1. Persamaan Linear.  Sebuah ekspresi linear dalam 
peubah tak diketahui (atau variabel) $x_1,x_2, \cdots ,x_n$ adalah ekspresi berbentuk
$a_1x_1 + a_2x_2 + \cdots + a_nx_n,$
dengan $a_1,a_2,...a_n$ adalah bilangan real tetap.
Sebuah persamaan linear dalam peubah $x_1,x_2,..x_n$ adalah persamaan yang dapat disederhanakan—hanya menggunakan penjumlahan dan pengurangan—menjadi bentuk
$a_1x_1+a_2x_2+...=a_nx_n = b,
Diberikan suatu persamaan linear dalam bentuk baku (1.2.1), persamaan tersebut disebut homogen jika,b = 0 dan nonhomogen jika $b \neq 0$ .
Example 1.2.2. Persamaan Linear dan Nonlinear.
1. Tinjau $\sqrt{3}x + \sin(5) = 2z - e^{4}y$.Ini adalah persamaan linear dalam peubah x,y,z
Bentuk bakunya adalah sqrt(3)x + e^(4)y - 2z = -sin(5)Karena ruas kanannya tak nol, persamaan ini bersifat nonhomogen.
2. Persamaan $x^{2}y$ + y^{2}$ = 1 adalah persamaan nonlinear dalam peubah x dan y.
Definition 1.2.3. Sistem Persamaan Linear.  Sebuah sistem persamaan linear (atau sistem linear) adalah himpunan persamaan linear.
Definition 1.2.3. Sistem Persamaan Linear. Sebuah sistem linear disebut homogen jika seluruh persamaannya homogen.Saat menampilkan sistem yang terdiri atas m persamaan dalam n peubah
$x_1,x_2,...a_n$ biasanya kita menuliskan setiap persamaan dalam bentuk baku dan menyelaraskan suku-suku yang bersesuaian ke dalam kolom. 
Remark 1.2.4.  Anda perlu segera membiasakan diri dengan notasi indeks ganda yang digunakan untuk menampilkan sistem linear. Berikut cara memahaminya:
Indeks $i$ pada $a_i_j$ menunjukkan baris ke- $i$ dalam sistem yang ditampilkan, atau secara ekuivalen, persamaan ke- $i$ Indeks $j$ pada $a_i_j$ menunjukkan kolom ke- $j$,menunjukkan kolom ke- $j$, untuk $1 \leq j \leq n$.
Definition 1.2.5. Solusi Sistem Linear.  Sebuah solusi persamaan linear
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
\vdots & \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n &= b_m
\end{cases} 
adalah sebuah $n$ -tuple $(s_1, s_2, \dots, s_n)$. yang merupakan solusi dari masing-masing $m$ persamaan dalam sistem tersebut. Kita katakan bahwa $(s_1, s_2, \dots, s_n)$.  memecahkan sistem tersebut.
Example 1.2.6. Solusi Sistem Elementer.  Untuk tiap sistem berikut, tentukan himpunan solusinya.
\begin{cases}
x - y = 0 \\
x - y = 1
\end{cases}
1.2.1.1 Representasi Matriks dari Sistem Linear
Definition 1.2.7. Representasi Matriks dari Sistem Linear. 
 Jika $A$
 adalah matriks koefisien dari suatu sistem persamaan linear dan $B$
 adalah vektor konstanta, maka kita akan menuliskan $LS$ ($A,b) 
 sebagai ungkapan singkat untuk sistem persamaan linear tersebut, yang akan kita sebut sebagai representasi matriks dari sistem linear.
 Example 1.2.8. Notasi untuk sistem persamaan linear.  Sistem persamaan linear
\documentclass{article}
\usepackage{amsmath}
\begin{document}

$$\begin{matrix}2x_{1}+4x_{2}-3x_{3}+5x_{4}+x_{5}=9\\ 3x_{1}+x_{2}+x_{4}-3x_{5}=0\\ -2x_{1}+7x_{2}-5x_{3}+2x_{4}+2x_{5}=-3\end{matrix}$$

Memiliki matriks koefisien 
A = \begin{bmatrix}
2 & 4 & -3 & 5 & 1 \\
3 & 1 & 0 & 1 & -3 \\
-2 & 7 & -5 & 2 & 2
\end{bmatrix}
dan vektor konstanta
b = \begin{bmatrix} 9 \\ 0 \\
dan sehingga akan direferensikan sebagai $LS$ ($A,b$)
Definition 1.2.9. Matriks Augmentasi.
Matriks augmentasi merepresentasikan semua informasi penting dalam sistem persamaan, karena nama-nama variabel telah diabaikan, dan satu-satunya koneksi dengan variabel adalah lokasi koefisien mereka dalam matriks. Perlu diperhatikan bahwa matriks augmentasi hanyalah sebuah matriks, dan bukan sistem persamaan. Namun, matriks augmentasi selalu terkait dengan suatu sistem persamaan, dan sebaliknya.
Example 1.2.10. Matriks augmentasi.  Berikut adalah sistem berikut dengan 3 persamaan dalam 3 variabel.
\begin{cases}
x_1 - x_2 + 2x_3 = 1 \\
2x_1 + x_2 + x_3 = 8 \\
x_1 + x_2 = 5
\end{cases}
Berikut adalah matriks augmentasinya.
\left[
\begin{array}{ccc|c}
1 & -1 & 2 & 1 \\
2 & 1 & 1 & 8 \\
1 & 1 & 0 & 5
\end{array}
\right]
Computation 1.2.11. Matriks Augmentasi.  Sage memiliki metode matriks, .augment(), yang akan menggabungkan dua matriks, berdampingan asalkan keduanya memiliki jumlah baris yang sama. Metode yang sama akan memungkinkan Anda untuk mengaugmentasi matriks dengan vektor kolom, seperti yang dijelaskan dalam Definition 1.2.9, asalkan jumlah entri dalam vektor sesuai dengan jumlah baris untuk matriks. 
A = matrix(QQ, 3, 3, [[1, -1, 2],
                      [2,  1, 1],
                      [1,  1, 0]])
b = vector(QQ, [1, 8, 5])
M = A.augment(b)
M

$$x_1 + x_2 + x_3 + x_4 + x_5 = 15$$
$$2x_1 + x_2 + x_3 + x_4 + x_5 = 16$$
$$2x_1 + 2x_2 + x_3 + x_4 + x_5 = 18$$
$$2x_1 + 2x_2 + 2x_3 + x_4 + x_5 = 21$$
$$2x_1 + 2x_2 + 2x_3 + 2x_4 + x_5 = 25$$

$$
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 | 15\\
2 & 1 & 1 & 1 & 1 | 16\\
2 & 2 & 1 & 1 & 1 | 18\\
2 & 2 & 2 & 1 & 1 | 21\\
2 & 2 & 2 & 2 & 1 | 25\\
\end{bmatrix}
$$

$$R_2 = R_2 - 2R_1$$
$$R_3 = R_3 - 2R_1$$
$$R_4 = R_4 - 2R_1$$
$$R_5 = R_5 - 2R_1$$

(2,1,1,1,1|16) -2(1,1,1,1,1|15)
= (0, -1, -1, -1, -1| -14)

(2,2,1,1,1|18) -2(1,1,1,1,1|15)
=(0,0, -1, -1, -1| -12)

(2,2,2,1,1|21) -2(1,1,1,1,1|15)
=(0,0,0, -1, -1|-9)

(2,2,2,2,1|25) -2(1,1,1,1,1|15)
=(0,0,0,0, -1| -5)

$$
\begin{bmatrix}
1 & 1 & 1 & 1 &1 | 15\\
2 &-1 &-1 &-1 &-1 |-14\\
2 & 2 & 1 & 1 &-1 |-12\\
0 & 0 & 0 & -1 &-1 |-9\\
0 & 0 & 0 & 0 & -1 |-5\\
\end{bmatrix}
$$

-X_5 = -5
X_5 = 5

-X_4`- X_5 = -9
-X_4 - 5 = -9 
X_4 = 4

-X_3 - X_4 - X_5 = 12
-X_3 - 4 - = - 12
X_3 = 3

-X_2 - X_3 - X_4 - X_5 = -14
X_2 - 3 - 4 - 5 = - 14
X_2 = 2

X_1 + X_2 + X_3 + X_4 + X_5 = 15
X_1 + 2 + 3 + 4 + 5 = 15
X_1 = 1

X_1 = 1, X_2 = 2, X_3 = 3,  X_4 = 4,  X_5 = 5

$$R_2 = R_2 - 2R_1$$
$$R_3 = R_3 - 2R_1$$
$$R_4 = R_4 - 2R_1$$
$$R_5 = R_5 - 2R_1$$