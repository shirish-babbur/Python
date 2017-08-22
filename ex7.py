# exercise for more printing practices.
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And Everywhere that Mary went.")
#print char '.' 10 times
print("."*10) # What'd that do? Answer - It will print '.' char 10 times.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch that comma at the end. try removing it to see what happens.
# 'end' is simple parameter which decides what has to append after the input passed to print function.It's default value is '\n'.We can put any other char as below. 
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 +end12)
