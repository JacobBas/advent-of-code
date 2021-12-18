def part1():
    with open("./01-data.txt", "r") as data:
        # read in the data and format by splitting the data
        data = data.read().strip().split("\n")

        # check if the value is increasing or not
        data = [int(data[i-1]) < int(data[i]) for i in range(1, len(data))]

        # return the number of true values
        print(sum(data))


def part2():
    with open("./01-data.txt", "r") as data:
        # read in the data and format by splitting the data
        data = data.read().strip().split("\n")

        # converting the string values to int
        data = [int(num) for num in data]

        # finding the moving sum of the values
        data = [sum(data[i-2:i+1]) for i in range(2, len(data))]

        # check if the value is increasing or not
        data = [data[i-1] < data[i] for i in range(1, len(data))]

        # return the number of true values
        print(sum(data))


if __name__ == "__main__":
    part1()
    part2()
