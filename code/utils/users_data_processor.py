import os
import json
import csv
import xml.etree.ElementTree as ET
from datetime import datetime


class UsersDataProcessor:
    def __init__(self, data_catalog):
        self.data_catalog = data_catalog
        self.users = []

    @staticmethod
    def validate_email(email):
        if email.count('@') == 1:
            parts = email.split('@')
            if len(parts[0]) >= 1 and '.' in parts[1]:
                domain_parts = parts[1].split('.')
                if 1 <= len(domain_parts[-1]) <= 4 and domain_parts[-1].isalnum():
                    return True
        return False

    @staticmethod
    def validate_telephone_number(telephone):
        # Remove special characters and leading zeros
        cleaned_telephone = ''.join(filter(str.isdigit, telephone)).lstrip('0')
        # Store telephone numbers as 9 digits
        if len(cleaned_telephone) == 9:
            return cleaned_telephone
        return None

    def read_json_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading JSON file {file_path}: {e}")
            return None

    def read_csv_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file, delimiter=';')
                data = [row for row in reader]
            return data
        except FileNotFoundError as e:
            print(f"Error reading CSV file {file_path}: {e}")
            return None

    def read_xml_file(self, file_path):
        try:
            all_users = []
            tree = ET.parse(file_path)
            root = tree.getroot()

            for user in root.findall('user'):
                user_data = {
                    'firstname': user.find('firstname').text,
                    'telephone_number': user.find('telephone_number').text,
                    'email': user.find('email').text,
                    'password': user.find('password').text,
                    'role': user.find('role').text,
                    'created_at': user.find('created_at').text,
                    'children': [
                        {
                            'name': child.find('name').text,
                            'age': int(child.find('age').text)
                        } for child in user.findall('children/child')
                    ]
                }
                return all_users.append(user_data)

        except (FileNotFoundError, ET.ParseError) as e:
            print(f"Error reading XML file {file_path}: {e}")

    def process_data(self):
        all_users = []

        for root, dirs, files in os.walk(self.data_catalog):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith('.json'):
                    data = self.read_json_file(file_path)
                    if data:
                        all_users.extend(data)

                elif file.endswith('.csv'):
                    data = self.read_csv_file(file_path)
                    if data:
                        all_users.extend(data)

                elif file.endswith('.xml'):
                    data = self.read_xml_file(file_path)
                    if data:
                        all_users.extend(data)

        for user in all_users:
            if 'email' in user and 'telephone_number' in user:
                if self.validate_email(user['email']) and user['telephone_number'].strip():
                    user['telephone_number'] = self.validate_telephone_number(user['telephone_number'])
                    if user['telephone_number']:
                        user['created_at'] = datetime.strptime(user['created_at'], '%Y-%m-%d %H:%M:%S')
                        key = user['email'] + user['telephone_number']
                        existing_user = next((x for x in self.users if x['email'] + x['telephone_number'] == key), None)
                        if existing_user:
                            if existing_user['created_at'] < user['created_at']:
                                self.users.remove(existing_user)
                                self.users.append(user)
                        else:
                            self.users.append(user)

        return self.users
