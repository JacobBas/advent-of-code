def main():
    with open("./day1.txt", "r") as data:
        # read in the data and format by splitting the data
        data = data.read().strip().split("\n")
        
        # check if the value is increasing or not
        data = [int(data[i-1]) < int(data[i]) for i in range(1, len(data))]
        
        # return the number of true values
        print(sum(data))

if __name__ == "__main__":
    main()

