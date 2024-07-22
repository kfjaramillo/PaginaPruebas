import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge() 
        self.driver.get("http://www.clouditeducation.com/pruebas")

    def testIdName(self):
        elemento = self.driver.find_element(By.ID, "noImportante")

        if elemento is not None:
            print("El elemento by ID fue encontrado")

        elemento2 = self.driver.find_element(By.NAME, "ultimo")

        if elemento2 is not None:
            print("El elemento by NAME fue encontrado")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

