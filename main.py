import getopt
import sys

config_file = None
text_file = None
output_file = None
original_symbols = []
replace_symbols = []
text_symbols = []
count = 0
order_dict = {}

argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "c:t:")

except:
    print("Error")

for opt, arg in opts:
        if opt in ['-c']:
            config_file = arg
        elif opt in ['-t']:
            text_file = arg

config_rule = open(config_file,'r').read().split('\n')

for i in range(len(config_rule)):
    original, replace = config_rule[i].split("=")
    original_symbols.append(original)
    replace_symbols.append(replace)

text = open(text_file,'r').read().split('\n')
result = open("text.txt",'w')

for i in range(len(text)):
    text_symbols.append(text[i])

for i in range(len(text_symbols)):
    for j in range(len(original_symbols)):
        while text_symbols[i].find(original_symbols[j]) != -1:
            text_symbols[i] = text_symbols[i].replace(original_symbols[j], replace_symbols[j], 1)
            text_for_dict = text_symbols[i]
            count+=1
    order_dict[text_for_dict] = count
    count = 0

order_dict = dict(sorted(order_dict.items(), key=lambda item: item[1], reverse=True))
for key in order_dict:
    result.write(key + '\n')
    print(key + " Amount of changes: " + str(order_dict[key]))
