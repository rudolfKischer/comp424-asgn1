from matplotlib import pyplot as plt
import csv

runtime_csv_file = 'runtimes_table.csv'

def get_runtimes_from_csv():
    runtimes = {}
    file_path = f'{__file__[:__file__.rfind("/") + 1]}{runtime_csv_file}'
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == 'n':
                continue
            runtimes[int(row[0])] = float(row[1])
    return runtimes
    
def plot_runtimes():
    runtimes = get_runtimes_from_csv()
    plt.plot(list(runtimes.keys()), list(runtimes.values()))
    plt.xlabel('N')
    plt.ylabel('Time (s)')
    plt.title('N Queens Runtime')
    plt.show()

def main():
    plot_runtimes()

if __name__ == "__main__":
    main()