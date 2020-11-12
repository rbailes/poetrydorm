import bds_uidodorm as ud
import numpy as np
import pandas as pd
import sys


text1 = open(r"bd_inputs/tenny.txt", "r")

def poetrycleanup(text, sentences=False):
    if sentences == True:
        poem = text.read()
        poem = poem.strip()
        poem = poem.replace("\n\n", "\n")
        poem = poem.strip("\n")
        poem = poem.split("\n")
        poem = " ".join(poem)
        poem = poem.split(".")
        ii = 0
        while ii < len(poem):
            poem[ii] = poem[ii].strip()
            ii+=1
        if poem[-1] == "":
            poem.pop()
    else:
        poem = text.read()
        poem = poem.strip()
        poem = poem.replace("\n\n", "\n")
        poem = poem.split("\n")
    return poem

mypoem = poetrycleanup(text1)



def multidorm(text, dormuido=False):
    #opens output file for writing to:
    output2 = open(r"bd_outputs/poetrydorms.txt", "w")
    #dictionary for storing data:
    data = {"Line/Sentence":[], "Dorm":[], "Dorm-Uido":[]}
    lst = text
    count = 0
    #line number of text as analysed, either poem line or sentence number:
    line = 1
    #dormuido parameter determines whether dorm-uido is included, default is just dorms:
    if dormuido == True:
        #while loop stops one from the end of list entries:
        while count < len(lst)-1:
            #for each string in the list of strings generated above:
            for i in range(len(lst)-1):
                #gets dorm & rounds to 2d.p., gets uido, finds dorm-uido and round to 2.dp:
                dorm1 = ud.getDORM(lst[i])
                dormf = "{:.2f}".format(dorm1)
                uido1 = ud.dorm(ud.uido((lst[i])))
                du1 = float(dorm1) - float(uido1)
                duf = "{:.2f}".format(du1)
                #appends line number, dorm, & dorm-uido to the data dictionary:
                data["Line/Sentence"].append(line)
                data["Dorm"].append(dorm1)
                data["Dorm-Uido"].append(du1)
                #writes those, along with the string analysed, to output file:
                output2.write(str(line)+" "+lst[i]+" DORM: "+str(dormf)+", DORM-UIDO:"+str(duf)+",\n")
                count += 1
                line += 1
        #final run of the loop ensures output text file is formatted without trailing comma:
        dorm1 = ud.getDORM(lst[len(lst)-1])
        dormf = "{:.2f}".format(dorm1)
        uido1 = ud.dorm(ud.uido((lst[len(lst)-1])))
        du1 = float(dorm1) - float(uido1)
        duf = "{:.2f}".format(du1)
        data["Line/Sentence"].append(line)
        data["Dorm"].append(dorm1)
        data["Dorm-Uido"].append(du1)
        #converts the data dictionary into pandas dataframe to be returned:
        multidormdata = pd.DataFrame.from_dict(data)
        output2.write(str(line)+" "+lst[len(lst)-1]+" DORM: "+str(dormf)+", DORM-UIDO: "+str(duf))
        #closes output file when all is done:
        output2.close()
        return multidormdata
    else:
        data = {"Line/Sentence":[], "Dorm":[]}
        while count < len(lst)-1:
            for i in range(len(lst)-1):
                dorm1 = ud.getDORM(lst[i])
                dormf = "{:.2f}".format(dorm1)
                data["Line/Sentence"].append(line)
                data["Dorm"].append(dorm1)
                output2.write(str(line)+" "+lst[i]+" SENTENCE DORM:"+str(dormf)+",\n")
                count += 1
                line += 1
        dorm1 = ud.getDORM(lst[len(lst)-1])
        dormf = "{:.2f}".format(dorm1)
        data["Line/Sentence"].append(line)
        data["Dorm"].append(dorm1)
        multidormdata = pd.DataFrame.from_dict(data)
        output2.write(str(line)+" "+lst[len(lst)-1]+" SENTENCE DORM:"+str(dormf))
        output2.close()
        return multidormdata

        
        
dormy = multidorm(mypoem, dormuido=True)
print(dormy)
