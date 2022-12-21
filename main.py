import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, help="")
parser.add_argument('--medals', action="store_true", required=False, help="")
parser.add_argument('country', help="")
parser.add_argument('year', help="")
parser.add_argument('--output', required=False, help="")

args = parser.parse_args()
filename = args.filename
medals = args.medals
country = args.country
year = args.year
output = args.output

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

task1(filename, medals, country, year, output)
total_medals(medals, output)
