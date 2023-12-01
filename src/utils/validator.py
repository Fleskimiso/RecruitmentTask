class Validator:

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
        cleaned_telephone = ''.join(filter(str.isdigit, telephone.strip('+() ')))
        # Store telephone numbers as 9 digits
        if cleaned_telephone != '' and len(cleaned_telephone) >= 9:
            return cleaned_telephone[-9:]
        return False
