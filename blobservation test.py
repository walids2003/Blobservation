from blobservation import Blobservation
import codewars_test as test
test.describe('Example Tests')
pf = lambda x,r: test.assert_equals(x.print_state(),r)

'''generation0 = [
	{'x':0,'y':4,'size':3},
	{'x':0,'y':7,'size':5},
	{'x':2,'y':0,'size':2},
	{'x':3,'y':7,'size':2},
	{'x':4,'y':3,'size':4},
	{'x':5,'y':6,'size':2},
	{'x':6,'y':7,'size':1},
	{'x':7,'y':0,'size':3},
	{'x':7,'y':2,'size':1}]'''
#blobs = Blobservation(8)
#blobs.populate(generation0)
#blobs.move()
#pf(blobs,[[0,6,5],[1,5,3],[3,1,2],[4,7,2],[5,2,4],[6,7,3],[7,1,3],[7,2,1]])
#blobs.move()
#pf(blobs,[[1,5,5],[2,6,3],[4,2,2],[5,6,2],[5,7,3],[6,1,4],[7,2,4]])
#blobs.move(1000)
#pf(blobs,[[4,3,23]])

generation1 = [
	{'x':3,'y':6,'size':3},
	{'x':8,'y':0,'size':2},
	{'x':5,'y':3,'size':6},
	{'x':1,'y':1,'size':1},
	{'x':2,'y':6,'size':2},
	{'x':1,'y':5,'size':4},
	{'x':7,'y':7,'size':1},
	{'x':9,'y':6,'size':3},
	{'x':8,'y':3,'size':4},
	{'x':5,'y':6,'size':3},
	{'x':0,'y':6,'size':1},
	{'x':3,'y':2,'size':5}]
generation2 = [
	{'x':5,'y':4,'size':3},
	{'x':8,'y':6,'size':15},
	{'x':1,'y':4,'size':4},
	{'x':2,'y':7,'size':9},
	{'x':9,'y':0,'size':10},
	{'x':3,'y':5,'size':4},
	{'x':7,'y':2,'size':6},
	{'x':3,'y':3,'size':2}]
blobs = Blobservation(10,8)
                    #(x ,y)
blobs.populate(generation1)
blobs.move()
pf(blobs,[[0,6,1],[1,1,1],[1,6,2],[2,1,5],[2,6,7],[4,2,6],[6,7,3],[7,1,2],[7,4,4],[7,7,1],[8,7,3]])
blobs.move(2)
pf(blobs,[[0,6,7],[1,5,3],[2,2,6],[4,1,6],[6,1,2],[6,4,4],[6,6,7]])
blobs.move(2)
pf(blobs,[[2,4,13],[3,3,3],[6,1,8],[6,2,4],[6,4,7]])
blobs.populate(generation2)
pf(blobs,[[1,4,4],[2,4,13],[2,7,9],[3,3,5],[3,5,4],[5,4,3],[6,1,8],[6,2,4],[6,4,7],[7,2,6],[8,6,15],[9,0,10]])
blobs.move()
pf(blobs,[[2,4,9],[3,3,13],[3,6,9],[4,4,4],[5,3,4],[5,4,10],[6,2,6],[7,2,8],[7,5,15],[8,1,10]])
blobs.move(3)
pf(blobs,[[4,3,22],[5,3,28],[5,4,9],[6,2,29]])
test.expect_error('Invalid input for the move method should trigger an error',lambda: blobs.move(-3))
blobs.move(30)
pf(blobs,[[5,3,88]])
test.expect_error('Invalid elements should trigger an error',lambda: blobs.populate([{'x':4,'y':6,'size':3},{'x':'3','y':2,'size':True}]))
print('<COMPLETEDIN::>')