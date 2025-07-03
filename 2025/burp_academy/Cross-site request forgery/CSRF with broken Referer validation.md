# CSRF with broken Referer validation
First, add the header to the server to avoid it stripping away the malicious url
`Referrer-Policy: unsafe-url`
Then set the exploit file to something that includes the referer. I did `/exploit/0a3b00a40301de24804e030d00b10079.web-security-academy.net`
Then the referer will include the site.
From there on, it's a very basic exploit.
[Solution](./assets/CSRF%20with%20broken%20Referer%20validation.html)