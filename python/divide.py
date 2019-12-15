import time
import sys
results = dict()
def get_div(n, k):
    key = (n, k);
    if results.has_key(key):
        return results[key]
    if k==1 or n==k :
        #print n, k, 1
        results[key]=1
        return 1
    r = 0
    for i in range(1, n/k+1):
        #print 'k:', n, ' i:', i
        r = r+get_div(n-i-(k-1)*(i-1), k-1)
    #print n, k, r
    results[key]=r
    return r
if __name__=="__main__":
    if len(sys.argv)<3:
        print 'usage: '+sys.argv[0]+' n k'
        sys.exit(0)
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    t1 = time.time()
    print 'div(%d,%d)=%d'%(n, k, get_div(n, k))
    t2 = time.time()
    print 'time:',t2-t1