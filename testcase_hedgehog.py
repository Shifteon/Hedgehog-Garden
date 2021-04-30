import unittest
from hedgehog import Hedgehog
from food import Orange, Cake, Kibble

class testHedgehog(unittest.TestCase):
    def testFeedOrange(self):
        # Setup
        hedgehog = Hedgehog()
        orange = Orange()
        # Exercise
        hedgehog.feed(orange)
        # Verify
        assert(hedgehog.hunger == 400 and hedgehog.health == 120)
    # Teardown
    
    def testFeedCake(self):
        # Setup
        hedgehog = Hedgehog()
        cake = Cake()
        # Exercise
        hedgehog.feed(cake)
        # Verify
        assert(hedgehog.hunger == 300 and hedgehog.health == 90)
    # Teardown

    def testFeedFull(self):
        # Setup
        hedgehog = Hedgehog()
        kibble = Kibble()
        hedgehog.hunger = 0
        # Exercise
        hedgehog.feed(kibble)
        # Verify
        assert(hedgehog.hunger == 0)
    # Teardown

    def testWash(self):
        # Setup
        hedgehog = Hedgehog()
        # Exercise
        hedgehog.wash()
        # Verify
        assert(hedgehog.hygeine == 120)
    # Teardown

    def testWashFull(self):
        # Setup
        hedgehog = Hedgehog()
        hedgehog.hygeine = 500
        # Exercise
        hedgehog.wash()
        # Verify
        assert(hedgehog.hygeine == 500)
    # Teardown

    def testExercise(self):
        # Setup
        hedgehog = Hedgehog()
        # Exercise
        hedgehog.exercise()
        # Verify
        assert(hedgehog.health == 120)
    # Teardown

    def testExerciseFull(self):
        # Setup
        hedgehog = Hedgehog()
        hedgehog.health = 500
        # Exercise
        hedgehog.exercise()
        # Verify
        assert(hedgehog.health == 500)
    # Teardown

    def testIsMaxStatus(self):
        # Setup
        hedgehog = Hedgehog()
        hedgehog.hunger = hedgehog.maxStats[0]
        hedgehog.health = hedgehog.maxStats[1]
        hedgehog.hygeine = hedgehog.maxStats[2]
        # Exercise / Verify
        assert(hedgehog.isMaxStatus() == True)
    # Teardown

    def testIsMaxStatusFalse(self):
        # Setup
        hedgehog = Hedgehog()
        # Exercise / Verify
        assert(hedgehog.isMaxStatus() == False)
    # Teardown

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(testHedgehog)
    return suite