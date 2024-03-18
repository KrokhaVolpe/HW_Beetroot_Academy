import json

class PhonebookApp:
    def __init__(self, phonebook_name):
        self.phonebook_name = phonebook_name
        self.phonebook_data = self.load_phonebook_data()

    def load_phonebook_data(self):
        try:
            file_path = self.phonebook_name
            with open(file_path, "r", encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("Phonebook data not found. Create a new phonebook.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in phonebook data.")

    def save_phonebook_data(self):
        file_path = self.phonebook_name
        with open(file_path, "w", encoding='utf-8') as file:
            json.dump(self.phonebook_data, file, indent=2)

    def add_entry(self, entry):
        self.phonebook_data.append(entry)
        self.save_phonebook_data()

    def search_entry(self, query):
        results = []
        for entry in self.phonebook_data:
            full_name = f"{entry.get('name', '').lower()} {entry.get('last_name', '').lower()}"
            if query in full_name:
                results.append(entry)
            elif any(query in value.lower() for value in entry.values()):
                results.append(entry)
        return results

    def update_entry(self, index, entry):
        self.phonebook_data[index] = entry
        self.save_phonebook_data()

    def delete_entry(self, index):
        deleted_entry = self.phonebook_data.pop(index)
        self.save_phonebook_data()
        return deleted_entry

    def restore_database(self):
        self.phonebook_data = []
        self.save_phonebook_data()
