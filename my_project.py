import re

list_email = []
dict_info = {}


def email_parse(email_address):
    parsed = re.findall(r"([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$", email_address)
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(["username", "domain"], parsed[0]))
    else:
        val_1 = re.findall(r"\w+", email_address)
        al_2 = val_1[0]
        val_3 = re.findall(r'@\w+[/.]\w+', email_address)
        dict_info['username'] = val_2
        dict_info["domain"] = ''.join(val_3)

        return dict_info


print(email_parse('someone@geekbrains.ru'))
