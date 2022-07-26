import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from k_means import *
from PyQt5.QtWidgets import QApplication,QWidget,QInputDialog,QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title='K-mean clustering'
        self.left=10
        self.top=10
        self.width=300
        self.height=250
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.getText()
        self.show()
    def getText(self):
        end = False
        list_col = []
        d1,okPressed1=QInputDialog.getText(self, "Arquivo", "Caminho")
        d2,okPressed2=QInputDialog.getInt(self, "Centroides", "Qtde:")
        
        while(not end):
            d4,okPressed4=QInputDialog.getText(self, "Nova Coluna", "Nome")

            if d4 == "" and okPressed4:
                end = True
            else:
                list_col.append(d4)

        if okPressed1 and okPressed2:
            df = pd.read_csv(d1, delimiter="," )

            data = df[list_col].to_numpy()

            result = k_means(d2, data)
            
            plotar(data, result, list_col)


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()