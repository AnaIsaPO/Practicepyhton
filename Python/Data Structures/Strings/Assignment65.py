text = "X-DSPAM-Confidence:    0.8475"
xtra = text.find(' ')
fxtra = text[xtra:]
print(float(fxtra))