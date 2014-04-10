import sys
import unittest

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123qwe@AS')
        sql_manager.register('Tester_1', '1234Tester_1')
        sql_manager.register('Tester_3', '12345678Qw')
        sql_manager.register('Tester_2', '12345678@')
        sql_manager.register('Tester_4', 'qweqweqwe@')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        sql_manager.register('Dinko', '123D@123')

        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', '123D@123'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        self.assertEqual(logged_user.get_username(), 'Tester')


        logged_user = sql_manager.login('\' OR 1==1--', '123')
        self.assertFalse(logged_user)

        logged_user = sql_manager.login('Blq', '\' OR 1==1--')
        self.assertEqual(False,logged_user)

    def test_login_substring(self):
        logged_user = sql_manager.login('Tester_1', '1234Tester_1')
        self.assertFalse(logged_user)

    def test_login_substring_1(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_special_symbol_wrong(self):
        logged_user = sql_manager.login('Tester_3', '12345678Qw')
        self.assertFalse(logged_user)

    def test_login_special_symbol_pass(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_number_wrong(self):
        logged_user = sql_manager.login('Tester_4', 'qweqweqwe@')
        self.assertFalse(logged_user)

    def test_login_number_pass(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_capital_letter_wrong(self):
        logged_user = sql_manager.login('Tester_4', 'qweqweqwe@')
        self.assertFalse(logged_user)

    def test_login_capital_letter_pass(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '1235678')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password_wrong(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        new_password = "12345@www"
        reg_success = sql_manager.change_pass(new_password, logged_user)

        self.assertEqual(False, reg_success)

    def test_change_password_pass(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        new_password = "123qwe@AS@"
        reg_success = sql_manager.change_pass(new_password, logged_user)

        self.assertEqual(True, reg_success)

    def test_change_password_wrong_1(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        new_password = "123qwe@ASTester"
        reg_success = sql_manager.change_pass(new_password, logged_user)

        self.assertEqual(False, reg_success)

    def test_change_password_pass_numb(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        new_password = "123qwe@AS@"
        reg_success = sql_manager.change_pass(new_password, logged_user)

        self.assertEqual(True, reg_success)

    def test_change_password_wrong_numb(self):
        logged_user = sql_manager.login('Tester', '123qwe@AS')
        new_password = "qwe@ASTester"
        reg_success = sql_manager.change_pass(new_password, logged_user)

        self.assertEqual(False, reg_success)
        #logged_user_new_password = sql_manager.login('Tester', new_password)
        #self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
