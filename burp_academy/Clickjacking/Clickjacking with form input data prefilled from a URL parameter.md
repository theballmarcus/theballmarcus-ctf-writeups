# Clickjacking with form input data prefilled from a URL parameter
To solve this one, first, we have to dicsover that setting url parameter email will prefill the submission form. From there, make an iframe element which shows the user its home page. 
Then make a button and align it on top of the change email account account button.
Then make the iframe practically invisible so the user doesn't see it.
Then deliver to the victim. Here is a page that does that:
[Soltion html](./assets/Clickjacking%20with%20form%20input%20data%20prefilled%20from%20a%20URL%20parameter.html)