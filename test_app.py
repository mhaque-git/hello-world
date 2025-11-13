# test 
import unitest
from app import hello_world

class TestApp(unitest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

if __name__ == "__main__":
    unitest.main()
    
