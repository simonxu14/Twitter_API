list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
list17 = []
list18 = []
list19 = []
list20 = []
list21 = []
list22 = []
list23 = []
list24 = []
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
    date_list = time_list[1].split(":")
    if int(date_list[0]) == 0:
        list1.append(dict)
    elif int(date_list[0]) == 1:
        list2.append(dict)
    elif int(date_list[0]) == 2:
        list3.append(dict)
    elif int(date_list[0]) == 3:
        list4.append(dict)
    elif int(date_list[0]) == 4:
        list5.append(dict)
    elif int(date_list[0]) == 5:
        list6.append(dict)
    elif int(date_list[0]) == 6:
        list7.append(dict)
    elif int(date_list[0]) == 7:
        list8.append(dict)
    elif int(date_list[0]) == 8:
        list9.append(dict)
    elif int(date_list[0]) == 9:
        list10.append(dict)
    elif int(date_list[0]) == 10:
        list11.append(dict)
    elif int(date_list[0]) == 11:
        list12.append(dict)
    elif int(date_list[0]) == 12:
        list13.append(dict)
    elif int(date_list[0]) == 13:
        list14.append(dict)
    elif int(date_list[0]) == 14:
        list15.append(dict)
    elif int(date_list[0]) == 15:
        list16.append(dict)
    elif int(date_list[0]) == 16:
        list17.append(dict)
    elif int(date_list[0]) == 17:
        list18.append(dict)
    elif int(date_list[0]) == 18:
        list19.append(dict)
    elif int(date_list[0]) == 19:
        list20.append(dict)
    elif int(date_list[0]) == 20:
        list21.append(dict)
    elif int(date_list[0]) == 21:
        list22.append(dict)
    elif int(date_list[0]) == 22:
        list23.append(dict)
    elif int(date_list[0]) == 23:
        list24.append(dict)
    item = f.readline()

print "file " + filename + ":"
num_retweet = 0
for ele in list1:
    num_retweet += ele.get("retweet")
print "00:00:00-01:00:00: tweet: " + str(len(list1)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list2:
    num_retweet += ele.get("retweet")
print "01:00:00-02:00:00: tweet: " + str(len(list2)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list3:
    num_retweet += ele.get("retweet")
print "02:00:00-03:00:00: tweet: " + str(len(list3)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list4:
    num_retweet += ele.get("retweet")
print "03:00:00-04:00:00: tweet: " + str(len(list4)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list5:
    num_retweet += ele.get("retweet")
print "04:00:00-05:00:00: tweet: " + str(len(list5)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list6:
    num_retweet += ele.get("retweet")
print "05:00:00-06:00:00: tweet: " + str(len(list6)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list7:
    num_retweet += ele.get("retweet")
print "06:00:00-07:00:00: tweet: " + str(len(list7)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list8:
    num_retweet += ele.get("retweet")
print "07:00:00-08:00:00: tweet: " + str(len(list8)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list9:
    num_retweet += ele.get("retweet")
print "08:00:00-09:00:00: tweet: " + str(len(list9)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list10:
    num_retweet += ele.get("retweet")
print "09:00:00-10:00:00: tweet: " + str(len(list10)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list11:
    num_retweet += ele.get("retweet")
print "10:00:00-11:00:00: tweet: " + str(len(list11)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list12:
    num_retweet += ele.get("retweet")
print "11:00:00-12:00:00: tweet: " + str(len(list12)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list13:
    num_retweet += ele.get("retweet")
print "12:00:00-13:00:00: tweet: " + str(len(list13)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list14:
    num_retweet += ele.get("retweet")
print "13:00:00-14:00:00: tweet: " + str(len(list14)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list15:
    num_retweet += ele.get("retweet")
print "14:00:00-15:00:00: tweet: " + str(len(list15)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list16:
    num_retweet += ele.get("retweet")
print "15:00:00-16:00:00: tweet: " + str(len(list16)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list17:
    num_retweet += ele.get("retweet")
print "16:00:00-17:00:00: tweet: " + str(len(list17)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list18:
    num_retweet += ele.get("retweet")
print "17:00:00-18:00:00: tweet: " + str(len(list18)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list19:
    num_retweet += ele.get("retweet")
print "18:00:00-19:00:00: tweet: " + str(len(list19)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list20:
    num_retweet += ele.get("retweet")
print "19:00:00-20:00:00: tweet: " + str(len(list20)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list21:
    num_retweet += ele.get("retweet")
print "20:00:00-21:00:00: tweet: " + str(len(list21)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list22:
    num_retweet += ele.get("retweet")
print "21:00:00-22:00:00: tweet: " + str(len(list22)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list23:
    num_retweet += ele.get("retweet")
print "22:00:00-23:00:00: tweet: " + str(len(list23)) + " retweet: "+ str(num_retweet)

num_retweet = 0
for ele in list24:
    num_retweet += ele.get("retweet")
print "23:00:00-24:00:00: tweet: " + str(len(list24)) + " retweet: "+ str(num_retweet)