# SameSite Strict bypass via client-side redirect
The lab description describes that we have to find a gadget where client side redirect is made.
First, when logging in, the server sets `Same-Site=Strict` on our session cookie. This means that no cross site requsts can be made.
Enumerating the website, we can observe that when a comment on a post is made, server responds with this header: `Location: /post/comment/confirmation?postId=10`
The confirmation page includes a javascript file `/resources/js/commentConfirmationRedirect.js` which has the following code
```javascript
redirectOnConfirmation = (blogPath) => {
    setTimeout(() => {
        const url = new URL(window.location);
        const postId = url.searchParams.get("postId");
        window.location = blogPath + '/' + postId;
    }, 3000);
}
``` 
This is called like this:
```js
redirectOnConfirmation('/post');
```
Trying to send a GET request to `/post/comment/confirmation?postId=/CustomTest` will redirect us to `/post/CustomTest`

This will allow us to make GET requests to the application while bypassing the `Same-Site: Strict`

Next up, we can try and change the email and observe the POST request that is made. However, trying to change the method to GET and including the email and submit in url params also lets us change the email, which means we have a plan:

1. Send victim to `https://[..]/post/comment/confirmation?postId=../my-account/change-email?email=pwned@evil-user.net&submit=1` (Needs to be url encoded)
2. Victim will be redirects to `/change-email?email=pwned@evil-user.net&submit=1`
3. This will solve the lab.

[Solution](./assets/SameSite%20Strict%20bypass%20via%20client-side%20redirect.html)