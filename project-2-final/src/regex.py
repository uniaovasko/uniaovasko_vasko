import csv
import re

def test_strings(strings):
    # recebe array de strings de qtd de ingredientes, retorna uma lista com a quantidade em float e a unidade de medida, se houver
    regex = re.compile(r'((\d+/\d+)|(\d)+(\s\d+/\d+)?) (teaspoons?|tablespoons?|pounds?|cups?|\((\d+(\.\d+)?) (ounces?)\))?')
    matched_groups = []

    for string in strings:
        match = regex.match(string)
        if match:
            matched_groups.append(match.groups())
        else:
            matched_groups.append(None)

    filtered_groups = []
    for group in matched_groups:
        if group is None:
            filtered_groups.append([1.])
            continue
        new_group = []
        for item in group:
            if item:
                new_group.append(item)
        
        new_group.pop(0)
        try:
            new_group[0] = float(new_group[0])
        except:
            frac = new_group[0].split('/')
            frac = float(frac[0]) / float(frac[1])
            new_group[0] = frac
        if new_group[-1] == "ounce":
            if len(new_group) == 5:
                if new_group[1][0] == ' ':
                    frac = new_group[1].split('/')
                    frac = float(frac[0]) / float(frac[1])
                    new_group[1] = frac
                    new_group[0] = new_group[0] + float(new_group[1])
                    new_group.pop(1); new_group.pop(1)
                else:
                    new_group.pop(-2); new_group.pop(-3)
            elif len(new_group) == 4:
                new_group.pop(1)
            try:
                new_group[0] = new_group[0] * float(new_group[1])
                new_group.pop(1)
            except:
                pass
        if len(new_group) == 3:
            frac = new_group[1].split('/')
            frac = float(frac[0]) / float(frac[1])
            new_group[0] = new_group[0] + frac
            new_group.pop(1)
            
            
        filtered_groups.append(new_group)
    
    return filtered_groups

# Example usage:
def test1():
    input_strings = ["1 1/2 (10 ounce)","1 (14 ounce)","1 tablespoon", "1 1/2 teaspoon", "2 (2.30 ounce)", "8 slices white bread, with crusts trimmed", "xablau"]

    result = test_strings(input_strings)

    for i, groups in enumerate(result):
        print(f"String {i + 1}: {input_strings[i]}")
        if groups:
            print(f"Matched Groups: {groups}")
        else:
            print("No match found")
        print("-" * 20)

def test2():
    with open('data/external/04_Recipe-Ingredients_Aliases.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        array = []
        for row in csv_reader:
            array.append(row[1])

    input_strings = array[1:]
    result = test_strings(input_strings)
    with open('data/interim/qtds_ingredientes.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i, groups in enumerate(result):
            csv_writer.writerow([f"String {i + 1}: {input_strings[i]}"])
            if groups:
                csv_writer.writerow([f"Matched Groups: {groups}"])
            else:
                csv_writer.writerow(["No match found"])
            csv_writer.writerow("-" * 20)
                
test2()