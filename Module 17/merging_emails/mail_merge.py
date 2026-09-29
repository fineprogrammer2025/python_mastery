with open("Names.txt", "r") as n_file:
    with open("Message.txt", "r") as m_file:
        mail_body = m_file.read()
        for name in n_file:
            mail = f"Hello {name}\n{mail_body}"
            with open(f"{name.strip()}.txt", "w") as m_file:
                m_file.write(mail)
print("All done, Messages created and ready")
print("------------------------------------")