import unittest

import data_examples
from ui import console

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("./tests", pattern="test*.py")
    unittest.TextTestRunner().run(suite)

print("All tests run successfully!")
print()
print("DATA EXAMPLES: ")
data_examples.dataExamples()
console.start()