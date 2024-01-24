import math
import copy
class Blobservation:
    def __init__(self,room_width,room_height=None):
        self.room_width = room_width
        self.room_height = room_height if room_height is not None else room_width
        self.blobs = []
    def populate(self,blob_info):
        if type(blob_info) == type([]):
            for i in range(len(blob_info)):
                if type(blob_info[i]) != type({}):raise TypeError
                if blob_info[i]['x'] < 0 or blob_info[i]['x'] >= self.room_width:raise ValueError("An x value is incorrect")
                if blob_info[i]['y'] < 0 or blob_info[i]['y'] >= self.room_height:raise ValueError("A y value is incorrect")
                if blob_info[i]['size'] < 1 or blob_info[i]['size'] > 20:raise ValueError("A size value is incorrect")
        else:
            raise TypeError
        for i in range(len(blob_info)):
            self.blobs.append(blob_info[i])
        self.blobs = self.merge()
    def merge(self):
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
    def distance(self,blob1,blob2):
        x = abs(blob2['x'] - blob1['x'])
        y = abs(blob2['y'] - blob1['y'])
        return max(x,y)
    def azimuth(self,origin,destination):
        return (450 - math.degrees(math.atan2(origin['y'] - destination['y'], destination['x'] - origin['x']))) % 360
    def find_nearest_blob(self,original_blob,modified_blob_list_distance):
        for i in range(len(modified_blob_list_distance)):
            modified_blob_list_distance[i]['distance'] = self.distance(original_blob,modified_blob_list_distance[i])
        #determine the closest blob
        smallest_blob_distance = self.room_height * self.room_width
        for i in range(len(modified_blob_list_distance)):
            if smallest_blob_distance > modified_blob_list_distance[i]['distance']:
                smallest_blob_distance = modified_blob_list_distance[i]['distance']
        modified_blob_list_distance = sorted(modified_blob_list_distance, key=lambda x: x['distance'])
        smallest_blob_distance = modified_blob_list_distance[0]['distance']
        result = [i for i in modified_blob_list_distance if i['distance'] == smallest_blob_distance]
        for i in range(len(modified_blob_list_distance)):
            modified_blob_list_distance[i].pop('distance')
        return result
    def find_smaller_blobs(self,blob):
        result = []
        for i in self.blobs:
            if blob['size'] > i['size']:
                result.append(i)
        return result
    def find_biggest_blobs(self,modified_blob_list_size):
        biggest_blob_size = 0
        result = []
        for i in modified_blob_list_size:
            if i['size'] > biggest_blob_size:
                biggest_blob_size = i['size']
        for i in modified_blob_list_size:
            if i['size'] == biggest_blob_size:
                result.append(i)
        return result
    def find_blob_angle(self,blob,modified_blob_list_angle):
        smallest_angle = 359.9
        for i in modified_blob_list_angle:
            if self.azimuth(blob,i) < smallest_angle:
                smallest_angle = self.azimuth(blob,i)
        for i in modified_blob_list_angle:
            if self.azimuth(blob,i) == smallest_angle:
                return i
    def determine_blob(self,blob):
        #smallest distance > largest size > smallest angle
        smaller_blobs = self.find_smaller_blobs(blob)
        if len(smaller_blobs) == 0 : return blob
        nearest_blobs = self.find_nearest_blob(blob,smaller_blobs)
        if len(nearest_blobs) != 1:
            biggest_blobs = smaller_blobs = self.find_biggest_blobs(nearest_blobs)
            if len(biggest_blobs) != 1:
                return self.find_blob_angle(blob,biggest_blobs)
            return biggest_blobs[0]
        return nearest_blobs[0]
    def determine_direction(self,blob):
        result = [0,0]
        blob1 = blob
        blob2 = self.determine_blob(blob)
        if blob1['x'] > blob2['x']:result[0] = -1
        if blob1['x'] < blob2['x']:result[0] = 1
        if blob1['y'] > blob2['y']:result[1] = -1
        if blob1['y'] < blob2['y']:result[1] = 1
        return result
    def move(self,num_of_turns = 1):
        if num_of_turns < 0:raise ValueError
        for turn in range(num_of_turns):
            modified_blob_list = copy.deepcopy(self.blobs)
            for i in range(len(modified_blob_list)):
                modified_blob_list[i]['direction'] = self.determine_direction(modified_blob_list[i])
            for i in range(len(modified_blob_list)):
                self.move_blob(i,modified_blob_list)
            self.merge()
    def find_dictionary_in_list(self,dictionary_list, target_dict):
        #remove 'direction' from the list
        for i in range(len(dictionary_list)):
            dictionary_list[i].pop('direction')
        #find index of target_dict in dictionary_list
        for d in range(len(dictionary_list)):
            if dictionary_list[d] == target_dict:
                return d
        return False
    def move_blob(self,i,modified_blob_list):
        self.blobs[i]['y'] += modified_blob_list[i]['direction'][1]
        self.blobs[i]['x'] += modified_blob_list[i]['direction'][0]
    def print_state(self):
        result = []
        for i in range(len(self.blobs)):
            element = []
            element.append(self.blobs[i]['x'])
            element.append(self.blobs[i]['y'])
            element.append(self.blobs[i]['size'])
            result.append(element)
        return sorted(result, key=lambda x: (x[0], x[1]))