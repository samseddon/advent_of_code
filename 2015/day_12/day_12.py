import re
import json

f = open("input.txt")
line = f.readline()
#line = '{"a":{"b":4},"c":-1}'
#line = '[1,{"c":"red","b":2},3]'

def hook(obj):
    if "red" in obj.values():
        return {}
    else:
        return obj

output1 = sum(int(x) for x in re.findall(r'-?\d+', line))
output = re.findall("\{(.*?)\}", line)
ignored = []
for thing in output:
    if "red" in thing:
        ignored.append(sum(int(x) for x in re.findall(r'-?\d+', thing)))

output_no_red = str(json.loads(line, object_hook = hook))
print(output_no_red)

output2 = sum(int(x) for x in re.findall(r'-?\d+', output_no_red))

print(output2)

