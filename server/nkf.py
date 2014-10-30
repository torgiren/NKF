from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
class NKF:

    def __init__(self):
        """
        TODO: defaultowy config
        """
        self.__config = {}
        self.__config['DATABASE'] = 'sqlite:///baza.db'
        self.__configured = False
    def update_config(self, values):
        """
        Uaktualnia konfigurację NKF
        TODO: Sprawdzanie wartości pod kątem sensowności
        """
        self.__config.update(values)

    def init(self):
        engine = create_engine(self.__config['DATABASE'], echo=True)
        Session = sessionmaker()
        Session.configure(bind=engine)
        self.__db = Session()
        pass

    def vat_list(self):
        return "Lista"

    def vat_add(self, value):
        return "True"
    pass
