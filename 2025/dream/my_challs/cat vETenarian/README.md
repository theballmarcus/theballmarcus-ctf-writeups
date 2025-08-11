# cat vETenarian

Category: pwn

## Mail

Subject: [DREAM Challenge Submission] cat vETenarian by vvbjorn & theballmarcus

To: **developers+dream@ncr.ntnu.no**

Dear CTF Development Team,

I am submitting a challenge for the upcoming "Make It & Break It" CTF session. Please find the metadata and required files attached in a zip.  Please mark the files that needs to be uploaded in CTFd with prefix *ctfd_*.

---

## 🧩 Challenge Metadata

**Challenge Title**: cat vETenarian
**Category**: Pwn
**Difficulty**: Medium
**Author**: vvbjorn & theballmarcus  
**Flag Format**: `DREAM{th4nks_f0r_t4k1ng_my_c4t_t0_th3_vETenarian<3}`  
**Files Required**: cat_vETenarian_handout.7z
**Handout password**: `mreoww_lol!!`
**URL**: [text](http://challenge6.dream.ncr-education.iaas.iik.ntnu.no:1337/uploads/cat_vETenarian_handout.7z)

---

## 📝 Description

meow meow

---

## 💡 Hints

i cant take it anymore

---

## ✅ Solution Write-up

- The program wraps cat to print a single file, filtering input to allow only alphanumeric, ., /, space, and _ characters.

- The input buffer filename is 100 bytes, but it copies up to 256 bytes without bounds checking, causing a buffer overflow that can overwrite the adjacent cat_flags buffer (4 bytes).

- By overflowing filename, you control cat_flags, which are command-line flags passed to cat. This bypasses input restrictions and lets you run cat with custom flags and arguments.

- The Python script crafts a payload that overflows filename, overwrites cat_flags to add flags and file name (like flag.txt), then runs the vulnerable binary to get the encoded flag.

- The flag is encoded in a custom binary format using tabs and null bytes. You reverse engineer the enc.py script to create your own dec.py script to decode the flag.

---

## 🧪 Testing Notes

<Mention any testing done and expected behavior.>

---

Thank you for organizing this event. Looking forward to your feedback!

Best regards,  
vvbjorn & theballmarcus 
Team 6
