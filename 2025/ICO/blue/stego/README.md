# Mona's Secret

## Description
Mona Lisa’s smile is said to hold secrets. But in this case, her image literally does.

📁 Provided File: Mona_Lisa_final.jpg  
🎯 Objective: Extract the hidden flag.

Flag format : ICO2025{xxxx}

## Category
Steganography

## Points
45

## **Solution**:
This one actually took me a LONG time... I started by spinning up a docker container with preinstalled stego tools. That took A WHILE on the ICO2025 university wifi. 
```bash
docker pull dominicbreuker/stego-toolkit
docker run -it --rm -v ~/stegodata:/data dominicbreuker/stego-toolkit /bin/bash
```
Then I tried these tools that didn't find anything.
```bash
exiftool, binwalk, check_jpg.sh, zsteg, stegdetect, stegoveritas, foremost, strings, outguess, jsteg, opensteg, hstego, f5
```
While I was trying this, I had started the brute force script:
```bash
brute_jpg.sh
```
It took an hour but finally revealed the code as DaVinci. So I extracted it:
```bash
steghide extract -sf Mona_Lisa_final.jpg -p "DaVinci"
cat flag.txt
```
The flag was *flag{happy_SG60}*