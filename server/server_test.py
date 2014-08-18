#!/usr/bin/env python
import os
import server
import unittest
import tempfile


class ServerTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()
        server.init_db()
        server.init_core()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(server.app.config['DATABASE'])

class VatTestCase(ServerTestCase):

    def test_vat_add(self):
        rv = self.app.post('/vat', data=dict(
            value=23))
        self.assertEqual(rv.status[:3],'201',"Błąd obsługi dodawania VATu")

    def test_vat_double_add(self):
        rv = self.app.post('/vat', data=dict(
            value=23))
        rv = self.app.post('/vat', data=dict(
            value=23))
        self.assertIn(rv.status, "400", "Błąd obługi podwójengo dodawania VATu")

    def test_vat_no_parameters(self):
        rv = self.app.post('/vat', data=dict())
        self.assertIn(rv.status, "400", "Błąd obsługi braku parametrów VATu")  

    def test_vat_list(self):
#        self.app.post('/vat', data=dict(
#            value=7))
#        self.app.post('/vat', data=dict(
#            value=0))
#        self.app.post('/vat', data=dict(
#            value=23))

        self.app.nkf.vat_add(7)
        rv = self.app.get('/vat')
        self.assertEqual(rv.status[:3], "200", "Zły status przy listowaniu VATu")
        self.assertIn(rv.data, 7, "Brak VATu 7%")
        self.assertIn(rv.data, 23, "Brak VATu 23%")
        self.assertIn(rv.data, 0, "Brak VATu 0%")



if __name__ == '__main__':
    unittest.main()
