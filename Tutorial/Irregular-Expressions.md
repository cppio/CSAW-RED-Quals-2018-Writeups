# Irregular Expressions
Can you find the flag in one of these files? Ctrl-F may not be enough.

[hello.zip](https://github.com/cppio/CSAW-RED-Quals-2018-Writeups/raw/master/Tutorial/hello.zip)
## Solution
We know that the flag is in the format `flag{_____}`. Thus we can find the flag by running
```bash
fgrep 'flag{' *.txt
```
### Flag
`flag{jus7_@_r3gul4r_flag}`
