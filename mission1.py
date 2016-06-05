list = []
dict = {}
filename = "Conserve_WA.csv"
f = open(filename)
item = f.readline()
while item != "":
    ele_list = item.split("	")
    dict = {}
    dict["id"] = int(ele_list[0])
    dict["create_time"] = ele_list[1]
    dict["content"] = ele_list[2]
    if dict.get("content")[0:2] == "RT":
        dict["rt"] = True
    else:
        dict["rt"] = False
    dict["like"] = int(ele_list[3])
    dict["retweet"] = int(ele_list[4])
    dict["hashtag"] = ele_list[5]
    dict["hashtag_num"] = int(ele_list[6])
    dict["follower"] = int(ele_list[7])
    dict["retweet_user"] = int(ele_list[8])
    list.append(dict)
    item = f.readline()
num = len(list)
num_no_rt = 0
num_rt = 0
for ele in list:
    if ele.get("rt") == False:
        num_no_rt += 1
for ele in list:
    if ele.get("rt") == True:
        num_rt += 1

num_no_rt = float(num_no_rt)
num_rt = float(num_rt)
percent_no_rt = num_no_rt/num
print "precent of no_retweet in file " + filename + " is : " + str(percent_no_rt)