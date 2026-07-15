package main

import (
	"fmt"
)

func program(zero uint16, one uint16) {
	a := zero
	b := one

	var c uint16 = 23
	var d uint16 = 43
	var e uint16 = 32
	var f uint16 = 2
	var g uint16 = 39
	var h uint16 = 24
	var i uint16 = 0
	var j uint16 = 0
	var k uint16 = 0
	var l uint16 = 0
	var m uint16 = 0
	var n uint16 = 0
	var o uint16 = 0
	var p uint16 = 16

L0:
	b += c
	d++
	a = a + d - e
	if p == 0 {
		a = 0
	} else {
		a = a % p
	}
	if a != 0 {
		goto L5
	}
L1:
	b += d
	m = b * b
	d = d + m + e
	if d != 0 {
		goto L9
	}
L2:
	h = d
	if p == 0 {
		h = 0
	} else {
		h = h % p
	}
	if h == 0 {
		goto L4
	}
L3:
	i = d * d
	j = i + e
	if p == 0 {
		k = 0
	} else {
		k = j % p
	}
	a = a - k
	if a != 0 {
		goto L20
	}
L4:
	l = h * h
	d = l + e + c
	if l != 0 {
		goto L8
	}
L5:
	a = a + p - c
	if c != 0 {
		goto L1
	}
L6:
	if a == 0 {
		c = 0
	} else {
		c = c % a
	}
	if e != 0 {
		goto L19
	}
L7:
	g = g - a
	e = e - c
	if g == 0 {
		goto L6
	}
	goto L9
L8:
	e = e + 1
	p = p - 1
	if p != 0 {
		goto L7
	}
L9:
	a = a + e - d
	if a == 0 {
		goto L15
	}
L10:
	p = b * b + c
	c = k - c + p
	if e == 0 {
		p = 0
	} else {
		p = p % e
	}
	if p != 0 {
		goto L18
	}
L11:
	f = d * d + c
	if e == 0 {
		f = 0
	} else {
		f = f % e
	}
	if f != 0 {
		goto L3
	}
L12:
	a = a + p - f
	goto L21
L13:
	c = c + e
	d = d - p
	if c != 0 {
		goto L10
	}
L14:
	e = e + f
	b -= c
	if e != 0 {
		goto L11
	}
L15:
	c += d
	p -= e
	if c != 0 {
		goto L12
	}
L16:
	e += a
	f -= p
	if e == 0 {
		goto L13
	}
L17:
	p += b
	d -= f
	if p != 0 {
		goto L14
	}
L18:
	f += c
	a -= d
	if f != 0 {
		goto L16
	}
L19:
	d += e
	c -= a
	if d != 0 {
		goto L17
	}
L20:
	n = a - f
	if c == 0 {
		o = 0
	} else {
		o = n % c
	}
	a += o
	if a == 0 {
		goto L0
	}
L21:
	n = p - d
	if e == 0 {
		o = 0
	} else {
		o = n % e
	}
	c += o
	a += o
	n = b - c
	if g == 0 {
		o = 0
	} else {
		o = n % g
	}
	if n != 0 {
		goto L2
	}

	fmt.Println(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)
}

func main() {
	program(uint16(0), uint16(0))
}
