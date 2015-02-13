f = open("C:\Users\G Torres\Documents\UP Diliman Stuff\GmE 205\MachineExercises\LE71060652004237ASA00_MTL.txt", "r")
counter = 0
for i in f:
    d = i.strip()
    c = d.split('=')
    counter += 1
    c.insert(0, counter)
    if c[0] == counter+61:
        d = {counter:c[2]}
    print c
print d
    

        
