import numpy as np 

######################################################################
"""
sigmoid(z) = 1 / (1+exp(-z))
"""

#######################################################################

# nms
def nms(input, thresh):
    x1 = input[:,0]
    y1 = input[:,1]
    x2 = input[:,2]
    y2 = input[:,3]
    score = input[:,4]

    order = score.argsort()[::-1]
    areas = (x2-x1+1) * (y2-y1+1)

    res = []
    while order.size > 0:
        i = order[0]
        res.append(i)

        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0., xx2-xx1+1)
        h = np.maximum(0., yy2-yy1+1)
        inter = w * h
        overlap = inter / (areas[i] + areas[order[1:]] - inter)

        inds = np.where(overlap <= thresh)[0]
        order = order[inds + 1]

    return res

#######################################################################

#k-means
def kmeans(dataset, k):
    m = np.shape(dataset)[0] # num of data

    cluster = np.mat(np.zeros(m,2))
    unstable = True

    centroid = randcent(dataset, k)
    while unstable:
        unstable = False

        for i in range(m):
            mindist = float("inf")
            minindex = -1
            for j in range(k):
                distance = cal_dist(dataset[i,:], centroid[j,:])
                if distance < mindist:
                    mindist = distance
                    minindex = j
            if cluster[i,0] != minindex:
                unstable = True
                cluster[i,:] = minindex, mindist**2

        for i in range(k):
            points = dataset[np.nonzero(cluster[:,0] == i)[0]]
            centroid[i,:] = np.mean(points, axis=0)
    return centroid, cluster

def cal_dist(x, y):
    return np.sqrt(np.sum((x-y)**2))

def randcent(dataset, k):
    m, n = dataset.shape
    centroid = np.zeros((k,n))
    for i in range(k):
        index = int(np.random.uniform(0,m))
        centroid[i,:] = dataset[index, :]
    return centroid

############################################################################

#knn
def knn(data, labels, test, k):
    square = (data - test)**2
    square_sum = square.sum(axis=1)
    dist = square_sum**0.5

    order = dist.argsort()
    index = order[:k]
    d = {}
    for i in index:
        label = labels[i]
        d[label] = d.get(label, 0) + 1
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

############################################################################

#svm

def svm(X, Y, epochs=1000, lr_rate):
    w = np.zeros(len(X[0]))

    for epoch in range(1, epochs):
        for i, x in enumerate(X):
            if (Y[i] * np.dot(X[i], w)) < 1:
                w = w + learning_rate * ((X[i] * Y[i]) + (-2 * (1/epochs) * w))
            else:
                w = w + learning_rate * (-2 * (1/epochs) * w)

    return w


