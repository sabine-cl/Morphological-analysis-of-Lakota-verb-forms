import subprocess
import difflib

directory = "/your/path/lakota/"
filename = "verb.xfst"
application = "xfst"

commands = [f"source < {directory}/{filename};"]
commands.append(f"apply down < {directory}/upper_from_publications.txt > output.txt;")

result = subprocess.run([f"{directory}/{application}"],
                    input="\n".join(commands),
                    text = True,
                    capture_output=True)

print(result.stdout)
print(result.stderr)

with open(f"{directory}/python_scripts/output.txt", "r") as f:
    output = f.readlines()

with open(f"{directory}/goal_from_publications.txt") as f:
    goal = f.readlines()    

delta2 = []
if "ERROR" in result.stderr:
    print("xfst reported an error")
else:
    diff = list(difflib.ndiff(output, goal))
    for idx in range(len(diff)):
        if diff[idx].startswith("-"):
            delta2.append(diff[idx-1])
            delta2.append(diff[idx])
        if diff[idx].startswith("+"):
            delta2.append(diff[idx])

    delta = ''.join(x[2:] for x in diff if x.startswith('- '))
    if delta == "":    
        print("Everything right!")
    else:
        print("Everything right except:")
        for line in delta2:
            print(line.strip())
            if line.startswith("+"):
                print()
        