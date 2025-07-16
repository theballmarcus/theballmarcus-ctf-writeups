# Client-side prototype pollution via flawed sanitization
This lab looks like the former ones. However, we know there is flawed sanitization. First, I tried `&__pro__proto__to__.foo=bar` in the url which didn't give me anything. Then I tried `tets&__pro__proto__to__.foo=bar?` which helped me find my source. 
Then I found the sink - exactly the same as in [lab 1](./DOM%20XSS%20via%20client-side%20prototype%20pollution.md)
Final payload: `https://0ac9003a036a19ff804a08d4005f00d0.web-security-academy.net/?search=tets&__pro__proto__to__[transport_url]=data:,alert(1)`