#importar librerías: webdriver(librería principal para controlar el navegador) y by (localización de elementos en la web ID, nombre, clase,..)
from selenium import webdriver
from selenium.webdriver.common.by import By

#crear una nueva instancia del navegador Microsoft Edge
driver = webdriver.Edge() 

#navegar a una web
driver.get("http://www.clouditeducation.com/pruebas")

#busca un elemento en la página, en este caso ID cuyo atributo sea noImportante
elemento = driver.find_element(By.ID, "noImportante")

#verifica si el elemento fue encontrado
if elemento is not None:
    print ("El elemento by ID fue encontrado")

#busca el elemento cuyo atributo NAME sea ultimo 
elemento2 = driver.find_element(By.NAME, "ultimo")

#verifica si el elemento fue encontrado
if elemento2 is not None:
    print ("El elemento by NAME fue encontrado")

#cierra el navegador    
driver.quit()
