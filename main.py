# Write a function called is_old_enough_to_drink_and_drive. Given a number, in this case an age, is_old_enough_to_drink_and_drive returns whether a person of this given age is old enough to legally drink and drive in the United States.

# Notes:

#     The legal drinking age in the United States is 21
#     It is always illegal to drink and drive in the United States

# output = is_old_enough_to_drink_and_drive(22)
# print(output) # --> False

def is_old_enough_to_drink_and_drive(age):
  if age>=21:
    return False
  else:
    return False

print(is_old_enough_to_drink_and_drive(21))
