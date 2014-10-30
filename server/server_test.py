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
        self.app.core = server.NKF()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(server.app.config['DATABASE'])

class VatTestCase(ServerTestCase):

    def test_vat_add(self):
        rv = self.app.post('/vat', data=dict(
            value=23))
        self.assertEqual(rv.status[:3],'201',"Błąd obsługi dodawania VATu")
        self.assertEqual(len(self.app.core.vat_list()), 1, "Błąd dodawania VATu - nie dodano")

    def test_vat_double_add(self):
        rv = self.app.post('/vat', data=dict(
            value=23))
        rv = self.app.post('/vat', data=dict(
            value=23))
        self.assertEqual(rv.status[:3], "400", "Błąd obługi podwójengo dodawania VATu")

    def test_vat_no_parameters(self):
        rv = self.app.post('/vat', data=dict())
        self.assertEqual(rv.status[:3], "400", "Błąd obsługi braku parametrów VATu")

    def test_vat_list(self):
#        self.app.post('/vat', data=dict(
#            value=7))
#        self.app.post('/vat', data=dict(
#            value=0))
#        self.app.post('/vat', data=dict(
#            value=23))

        self.app.core.vat_add(7)
        rv = self.app.get('/vat')
        data = str(rv.data)
        self.assertEqual(rv.status[:3], "200", "Zły status przy listowaniu VATu")
        self.assertIn("7", data, "Brak VATu 7%")
        self.assertIn("23", data, "Brak VATu 23%")
        self.assertIn("0", data, "Brak VATu 0%")

    def test_vat_delete(self):
        self.app.core.vat_add("5")
        rv = self.app.delete('/vat/1')
        self.assertEqual(rv.status[:3], "200")
        self.assertNotIn(self.app.core.vat_list(), "5", "Nie usunięty VAT")

    def test_vat_double_delete(self):
        self.app.core.vat_add("5")
        self.app.core.vat_add("7")
        rv = self.app.delete('/vat/7')
        count = len(self.app.core.vat_list())
        rv = self.app.delete('/vat/7')
        self.assertEqual(rv.status[:3], "404", "Bład obsługi usuniecia niestniejącego elementu - zly status")
        self.assertEqual(len(self.app.core.vat_list()), count, "Usunięcie nie tego elementu w przyadku braku żądanego elementu")



if __name__ == '__main__':
    unittest.main()
