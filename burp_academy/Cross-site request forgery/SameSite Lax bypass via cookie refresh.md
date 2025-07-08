# SameSite Lax bypass via cookie refresh
By enumeration, this is the interesting takeaways:
1. Going to `/social-login` will automaticly login if I have been logged in before. Observe that it refreshes the session cookie. For 120 seconds after that, the cookie is vulnerable because SameSite: Lax doesn't apply until 120 seconds after.
2. There is no csrf protection on the email form. 
3. The issued cookie does not have any SameSite restrictions which means it will default to Lax

Therefore, by first making the victim go to [the first site](./assets/SameSite%20Lax%20bypass%20via%20cookie%20refresh.html) will refresh the cookie - and after that make the victim visit [the second site](assets/SameSite%20Lax%20bypass%20via%20cookie%20refresh_2.html) which will update the email.