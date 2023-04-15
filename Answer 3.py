String_1='The quick Brow Fox'
lower_Case=0
upper_Case=0
for i in String_1:
      if(i.islower()):
            lower_Case+=1
      else:
            upper_Case+=1
print("The number of lowercase characters is:",lower_Case)
print("The number of uppercase characters is:",upper_Case)
