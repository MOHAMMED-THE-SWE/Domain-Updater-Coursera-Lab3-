import re
import csv

def contain_domain(old_domain,data):
    pattern = r"[\w\.-]+@" + old_domain + r"$"
    if re.match(pattern,data):
        return True
    return False

def replace_domain(old_domain, new_domain, data):
    address = re.sub(old_domain, new_domain, data)
    return address

def main():
    old_domain, new_domain = "abc.edu", "xyz.edu"
    file_name = "email.csv"
    report_name = ""
    old_email_list = []
    new_email_list = []
    with open(file_name) as file:
        csv.register_dialect("HAMA",skipinitialspace=True,strict=True)
        read = list(csv.reader(file,dialect="HAMA"))

        email_list = [email[1] for email in read[1:]]

        for data in email_list:
            if contain_domain(old_domain,data):
                old_email_list.append(data)
                replace_email = replace_domain(old_domain, new_domain, data)
                new_email_list.append(replace_email)

        for line in read:
            for old, new in zip(old_email_list, new_email_list):
                if line[1] == old:
                    line[1] = new

        with open("report.csv", "w") as report:
            writer = csv.writer(report,lineterminator="\n")
            writer.writerows(read)

main()






























