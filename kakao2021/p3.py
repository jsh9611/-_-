def solution(fees, records):
    base_time = fees[0]
    base_rate = fees[1]
    unit_time = fees[2]
    unit_rate = fees[3]
    t = []
    cn = []
    s = []
    count = 0
    for item in records:
        count += 1
        time,car_num,state = item.split(' ')
        h,m = map(int,time.split(':'))
        if car_num in cn:
            temp = cn.index(car_num)
            if s[temp] == 0:
                t[temp] -= (h*60+m)
                s[temp] = 1
            elif s[temp] == 1:
                t[temp] += (h*60+m)
                s[temp] = 0
        else:
            t.append(-h*60-m)
            cn.append(car_num)
            s.append(1)
    for i in range(len(cn)):
        if s[i] == 1:
            s[i] = 0
            t[i] += 1439

    dic = {}
    for i in range(len(t)):
        # if t[i]%unit_time != 0:
        #     t[i] = t[i] - t[i]%unit_time + unit_time
        dic[cn[i]] = t[i]
    sort_dic = sorted(dic.items(), key=lambda x: x[0])
    # print(sort_dic)
    answer = []
    for item in sort_dic:
        if item[1] <= base_time:
            answer.append(base_rate)
        else:
            base_rate+(((item[1]-base_time)/unit_time)*unit_rate)

            ans = item[1] - base_time
            if ans%unit_time > 0:
                ans = ans - ans%unit_time + unit_time
            ans = base_rate + ans/unit_time*unit_rate
            answer.append(int(ans))
            # print('b',ans)
            # answer.append(int(base_rate+(((item[1]-base_time)/unit_time)*unit_rate)))

    return answer

# fees = [180, 5000, 10, 600]
# records =["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

fees = [120, 0, 60, 591]	
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

# fees = [10, 100, 10, 100]
# records = ["00:00 1234 IN", "01:10 1234 OUT"]

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees,records))