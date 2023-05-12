



read = []
out = []
with open("wortH12", 'r') as fp:
    read = fp.readlines()

def run(s, delta, start, exits):
    curr = start
    ans = ""
    for id, ch in enumerate(s): 
        if curr in exits:
            ans=s[:id]
        if ch == "\n":
            break
        curr = delta[curr][ch]

        if curr == "D" :
            break
    return ans 




delta= {
    'A': {'a': 'B', 'b': 'C'},
    'B': {'a': 'D', 'b': 'E'},
    'C': {'a': 'F', 'b': 'D'},
    'D': {'a': 'D', 'b': 'D'},
    'E': {'a': 'B', 'b': 'C'},
    'F': {'a': 'G', 'b': 'C'},
    'G': {'a': 'B', 'b': 'H'},
    'H': {'a': 'I', 'b': 'C'},
    'I': {'a': 'G', 'b': 'H'}
}
start= 'A'
exits= ['A','G']

for s in read:
    ans = run(s, delta, start, exits)
    out.append(ans)


with open("out.txt", 'w') as fp:
    for i in out: 
        fp.write(i)
        fp.write("\n")



