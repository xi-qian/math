#directed_edges = ['ae', 'ec', 'ad', 'ef', 'cb', 'df', 'fb', 'af', 'de', 'eb', 'fc']
directed_edges = ['ae', 'ad', 'ap', 'dp', 'df', 'ep', 'ef', 'pf', 'ec', 'eq', 'fq', 'fb', 'cq', 'cb', 'qb']

def create_set(data):
    s = set()
    for p in data:
        s.add(p)
    return s

#nodes = create_set('abcdef')
nodes = create_set('abcdefpq')

def init_edges():
    edges = set()
    for edge in directed_edges:
        edges.add(edge)
        edges.add(edge[::-1])
    return edges

edges = init_edges()

def find_succeeds(preds):
    pred_set = create_set(preds)
    succeeds = set()
    for node in nodes:
        if (preds[-1]+node) in edges and not node in pred_set:
            succeeds.add(node)
    return succeeds

start = 'a'
end = 'b'

paths = [start]

for i in range(len(nodes)):
    new_paths = []
    for path in paths:
        if path[-1]==end:
            new_paths.append(path)
            continue
        ss = find_succeeds(path)
        #print i, path
        #print ss
        for node in ss:
            new_paths.append(path+node)
        #print new_paths
    paths = new_paths

print len(new_paths)
for path in new_paths:
    print path