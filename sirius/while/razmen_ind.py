'''Выдача сдачи
Имеется неограниченное количество монет в 1, 2, 5, 10 рублей. 
Определите, сколькими способами можно выдать сдачу в n рублей. 
Например, 5 рублей можно выдать четырьмя способами: 
5=2+2+1=2+1+1+1=1+1+1+1+1.
Входные данные
Программа получает на вход натуральное число n, не превышающее 10^6.
Выходные данные
Выведите ответ на задачу.
Примеры
Ввод
    Вывод
2
    2
5
    4

3

Aryabhatta’s answer for counting the number of ways to make change 
with coins of fixed denominations is very cute but also impractical 
to implement as described. Rather than use complex numbers, we’ll 
use modular arithmetic, similar to how the number-theoretic transform 
replaces a Fourier transform for multiplying integer polynomials.

Let D be the least common multiple of the coin denominations. By 
Dirichlet’s theorem on arithmetic progressions, there exist infinitely 
many prime numbers p such that D divides p - 1. (With any luck, they’ll 
even be distributed in a way such that we can find them efficiently.) 
We’ll compute the number of ways modulo some p satisfying this condition. 
By obtaining a crude bound somehow (e.g., n + k - 1 choose k - 1 where 
n is the total and k is the number of denominations), repeating this 
procedure with several different primes whose product exceeds that bound, 
and applying the Chinese remainder theorem, we can recover the exact 
number.

Test candidates 1 + k*D for integers k > 0 until we find a prime p. Let 
g be a primitive root modulo p (generate candidates at random and apply 
the standard test). For each denomination d, express the polynomial 
x**d - 1 modulo p as a product of factors:

x**d - 1 = product from i=0 to d-1 of (x - g**((p-1)*i/d)) [modulo p].
Note that d divides D divides p-1, so the exponent indeed is an integer.

Let m be the sum of denominations. Gather all of the constants 
g**((p-1)*i/d) as a(0), ..., a(m-1). The next step is to find a partial 
fraction decomposition A(0), ..., A(m-1) such that

sign / product from j=0 to m-1 of (a(j) - x) =
    sum from j=0 to m-1 of A(j)/(a(j) - x) [modulo p],
where sign is 1 if there are an even number of denominations and -1 if 
there are an odd number of denominations. Derive a system of linear 
equations for A(j) by evaluating both sides of the given equation for 
different values of x, then solve it with Gaussian elimination. Life 
gets complicated if there are duplicates; it's probably easiest just 
to pick another prime.

Given this setup, we can compute the number of ways (modulo p, of 
course) to make change amounting to n as

sum from j=0 to m-1 of A(j) * (1/a(j))**(n+1).
'''

# Recursive Python3 program for 
# coin change problem. 
  
# Returns the count of ways we can sum 
# S[0...m-1] coins to get sum n 
def count(S, m, n ): 
  
    # If n is 0 then there is 1 
    # solution (do not include any coin) 
    if (n == 0): 
        return 1
  
    # If n is less than 0 then no 
    # solution exists 
    if (n < 0): 
        return 0; 
  
    # If there are no coins and n 
    # is greater than 0, then no 
    # solution exist 
    if (m <=0 and n >= 1): 
        return 0
  
    # count is sum of solutions (i)  
    # including S[m-1] (ii) excluding S[m-1] 
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] ); 
  
# Driver program to test above function 
arr = [1, 2, 5, 10] 
m = len(arr) 
n = int(input())
print(count(arr, m, n)) 
  
# This code is contributed by Smitha Dinesh Semwal 
