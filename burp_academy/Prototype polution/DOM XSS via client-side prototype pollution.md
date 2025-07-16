# DOM XSS via client-side prototype pollution
First, I enumerated the different features on the website to get a complete site map. After that, I looked at the different javascript files.
Here, we can find `deparam.js`, `searchLogger.js`, and `submitFeedback.js`
While inspecting them, I found a possible sink. In `searchLogger.js`, config.transport_url is used to set a src of a script tag - however it is not explicitly set. That means that if we find a way to set a prototype property - we can overwrite this. 
While looking at `deparam.js`, I found that we can just set prototype properties using the url. We can just set `__proto__[abc]=def` which will be reflected if we then, in the dev console, write `Object.prototype`.
So - the final url payload is as follows:

`https://0ab200eb039dc00580cde91d0023001a.web-security-academy.net/?search=asd&__proto__[transport_url]=data:,alert(1)`
