
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTreeView, QFrame
from PyQt5.QtCore import Qt
from pyswip import Prolog

class DiagnosticoMedico(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Especialista para Diagnóstico Médico")
        self.setGeometry(100, 100, 500, 500)
        self.setStyleSheet("background-color: #C9E2DF;")

        self.central_widget = QFrame(self)
        self.central_widget.setStyleSheet("background-color: #C9E2DF;")
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.titulo = QLabel("SISTEMA ESPECIALISTA PARA DIAGNÓSTICO MÉDICO", self)
        self.titulo.setStyleSheet("font-weight: bold; font-size: 13px; color: #359A94;")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.titulo)

        self.entry = QLineEdit(self)
        self.entry.setStyleSheet("border: 2px solid; border-radius: 10px; padding: 5px; border-color: #359A94; background-color: white;")
        self.entry.setPlaceholderText("Pesquise pelos sintomas...")
        self.layout.addWidget(self.entry)

        self.treeview_frame = QFrame(self)
        self.treeview_frame.setLayout(QHBoxLayout())
        self.layout.addWidget(self.treeview_frame)

        self.treeview_frame.layout().addSpacing(10)
        
        self.sintomas_selecionados_treeview = QTreeView(self)
        self.treeview_frame.layout().addWidget(self.sintomas_selecionados_treeview)
       
        self.sintomas_selecionados_treeview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sintomas_selecionados_treeview.setIndentation(0) 
        self.sintomas_selecionados_treeview.setHeaderHidden(True)
        

        self.treeview_frame.layout().addSpacing(20)
        
        self.sintomas_treeview = QTreeView(self)
        self.treeview_frame.layout().addWidget(self.sintomas_treeview)

        self.sintomas_treeview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sintomas_treeview.setIndentation(0)  
        self.sintomas_treeview.setHeaderHidden(True)
        
        self.treeview_frame.layout().addSpacing(10)
        
        self.resultado_label = QLabel("", self)
        self.resultado_label.setAlignment(Qt.AlignCenter)
        self.resultado_label.setStyleSheet("font-weight: bold; color: #359A94; font-size: 13px;")
        self.layout.addWidget(self.resultado_label)

        self.bottom_frame = QFrame(self)
        self.bottom_frame.setLayout(QHBoxLayout())
        self.layout.addWidget(self.bottom_frame)

        self.sair_button = QPushButton("Sair", self)
        self.sair_button.setStyleSheet("""QPushButton {
                                                border: 2px solid;
                                                border-radius: 9px;
                                                background-color: #359A94;
                                                color: white;
                                                border-color: #359A94;
                                                font-size: 13px;
                                                font-weight: bold;
                                            }
                                            QPushButton:hover {
                                                background-color: #C9E2DF;
                                                color: #359A94;
                                            }
                                        """)
        self.sair_button.clicked.connect(self.close)
        self.bottom_frame.layout().addWidget(self.sair_button)

        self.bottom_frame.layout().addSpacing(50)  

        self.diagnosticar_button = QPushButton("Diagnosticar", self)
        self.diagnosticar_button.setStyleSheet("""QPushButton {
                                                border: 2px solid;
                                                border-radius: 9px;
                                                background-color: #359A94;
                                                color: white;
                                                border-color: #359A94;
                                                font-size: 13px;
                                                font-weight: bold;
                                            }
                                            QPushButton:hover {
                                                background-color: #C9E2DF;
                                                color: #359A94;
                                            }
                                        """)
        self.diagnosticar_button.clicked.connect(self.diagnosticar)
        self.bottom_frame.layout().addWidget(self.diagnosticar_button)

        self.entry.textChanged.connect(self.filter_list)
        self.sintomas_treeview.clicked.connect(self.add_sintoma)
        self.sintomas_selecionados_treeview.clicked.connect(self.remove_sintoma)

        self.prolog = Prolog()
        self.prolog.consult("database.pl")

        self.sintomas_model = QtGui.QStandardItemModel()  
        self.sintomas_treeview.setModel(self.sintomas_model)

        self.sintomas_selecionados_model = QtGui.QStandardItemModel()  
        self.sintomas_selecionados_treeview.setModel(self.sintomas_selecionados_model)  
        
        item_style = """QTreeView::item {
                            border: 2px solid;
                            border-radius: 10px;
                            background-color: #359A94;
                            border-color: #359A94;
                            color: white;
                            height: 20px;
                            margin: 5px;
                            font-weight: bold;
                        }
                        """
        
        self.sintomas_selecionados_treeview.setStyleSheet(item_style)
        self.sintomas_treeview.setStyleSheet(item_style)

        for sintoma in self.prolog.query("sintoma(S)"):
            item = QtGui.QStandardItem(sintoma['S']) 
            self.sintomas_model.appendRow(item)

    def filter_list(self, input_text):
        selected_sintomas = [self.sintomas_selecionados_model.item(row).text() for row in range(self.sintomas_selecionados_model.rowCount())]
        self.sintomas_model.clear()
        for sintoma in self.prolog.query("sintoma(S)"):
            if input_text.lower() in sintoma['S'].lower() and sintoma['S'] not in selected_sintomas:
                item = QtGui.QStandardItem(sintoma['S'])
                self.sintomas_model.appendRow(item)
        

    def add_sintoma(self, index):
        selected_items = self.sintomas_treeview.selectedIndexes()
        for item in selected_items:
            sintoma = self.sintomas_model.itemFromIndex(item).text()
            self.sintomas_selecionados_model.appendRow(QtGui.QStandardItem(sintoma)) 
        self.filter_list(self.entry.text())
        self.entry.clear()

    def remove_sintoma(self, index):
        selected_items = self.sintomas_selecionados_treeview.selectedIndexes()
        for item in selected_items:
            self.sintomas_selecionados_model.removeRow(item.row())
        self.filter_list(self.entry.text())

    def diagnosticar(self):
        sintomas_selecionados = [self.sintomas_selecionados_model.item(row).text() for row in range(self.sintomas_selecionados_model.rowCount())]

        if not sintomas_selecionados:
            self.resultado_label.setText("Nenhum sintoma selecionado.")
            return


        query = "diagnostico({}, Doenca)".format(sintomas_selecionados)
        resultados = list(self.prolog.query(query))

        if resultados:
            doencas = [resultado['Doenca'] for resultado in resultados]
            self.resultado_label.setText("Possíveis diagnósticos: " + ", ".join(doencas))
        else:
            self.resultado_label.setText("Não foi possível realizar o diagnóstico.")

app = QApplication([])
window = DiagnosticoMedico()
window.show()
app.exec_()