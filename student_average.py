scores =[ 10, 12, 56, 70, 70]
total = 0
for score in scores:
    total += score
average = total / len(scores)
print("Average:", average)
if average >= 70:
    print("Congratulations!Average is above 70")
elif average <= 70:\
    print("Sorry! Average is below 70")
else: print("The average is exactly 70")