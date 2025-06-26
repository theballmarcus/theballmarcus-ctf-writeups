# Credential Breakout

## Description
Try to find the credential to unlock the flag. 

Flag format : ICO2025{flag}

## Category
Reverse Engineering

## Points
50

## **Solution**:
This was crazy hard...
```bash
strings CredentialBreakoutChallenge.exe | grep -E '2025\{[^}]*\}'
```
That yeilded the flag: **ICO2025{94vYeC2sQc}**