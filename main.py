import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, help="")
parser.add_argument('--medals', action="store_true", required=False, help="")
parser.add_argument('country', help="")
parser.add_argument('year', help="")
parser.add_argument('--output', required=False, help="")
parser.add_argument('--total', action="store_true", required=False, help="")
parser.add_argument('--overall', nargs='+', required=False, help='')
parser.add_argument('--interactive', required=False, help='')
args = parser.parse_args()
filename = args.filename
medals = args.medals
country = args.country
year = args.year
output = args.output
total = args.total
overall = args.overall
interactive = args.interactive
def task1(filename, medals, country, year, output):
    if medals:
        output_file = None
        coutries = []
        years = []
        idx = 0
        participants = 0
        if output is not None:
            output_file = open(output, 'w')
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split("\t")
                if (data[7] == country or data[6] == country) and data[9] == year:
                    coutries.append(data[6])
                    years.append(data[9])
                    if data[-1] != "NA":
                        idx += 1
                        participants += 1
                        if participants == 11:
                            break
                        if output_file is not None:
                            output_file.write(str(idx) + " " + data[1] + " " + data[12] + " " + data[14] + "\n")
                        else:
                            print(str(idx) + " " + data[1] + " " + data[12] + " " + data[14] + "\n")
            if len(coutries) == 0 or len(years) == 0:
                if output_file is not None:
                    output_file.write("Your country does not exist or there were not olympic games this year" + "\n")
                else:
                    print("Your country does not exist or there were not olympic games this year" + "\n")
        if output_file is not None:
            output_file.close()

def total_medals(medals, output):
    if medals:
        gold = 0
        silver = 0
        bronze = 0
        output_file = None
        if output is not None:
            with open(output, 'r') as file:
                for line in file:
                    data = line.strip().split(" ")
                    if data[-1] == "Gold":
                        gold += 1
                    if data[-1] == "Silver":
                        silver += 1
                    if data[-1] == "Bronze":
                        bronze += 1
            output_file = open(output, 'a')
            if output_file is not None:
                output_file.write(f"""
Gold = {gold}
Silver = {silver}
Bronze = {bronze}""")
            else:
                print(f"""
Gold = {gold}
Silver = {silver}
Bronze = {bronze}""")
        if output_file is not None:
            output_file.close()
def task2(filename, year, total):
    if total:
        first_line = True
        countries = {}
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("\t")
                country_name = data[6]
                if first_line:
                    first_line = False
                    continue
                if year == data[9] and data[14] != "NA" and data[6] != "Unified Team":
                    if str(country_name) not in countries:
                        countries[str(country_name)] = [0, 0, 0]
                    if data[14] == "Gold":
                        countries[str(country_name)][0] += 1
                    elif data[14] == "Silver":
                        countries[str(country_name)][1] += 1
                    elif data[14] == "Bronze":
                        countries[str(country_name)][2] += 1
            sorted_countries = sorted(countries.items(), key=lambda x: sum(x[1]), reverse=True)
            for i in sorted_countries:
                print(i[0], " ", i[1][0], "Gold", i[1][1], "Silver", i[1][2], "Bronze", " ", "Total", sum(i[1]))
def task3(filename,overall):
    if overall:
        first_line = True
        for country in overall:
            results = {}
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split("\t")
                    if first_line:
                        first_line = False
                        continue
                    if country == data[6] and (data[-1] != "NA"):
                        if data[9] not in results:
                            results[data[9]] = 1
                        else:
                            results[data[9]] += 1
            print(country, max(results, key=results.get), max(results.values()))
def task4(filename, interactive):
    if interactive:
        first_line = True
        results = {}
        user_input = input("please enter NOC")
        with open(filename, "r") as file:
            best_year = 0
            olymp = []
            worst_year = 0
            year1 = 2023
            best_result = 0
            worst_result = 100000
            Gold = 0
            Silver = 0
            Bronze = 0
            city1 = ""
            for line in file:
                data = line.strip().split("\t")
                if first_line:
                    first_line = False
                    continue
                if user_input == data[7] or user_input == data[6]:
                    if data[9] not in olymp:
                        olymp.append(data[9])
                    if data[9] not in results:
                        results[data[9]] = 0
                    if year1 > int(data[9]):
                        year1 = int(data[9])
                        city1 = data[11]
                    if data[-1] != "NA":
                        results[data[9]] += 1
                        if data[-1] == "Gold":
                            Gold += 1
                        elif data[-1] == "Silver":
                            Silver += 1
                        elif data[-1] == "Bronze":
                            Bronze += 1
        for i in results:
            if results[i] > best_result:
                best_result = results.get(i)
                best_year = i
            if results[i] < worst_result:
                worst_result = results.get(i)
                worst_year = i
        print(f"Best - {best_year} - {best_result} medals")
        print(f"Worst - {worst_year} - {worst_result} medals")
        print(f"avr gold {Gold//len(olymp)} ")
        print(f"avr silver {Silver//len(olymp)} ")
        print(f"avr bronze {Bronze//len(olymp)} ")
        print(city1)
        print(year1)

task1(filename, medals, country, year, output)
total_medals(medals, output)
task2(filename, year, total)
task3(filename, overall)
task4(filename, interactive)
