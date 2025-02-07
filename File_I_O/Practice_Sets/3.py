# write a multiplication table 2 to 20 for a 13 year old Child and make every table in different file 
for num in range(2,21):
    with open("table_"+str(num)+".txt","w") as f:
        for i in range(1,11):
            f.write(str(num)+"*"+ str(i)+"="+str(i*num)+"\n"+"---------------------------\n")

print("Done")
