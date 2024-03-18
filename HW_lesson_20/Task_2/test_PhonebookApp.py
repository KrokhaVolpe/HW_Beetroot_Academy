import unittest
import json
import os
from phonebook_logic import PhonebookApp


class TestPhonebookApp(unittest.TestCase):

    def setUp(self):
        """This method configures the test environment before each test run. """
        self.sample_data = [{"name": "John", "last_name": "Doe", "phone": "1234567890"},
                            {"name": "Jane", "last_name": "Smith", "phone": "9876543210"}]
        self.phonebook_name = "test_phonebook.json"
        self.create_test_phonebook()
        

    def tearDown(self):
        """This method is called after each test is executed and deletes the test file."""
        os.remove(self.phonebook_name)
        

    def create_test_phonebook(self):
        """This method creates a test file with phonebook data."""
        with open(self.phonebook_name, "w", encoding='utf-8') as file:
            json.dump(self.sample_data, file)
            

    def test_load_phonebook_data(self):
        """This method checks if the phonebook data is being loaded correctly."""
        app = PhonebookApp(self.phonebook_name)
        self.assertEqual(app.phonebook_data, self.sample_data)
        

    def test_add_entry(self):
        """This method verifies that a new entry has been added to the phonebook. """
        app = PhonebookApp(self.phonebook_name)
        new_entry = {"name": "Alice", "last_name": "Johnson", "phone": "5555555555"}
        app.add_entry(new_entry)
        self.assertIn(new_entry, app.phonebook_data)
        

    def test_search_entry(self):
        """This method tests the phonebook search function."""
        app = PhonebookApp(self.phonebook_name)
        result = app.search_entry("John")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "John")
        

    def test_update_entry(self):
        """This method checks if an entry in the phonebook has been updated. It updates the entry with index 0 with new data and checks if it is really updated."""
        app = PhonebookApp(self.phonebook_name)
        updated_entry = {"name": "John", "last_name": "Doe", "phone": "9999999999"}
        app.update_entry(0, updated_entry)
        self.assertEqual(app.phonebook_data[0], updated_entry)
        

    def test_delete_entry(self):
        """This method checks if an entry is deleted from the phonebook."""
        app = PhonebookApp(self.phonebook_name)
        deleted_entry = app.delete_entry(0)
        self.assertEqual(deleted_entry, {"name": "John", "last_name": "Doe", "phone": "1234567890"})
        self.assertEqual(len(app.phonebook_data), 1)
        

    def test_restore_database(self):
        """This method checks the recovery of the phonebook database."""
        app = PhonebookApp(self.phonebook_name)
        app.restore_database()
        self.assertEqual(app.phonebook_data, [])


if __name__ == '__main__':
    unittest.main()
