def all_path(pre, numbers, end, max, min):
    if(len(numbers)==1):
        print 'last ', numbers[0]
        n = numbers[0]
        d = abs(n-end)
        if(d<=max and d>=min):
            print 'success'
            return [[n]]
        else:
            print 'fail'
            return None
    r = list()
    for i in numbers:
        d = abs(pre-i)
        if(d<=max and d>=min):
            print 'try ', i
            new_list = list(numbers);
            new_list.remove(i)
            paths = all_path(i, new_list, end, max, min)
            if paths:
                for path in paths:
                    path.insert(0, i)
                r.extend(paths)
                if(len(r)>30):
                    return r
    if len(r)==0:
        return None
    else:
        return r

paths = all_path(1, range(2, 21), 1, 5, 3)
for path in paths:
    print path

def path(pre, numbers, end, max, min):
    if(len(numbers)==1):
        print 'last ', numbers[0]
        n = numbers[0]
        d = abs(n-end)
        if(d<=max and d>=min):
            print 'success'
            return [n]
        else:
            print 'fail'
            return None

    for i in numbers:
        d = abs(pre-i)
        if(d<=max and d>=min):
            print 'try ', i
            new_list = list(numbers);
            new_list.remove(i)
            r = path(i, new_list, end, max, min)
            if r:
                r.insert(0, i)
                return r
    return []

#print path(1, range(2, 21), 1, 5, 3)
#print path(1, [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 1, 5, 3)