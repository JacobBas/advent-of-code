def part1():
    with open("./02-data.txt", "r") as data:
        # reading in an formatting the data
        data = [direct.split(" ")
                for direct in data.read().strip().split("\n")]

        # dictionary of values
        direct = {
            'up': 0,
            'down': 0,
            'forward': 0,
        }

        # adding the directions to the data
        for item in data:
            direct[item[0]] += int(item[1])

        # finding the final distance traveled
        distance = direct["forward"] * (direct["down"] - direct["up"])

        print(distance)


def part2():
    with open("./02-data.txt", "r") as data:
        # reading in an formatting the data
        data = [direct.split(" ")
                for direct in data.read().strip().split("\n")]

        # initializing our values
        horiz = aim = depth = 0

        # adding the directions to the data
        for item in data:
            if item[0] == "forward":
                horiz += int(item[1])
                depth += aim * int(item[1])

            elif item[0] == "down":
                aim += int(item[1])

            elif item[0] == "up":
                aim -= int(item[1])

        # printing the final values
        print(horiz*depth)


if __name__ == "__main__":
    part1()
    part2()
