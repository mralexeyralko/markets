from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
import sys

from functions import printCityFunc
from functions import addCitiesToComboBoxFunc
from functions import aboutMarketFunc
from functions import radioActionFunc

app = QApplication(sys.argv)

def uiFunc():
    ##############################################################
    #                           WINDOW                           #
    ##############################################################  
     
    window = QWidget()
    window.setWindowTitle('How about buying some fresh farm goods not far from your location?')
    window.setFixedWidth(900)
    window.setStyleSheet('background: steelblue;')
    grid = QGridLayout()

    ##############################################################
    #                      TEXT BLOCK                            #
    ##############################################################

    textBlock = QTextEdit()
    textBlock.setStyleSheet('background: white;'
                            'border-radius: 10px;'
                            'border: 1px solid slategrey;'
                            'margin: 0px;'
                            'padding: 10px;'
                            'min-height: 100%;'
                            'max-width: 400px;'
                            'text-align: center;')
                            
    textBlock.setAlignment(QtCore.Qt.AlignLeft)
    grid.addWidget(textBlock, 0, 4)

    def sendSLTextFunc():

        if (marketBox.currentText()) == '':
            print('кажись выловил')
        else:
            try:
                textBlock.setText(aboutMarketFunc(marketBox.currentText()))

                def setRadioButtons():
                    marketName = str(marketBox.currentText())
                    marketName = marketName[0:-7]
                    
                    if marketName[-1] == ' ':
                        marketName = marketName[0:-1]

                    
                    # def radioActionFunc(someValue):
                    #         str(someValue)
                    #         print('Кнопа кричит' + str(someValue))
                    
                    radioButton = QRadioButton("*")
                    radioButton.setChecked(False)
                    radioButton.value = 1.0
                    radioButton.pressed.connect(lambda: radioActionFunc(radioButton.value, marketName))
                    grid.addWidget(radioButton, 2, 4)

                    radioButton2 = QRadioButton("**")
                    radioButton2.setChecked(False)
                    radioButton2.value = 2.0
                    radioButton2.pressed.connect(lambda: radioActionFunc(radioButton2.value, marketName))
                    grid.addWidget(radioButton2, 3, 4)

                    radioButton3 = QRadioButton("***")
                    radioButton3.setChecked(False)
                    radioButton3.value = 3.0
                    radioButton3.pressed.connect(lambda: radioActionFunc(radioButton3.value, marketName))
                    grid.addWidget(radioButton3, 4, 4)

                    radioButton4 = QRadioButton("****")
                    radioButton4.setChecked(False)
                    radioButton4.value = 4.0
                    radioButton4.pressed.connect(lambda: radioActionFunc(radioButton4.value, marketName))
                    grid.addWidget(radioButton4, 5, 4)

                    radioButton5 = QRadioButton("*****")
                    radioButton5.setChecked(True)
                    radioButton5.value = 5.0
                    radioButton5.pressed.connect(lambda: radioActionFunc(radioButton5.value, marketName))
                    grid.addWidget(radioButton5, 6, 4)
                setRadioButtons()






            except TypeError:
                textBlock.setText('Not all the parameters were chosen')
               

    def uiPrintFunc():

        try:
            marketBox.clear()
            marketBox.addItems(printCityFunc(comboBox.currentText(), sideSlider.value()))
        except:
            textBlock.setText('Choose the City name first, please')


    ##############################################################
    #                           LOGO                             #
    ##############################################################

    image = QPixmap('logo.png')
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignHCenter)

    logo.setStyleSheet('margin: 20px;')
    grid.addWidget(logo, 0, 1)
    
    # def marketLstFunc():
    ##############################################################
    #                         MARKET LIST                        #
    ##############################################################

    marketBox = QComboBox()
    marketBox.addItem('First set the City and current search radius, please')
    marketBox.setStyleSheet('color: white;'
                                'font-size: 12px;'
                                'background-color: slategray;'
                                'border: 1px solid white;'
                                'padding: 5px;'                    
                                'max-width: 300px ;')
    marketBox.setPlaceholderText('nobody knows where it will appear')
    marketBox.currentIndexChanged.connect(sendSLTextFunc)
    grid.addWidget(marketBox, 2, 1)  

    ##############################################################
    #                           MENU                             #
    ##############################################################

    comboBox = QComboBox()
    comboBox.addItem('Select the City, please.')
    comboBox.addItems(addCitiesToComboBoxFunc())
    comboBox.setStyleSheet('color: white;'
                            'font-size: 12px;'
                            'background-color: slategray;'
                            'border: 1px solid white;'
                            'padding: 5px;'                    
                            'max-width: 300px ;')
    
    comboBox.currentIndexChanged.connect(uiPrintFunc)
    grid.addWidget(comboBox, 1, 1)    

    ##############################################################
    #                      SLIDER FUNCTIONS                      #
    ##############################################################

    def sliderEvent():
        print('slider is mooving')
        uiPrintFunc()   

    def displaySliderValue():
        label.setText(str(sideSlider.value()) + 'km') 
        
    ##############################################################
    #                          SLIDER                            #
    ##############################################################

    sideSlider = QSlider()
    sideSlider.setTickPosition(QSlider.TicksBelow)
    sideSlider.setTickInterval(5)
    sideSlider.setMinimum(0)
    sideSlider.setMaximum(50)
    sideSlider.valueChanged.connect(displaySliderValue)
    sideSlider.valueChanged.connect(sliderEvent)

    dial = QDial()
    dial.setGeometry(100, 100, 100, 100)
    value = dial.value()
    dial.setValue(value)

    grid.addWidget(sideSlider, 0, 2)


    ##############################################################
    #                      SLIDER TEXT                           #
    ##############################################################

    label = QLabel()
    label.setStyleSheet('font: "Tahoma";'
                        'max-width: 40px;'
                        'color: White;'
                        'border-radius: 10px;'
                        'border: 1px solid grey;'
                        'background: slategrey;'
                        'max-height: 20px;'
                        'text-align: center;')

    label.setText(str(value))
    grid.addWidget(label, 0, 3)

    ##############################################################
    #                         TEXT LINE                          #
    ##############################################################

    searchLine = QLineEdit()
    searchLine.setStyleSheet('background: white;'
                            'border-radius: 10px;'
                            'border: 1px solid slategrey;'
                            'margin: 0px;'
                            'max-width: 420px;'
                            'min-height: 20px;')
                            
    searchLine.setPlaceholderText("Type market's name here for more information")
    searchLine.setAlignment(QtCore.Qt.AlignHCenter)
    icon = app.style().standardIcon(QtWidgets.QStyle.SP_ArrowUp)

    action = searchLine.addAction(icon, searchLine.TrailingPosition)
    action.triggered.connect(sendSLTextFunc)

    searchLine.show()
    grid.addWidget(searchLine, 1, 4)

       
    window.setLayout(grid)
    window.show()  

    # Запуск
    sys.exit(app.exec())

uiFunc()

