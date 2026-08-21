import subprocess
import difflib

directory = "/your/path/lakota/"
filename = "verb.xfst"
application = "xfst"

commands = [f"source < {directory}/{filename};"]
commands.append(f"apply up < {directory}/lower-false.txt > output.txt;")


result = subprocess.run([f"{directory}/{application}"],
                    input="\n".join(commands),
                    text = True,
                    capture_output=True)

#print(result.stdout)
#print(result.stderr)

with open(f"{directory}/python_scripts/output.txt", "r") as f:
    output = f.readlines()

with open(f"{directory}/lower-false-goal.txt") as f:
    goal = f.readlines()  

if "ERROR" in result.stderr:
    print("xfst reported an error")
else:
    diff = difflib.ndiff(output, goal)
    delta = ''.join(x[2:] for x in diff if x.startswith('- '))
    if delta == "":    
        print("Everything right!")
    else:
        print(len(delta.split("\n"))-1, "/", int(len(output)/3), "test cases wrong")
        print(delta)