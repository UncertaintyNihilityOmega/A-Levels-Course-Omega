# data/cs.float_model.py: exact reference model of the Cambridge floating-point format (Fractions only).
# Used by checks/cs.float.py (copied there), by data/cs-float.test.js (through JSON) and for chapter numbers.
from fractions import Fraction as F
import math


def twos(bits):
    v = int(bits, 2)
    return v - (1 << len(bits)) if bits[0] == "1" else v


def mantissa_value(mbits):
    return F(twos(mbits), 1 << (len(mbits) - 1))


def value(mbits, ebits):
    return mantissa_value(mbits) * F(2) ** twos(ebits)


def is_normalised(mbits):
    return len(mbits) >= 2 and mbits[0] != mbits[1]


def limits(m, e):
    emax, emin = (1 << (e - 1)) - 1, -(1 << (e - 1))
    big = F((1 << (m - 1)) - 1, 1 << (m - 1))
    return {
        "largest": big * F(2) ** emax,
        "smallest": F(1, 2) * F(2) ** emin,
        "most_negative": F(-1) * F(2) ** emax,
        "least_negative": F(-((1 << (m - 2)) + 1), 1 << (m - 1)) * F(2) ** emin,
    }


def to_bits(n, width):
    return format(n & ((1 << width) - 1), f"0{width}b")


def encode(x, m, e):
    """Nearest normalised pattern. Returns (mbits, ebits, status); status in ok, overflow, underflow, zero."""
    x = F(x)
    if x == 0:
        return "0" * m, "0" * e, "zero"
    emax, emin = (1 << (e - 1)) - 1, -(1 << (e - 1))
    neg = x < 0
    a = abs(x)
    # exponent E with y = a / 2^E in [1/2, 1) (positive) or (1/2, 1] (negative)
    E = a.numerator.bit_length() - a.denominator.bit_length()
    while F(2) ** E < a:
        E += 1
    while F(2) ** (E - 1) >= a:
        E -= 1
    # now 2^(E-1) <= a < 2^E
    if neg and a == F(2) ** (E - 1):
        E -= 1            # exact power of two: y = 1, mantissa -1
    y = a / F(2) ** E
    scaled = y * (1 << (m - 1))
    N = math.floor(scaled + F(1, 2))
    if not neg:
        if N == (1 << (m - 1)):
            N, E = 1 << (m - 2), E + 1
        mant = N
    else:
        if N == (1 << (m - 2)):
            N, E = 1 << (m - 1), E - 1
        mant = -N
    if E > emax:
        return None, None, "overflow"
    if E < emin:
        return "0" * m, "0" * e, "underflow"
    return to_bits(mant, m), to_bits(E, e), "ok"


def normalise_steps(mbits, ebits):
    steps = []
    e = twos(ebits)
    emin = -(1 << (len(ebits) - 1))
    while not is_normalised(mbits) and "1" in mbits.replace(mbits[0], "") + ("1" if mbits[0] == "1" else ""):
        if mbits == "0" * len(mbits):
            break
        if e - 1 < emin:
            steps.append("blocked")
            break
        mbits, e = mbits[1:] + "0", e - 1
        ebits = to_bits(e, len(ebits))
        steps.append((mbits, ebits))
    return steps


if __name__ == "__main__":
    for mb, eb in [("01011000", "0011"), ("10110000", "0010"), ("01100000", "1110"), ("10100000", "1101"),
                   ("01100100", "0011"), ("10010000", "0010"), ("01010000", "1110"), ("10000000", "0010"), ("10110000", "1111")]:
        print(mb, eb, mantissa_value(mb), twos(eb), value(mb, eb), float(value(mb, eb)), is_normalised(mb))
    for x in [F("6.25"), F("-3.5"), F("0.15625"), F(-4), F("-0.3125"), F("0.1"), F("100"), F("-100"), F(300), F("0.001")]:
        print(x, encode(x, 8, 4))
    print(limits(8, 4))
    for m, e in [(8, 4), (9, 3), (7, 5), (10, 6)]:
        L = limits(m, e)
        print(m, e, {k: (str(v), float(v)) for k, v in L.items()})
