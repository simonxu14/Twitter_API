list = []
dict = {}
filename = "ConservationNW.csv"
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
    time_list = dict.get("create_time").split(" ")
    date_list = time_list[0].split("-")
    if int(date_list[0]) > 2016:
        list.append(dict)
    elif int(date_list[0]) == 2016 and int(date_list[1]) > 5:
        list.append(dict)
    elif int(date_list[0]) == 2016 and int(date_list[1]) == 5 and int(date_list[2]) >=2:
        list.append(dict)
    item = f.readline()
num_follower = 0
for ele in list:
    num_follower += ele.get("follower")
print "num_follower of file " + filename + "is : " + str(num_follower)