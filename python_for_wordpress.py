import csv

list_members=[]

with open('member_list_2019.csv','r') as csv_file:
    list_member = csv_file.readlines()

html_head = "<table>"
html_body = ""
html_end="</table>"

count=1
count_lines=0
for line in list_member:
    html_line="<tr>"
    val=line.split(",")
    for i in range(len(val)):
        if(i==1 or i==2 or i==6):
            continue
        val[i]=val[i].replace("\"","")
        html_line=html_line+"<td>"+val[i]+"</td>"
    html_line=html_line+"</tr>"
    html_body=html_body+html_line
    count_lines+=1
    if(count_lines%50==0 or count_lines>=len(list_member)-1):
        newFile= open("html_file"+str(count)+".html","w")
        html_final=html_head+html_body+html_end
        html_body=""
        newFile.write(html_final)
        count+=1
        newFile.close()

#newFileName=open("htmlfile.html"+count,"w")
    
