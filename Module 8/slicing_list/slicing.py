nums = [1,2,3,4,5,6]
print(nums)
print(nums[2:5])

# slice in a for loop
players = ["bob", "steve", "michael", "tom", "eli", "bill"]
print("Here are the first three players on my team")
for player in players[2:5]:
    print(player.title())

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:8:2])