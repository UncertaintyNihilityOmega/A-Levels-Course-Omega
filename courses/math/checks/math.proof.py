# checks/math.proof.py: recomputes every number in the Proof chapter.
from fractions import Fraction as F
from math import isqrt, isclose, log2

def isp(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

# warm-up
assert all((2 * n + 1)**2 == 4 * n * n + 4 * n + 1 for n in range(-20, 20))
assert all(n * n + n == n * (n + 1) for n in range(-20, 20))
assert F(36, 99) == F(4, 11) and 99 * F(4, 11) == 36

# the n^2 + n + 41 story
assert [n * n + n + 41 for n in (1, 2, 3, 4, 5, 10)] == [43, 47, 53, 61, 71, 151]
assert all(isp(n * n + n + 41) for n in range(0, 40)) and not isp(40 * 40 + 40 + 41) and 40 * 40 + 40 + 41 == 1681 == 41 * 41
assert all(isp(n * n + n + 41) for n in range(1, 11))
assert not isp(41 * 41 + 41 + 41) and 41 * 41 + 41 + 41 == 41 * 43

# deduction
for a in range(-6, 7):
    for b in range(-6, 7):
        assert (2 * a + 1) + (2 * b + 1) == 2 * (a + b + 1)
        assert (2 * a + 1) * (2 * b + 1) == 2 * (2 * a * b + a + b) + 1
for n in range(-30, 30):
    assert (2 * n + 1)**2 == 4 * n * (n + 1) + 1 and (n * (n + 1)) % 2 == 0 and (2 * n + 1)**2 % 8 == 1
    assert (n + 1)**2 - (n - 1)**2 == 4 * n
    assert (n + 3)**2 - (n - 1)**2 == 8 * (n + 1)
    assert n + (n + 1) + (n + 2) == 3 * (n + 1)
    assert (2 * n + 1) + (2 * n + 3) == 4 * (n + 1)
assert 7**2 == 6 * 8 + 1

# exhaustion: squares mod 3
for k in range(-20, 20):
    assert (3 * k)**2 == 3 * (3 * k * k)
    assert (3 * k + 1)**2 == 3 * (3 * k * k + 2 * k) + 1
    assert (3 * k + 2)**2 == 3 * (3 * k * k + 4 * k + 1) + 1
assert all((n * n) % 3 in (0, 1) for n in range(-50, 50))

# counter-examples
assert 2 + 3 == 5 and isp(2) and isp(3) and not (5 % 2 == 0)
assert isp(7) and not isp(9) and 9 == 3 * 3
assert F(1, 2)**2 < F(1, 2)
assert not isp(2**3 + 1) and isp(2 + 1) and isp(2**2 + 1)
assert not (1**2 > 2 * 1) and not (2**2 > 2 * 2)
# sqrt2 + (3 - sqrt2) = 3
from math import sqrt
assert isclose(sqrt(2) + (3 - sqrt(2)), 3, abs_tol=1e-12)
# n^2 - n + 11
assert all(isp(n * n - n + 11) for n in range(1, 11)) and not isp(11 * 11 - 11 + 11) and 11 * 11 - 11 + 11 == 121

# contradiction
assert not any(p * p == 2 * q * q for p in range(1, 600) for q in range(1, 600))
assert not any(p * p == 3 * q * q for p in range(1, 600) for q in range(1, 600))
assert not any(p * p == 5 * q * q for p in range(1, 600) for q in range(1, 600))
assert all((n * n) % 2 == n % 2 for n in range(-30, 30))                       # n^2 even iff n even
assert all(((3 * k + 1)**2) % 3 == 1 and ((3 * k + 2)**2) % 3 == 1 for k in range(-20, 20))   # for sqrt3
assert all(((5 * k + r)**2) % 5 != 0 for k in range(-10, 10) for r in (1, 2, 3, 4))            # for sqrt5
primes = [2, 3, 5, 7, 11, 13]; N = 1
for p in primes: N *= p
N += 1
assert N == 30031 == 59 * 509 and isp(59) and isp(509) and not isp(N) and all(N % p == 1 for p in primes)

# induction taste: 2^n >= n + 1
assert all(2**n >= n + 1 for n in range(1, 60)) and 2**1 == 2 == 1 + 1
assert all(2 * (k + 1) >= k + 2 for k in range(0, 60))

# spot the error is about structure, no numbers

# try and exam practice
assert all((n**3 - n) % 6 == 0 and n**3 - n == (n - 1) * n * (n + 1) for n in range(1, 80))
assert all(((2 * a + 1)**2 + (2 * b + 1)**2) % 4 == 2 for a in range(-8, 8) for b in range(-8, 8))
assert all(isqrt(((2 * a + 1)**2 + (2 * b + 1)**2))**2 != (2 * a + 1)**2 + (2 * b + 1)**2 for a in range(0, 30) for b in range(0, 30))
assert all((2 * m)**2 % 4 == 0 and (2 * m + 1)**2 % 4 == 1 for m in range(-20, 20))
for x in (-5, 0, 3, 7.5): assert x * x - 6 * x + 10 == (x - 3)**2 + 1 > 0
assert 3 * 3 - 18 + 8 == -1
for n in range(1, 60):
    assert n * (n + 1) * (n + 2) * (n + 3) + 1 == (n * n + 3 * n + 1)**2
    m = n * n + 3 * n; assert n * (n + 3) == m and (n + 1) * (n + 2) == m + 2 and m * (m + 2) + 1 == (m + 1)**2
assert 1 * 2 * 3 * 4 + 1 == 25 == 5**2 and 1 + 3 + 1 == 5
assert log2(3) > 0 and all(2**p != 3**q for p in range(1, 60) for q in range(1, 40)) and all(2**p % 2 == 0 and 3**q % 2 == 1 for p in range(1, 20) for q in range(1, 20))
print("ok")
