Subject: [DREAM Challenge Submission] "Just Cat The Moon" by theballmarcus & vbjorn

To: **developers+dream@ncr.ntnu.no**

Dear CTF Development Team,

I am submitting a challenge for the upcoming "Make It & Break It" CTF session. Please find the metadata and required files attached in a zip.  Please mark the files that needs to be uploaded in CTFd with prefix *ctfd_*.

---

## 🧩 Challenge Metadata

**Challenge Title**: Just Cat The Moon
**Category**: Web
**Difficulty**: Medium 
**Author**: theballmarcus & vbjorn
**Flag Format**: `DREAM{tung_tung_tung_sahur_gr1ppy_c4t}`  
**Files Required**: handout.zip
**URL**: http://challenge6.dream.ncr-education.iaas.iik.ntnu.no:42069/

---

## 📝 Description

```
Oh no, meow! I've forgotten my flag on the moon. I'll have to crawl back there to grab it :( 
I don't know if I can hold onto it though, it though. Can yoy help me with my grip strength?
```

---

## 💡 Hints

```
It's important to check the weather so the cat can RACE to the moon!
```
---

## ✅ Solution Write-up

1. We have to notice the `/boost` and `/sboost` - how can we reach `/boost` when only localhost can do it?
2. How can we bypass password in `/sboost`? We don't know it since it is randomly generated. However, it tells you when it goes wrong, and that means that we can bruteforce characters one by one using a custom-made script.
3. In `/boost`, notice this part:
```python
    state = read_state(session.get('username'))

    if state['grip'] >= 1:
        return jsonify({'message': 'Grip already boosted!'}), 403

    username = session.get('username')

    check_weather()

    state = read_state(username)
    print(f"Boosting grip for {username}, current state: {state}")
    state['grip'] += 1
    write_state(username, state)
```
It checks the state, then it checks the weather (which takes a while). Then it reads the state again and overwrites. This means that we have race condition because we have a window where we can send multiple requests to `/boost`. If we send enough, we get the flag.
Solve script is attached - do NOT upload to ctfd.

Thank you for organizing this event. Looking forward to your feedback!

Best regards,  
theballmarcus & vbjorn