# Detecting server-side prototype pollution without polluted property reflection
To solve the lab, we have to make a change to the server bahavior that is non-destructive but noticable. First, I tried changing the "json spaces" variable to see what the server responds with.
```json
"__proto__" : {
    "json spaces" :  4
}
```
I could see this changed the spaces and it solved the lab.
