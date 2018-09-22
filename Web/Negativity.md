# Negativity
People say that I'm too negative. I say that sometimes you need negativity to grow.

[web.chal.csaw.io:10106](http://web.chal.csaw.io:10106)

Note: runs on Python3

[clicker2.0.zip](https://github.com/cppio/CSAW-RED-Quals-2018-Writeups/raw/master/Web/clicker2.0.zip)
## Solution
Looking at `clicker/__init__.py`, we can see that `flag2.txt` is returned if `/money` is requested and the user has negative money. The only way to lose money is to purchase a clicker. Looking at `purchase_clicker` in `clicker/service/user_click.py`, it will only let you purchase if
```python3
round(money - price) >= 0
```
and when afterwards it changes
```python3
money -= round(price)
```
Now if price has a fractional part of 0.5, we can arrive at a situation where `round(money - price)` rounds up, and `round(price)` rounds up as well. In Python, `round` rounds to the nearest even.

We can create an example of a way to get negative numbers:
```python3
money = 1
price = 1.5
round(money - price) = round(-0.5) = 0
money - round(price) = 1 - 2 = -1
```
And so for any odd amount of money, if we buy something with a price of 0.5 more, we will end up with negative money. Now looking at how `price` is calculated:
```python3
clicker['price'] * (clicker['scale'] ** quantity)
```
we can see that price scales with the amount you own. Looking at [web.chal.csaw.io:10106/clicker/](http://web.chal.csaw.io:10106/clicker/), scale is always 1.15. To get .5, we can multiply scale by 10, so quantity should be 1 and price should be 10, which 'momo' fits. Thus, if we have 11 money and we buy a second 'momo', we would have negative money.

One important thing to consider before attempting this is that in `clicker/controller/clicker.py`, `UseClicker` is rate-limited to twice a second.

The script is available [here](https://github.com/cppio/CSAW-RED-Quals-2018-Writeups/blob/master/Web/negativity.py). It requires the [python requests](http://python-requests.org/) library.
### Flag
`flag{d1d_u_eXp3r1ence_gr0wTh}`
