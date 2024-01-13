import math
class Blobservation:
    def __init__(self,room_height,*args):#completed
        if len(args) == 1:
            self.room_height = room_height
            self.room_width = args[0]
        elif len(args) == 0:
            self.room_height = room_height
            self.room_width = self.room_height
        else:
            raise TypeError("__init__() takes 2 positional arguments but " + str(len(args)+1) + " were given")
        self.blobs = []
    def populate(self,blob_info):#completed
        if type(blob_info) == type([]):
            for i in range(len(blob_info)):
                if type(blob_info[i]) != type({}):
                    raise TypeError
                if blob_info[i]['x'] < 0 or blob_info[i]['x'] > self.room_width:
                    raise ValueError("An x value is incorrect")
                if blob_info[i]['y'] < 0 or blob_info[i]['y'] > self.room_height:
                    raise ValueError("A y value is incorrect")
                if blob_info[i]['size'] < 1 or blob_info[i]['size'] > 20:
                    raise ValueError("A size value is incorrect")
        else:
            raise TypeError
        for i in range(len(blob_info)):
            self.blobs.append(blob_info[i])
        self.blobs = self.merge()
    def merge(self):#completed
        i = 0
        while i < len(self.blobs):
            b = i+1
            while b < len(self.blobs):
                if self.blobs[i]['x'] == self.blobs[b]['x'] and self.blobs[i]['y'] == self.blobs[b]['y']:
                    self.blobs[i]['size'] += self.blobs[b]['size']
                    self.blobs.remove(self.blobs[b])
                else:
                    b += 1
            i += 1
        return self.blobs
    def distance(self,blob1,blob2):#completed
        a = blob2['x'] - blob1['x']
        b = blob2['y'] - blob1['y']
        c = (a*a)+(b*b)
        c = math.sqrt(c)
        return c
    def azimuth(self,blob1,blob2):#completed
        x1 = 0
        y1 = 1
        x2 = blob2['x'] - blob1['x']
        y2 = blob2['y'] - blob1['y']
        v1_theta = math.atan2(y1, x1)
        v2_theta = math.atan2(y2, x2)
        r = (v1_theta - v2_theta) * (180.0 / math.pi)
        if r < 0:
            r += 360
        return r
    def find_nearest_blob(self,original_blob):#completed
        #make a copy of self.blobs , and add distance to it
        modified_blob_list = self.blobs
        for i in range(len(modified_blob_list)):
            modified_blob_list[i]['distance'] = self.distance(original_blob,i)
        #determine the closest blob
        smallest_blob_distance = self.room_height * self.room_width
        for i in range(len(modified_blob_list)):
            if modified_blob_list[i]['distance'] != 0:
                if smallest_blob_distance > modified_blob_list[i]['distance']:
                    smallest_blob_distance = modified_blob_list[i]['distance']
        modified_blob_list = sorted(modified_blob_list, key=lambda x: x['distance'])
        return modified_blob_list[0]
    def find_smallest_blob(self):
        pass
    def move(self,*args):#completed
        test = 1
        if len(args) == 1:
            turns = args[0]
        elif len(args) == 0:
            turns = 1
        else:
            raise TypeError("move() takes 1 positional argument but " + str(len(args)) + " were given")
        if type(turns) != type(test):
            raise TypeError
        elif turns < test:
            raise ValueError
        biggest_blob_size = 0
        for i in self.blobs:
            if i['size'] > biggest_blob_size:
                biggest_blob_size = i['size']
                biggest_blob = i
        smallest_blob_size = biggest_blob_size
        for i in self.blobs:
            if i['size'] < smallest_blob_size:
                smallest_blob_size = i['size']
                smallest_blob = i
    def print_state(self):#completed
        result = []
        for i in range(len(self.blobs)):
            element = []
            element.append(self.blobs[i]['x'])
            element.append(self.blobs[i]['y'])
            element.append(self.blobs[i]['size'])
            result.append(element)
        result.sort()
        return result