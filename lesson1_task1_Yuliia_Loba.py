duration  = int(input("Write the time in seconds:" ))

#if duration // 86400:ATOPE

day = duration // 86400

#if duration % 86400 > 3600:

hours = duration // 3600
min = duration  // 60
sec = duration % 86400 % 3600 % 60
print(day , hours, min, sec)