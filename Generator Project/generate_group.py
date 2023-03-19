import random

#Load previous runs by grabbing previous data from the txt doc (with seems to work rather than file = open)
with open("previouss_groups.txt", "r") as f: #read only and f is to ensure it closes jt after
    previous_groups = {} #empty dictionary
    for line in f:
        group = tuple(line.strip().split(",")) #adds data into group ((split)) removess excess characters
        if group in previous_groups:
            previous_groups[group] += 1 # if previous versions are found increment by 1 if not then dont
        else:
            previous_groups[group] = 1

# Get participants as input from user
participants = input("Enter participants, separated by commas: ").strip().split(",")
random.shuffle(participants)

# wHile loop continues until it cant put anymore participants into groups of 2
groups = []
while len(participants) >= 2:
    group = (participants.pop(), participants.pop())
    groups.append(group)

# Divide the participants into pairs and print the pairs
print("Groups:")
for group in groups: #for each previous group its found print that group
    print(group)
    with open("previouss_groups.txt", "a") as f: #checks the premade dictionary
        f.write(",".join(group) + "\n")
        if group in previous_groups: #if a match is found in the disctionary increment it by 1
            previous_groups[group] += 1
        else:
            previous_groups[group] = 1
# Print list of previous groups aka the dictrionary 
print("Previous groups:")
for group, count in sorted(previous_groups.items(), key=lambda x: x[1]): # This code prints a sorted list of groups and their counts.
    print(f"{group}: {count}")

    #sorted function sorts the dictionary into numerical order
    #the lambda is essentially counting how many times it as appeared