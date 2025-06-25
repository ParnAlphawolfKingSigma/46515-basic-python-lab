if celsius <= 0:
   Type = "Freezing"
elif 1 <= celsius <= 15:
    Type = "Cold"
elif 16 <= celsius <= 30:
    Type = "Warm"
else:
    Type = "Hot"