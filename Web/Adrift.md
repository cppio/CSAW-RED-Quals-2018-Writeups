# Adrift
Someone brought up this game from back in high school, and I just HAVE to beat the new version.

[web.chal.csaw.io:10106](http://web.chal.csaw.io:10106)

Note: runs on Python3

[clicker2.0.zip](https://github.com/cppio/CSAW-RED-Quals-2018-Writeups/raw/master/Web/clicker2.0.zip)
## Solution
Looking at `clicker/__init__.py`, we can see that `flag1.txt` is returned if the header `bring_back_random_click` has the same value as a random lowercase letter repeated 10 times is passed to the endpoint `/default/`.

Thus we can repeatedly run
```
curl web.chal.csaw.io:10106/default/ -H 'bring_back_random_click: aaaaaaaaaa'
```
until we see the flag.
### Flag
`flag{wh@t_Ar3_lAt3_b1nDiNg_cl0sUreS}`
