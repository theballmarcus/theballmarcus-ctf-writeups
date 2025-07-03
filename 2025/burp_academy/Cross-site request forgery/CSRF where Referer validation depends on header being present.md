# CSRF where Referer validation depends on header being present
Very basic, just add the following to avoid referer header.
```html
<meta name="referrer" content="never">
```
After that, just perform a simple csrf attack.
[Solution](./assets/CSRF%20where%20Referer%20validation%20depends%20on%20header%20being%20present.html)