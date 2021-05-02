import csv
import os

class CSV(object):
    
    def __init__(self, h, n):
        self.setFile(n)
        self.setHeader(h)
        self.encabezado()
        
    def encabezado(self):
        header = self.getHeader()
        f = open(self.getFile(), 'a')
        writer = csv.writer(f)
        if os.stat(self.getFile()).st_size == 0:
            writer.writerow(header)
        f.close()
        
    def load(self, data):
        f = open(self.getFile(), 'a')
        writer = csv.writer(f)
        writer.writerow(data)
        f.close()
        
    def setFile(self, p):
        self.file = p
    def getFile(self):
        return self.file
    
    def setHeader(self, p):
        self.header = p
    def getHeader(self):
        return self.header
        
# data = CSV(["casa", "perro"], "prueba.csv")
# data.load(("azul", "Pi"))
