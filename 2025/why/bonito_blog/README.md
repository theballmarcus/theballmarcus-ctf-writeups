# bonito blog writeup

## Description
```We created a blog, now go write your life story like everyone else!``` 

## Points: **100**

## Solutions: **8%** of players

## Solution
so initial though, there is a blog, where we can create a user, grant users priviliges to our blog post (which is by default public). I started by enumerating the website and discovered `/server-status` in the root. However - we didnt have access to this. I tried a couple of CVE's for the apache version which was sent to us in response headers.
This did not work. After that, I tried to fire gobuster on the `/blog/FUZZ`. I discovered post with id 4, which was from admin, and said that we shouldn't try to access the hidden pages. I let gobuster run and saw that `/blog/1337` sent back `403 unauthorized`. This is interesting. I then copied the the request that grants users priviliges to a post and changed `postID` param to 1337 and user to `theball` which was my username. After that, I could access the post, where a flag was stored.

