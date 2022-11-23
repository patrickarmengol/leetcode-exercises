import re

def num_unique_emails(emails):
    semails = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        clean_email = '@'.join((local, domain))
        semails.add(clean_email)
    return len(semails)

def main():
    tests = [
        ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],
        ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    ]
    for test in tests:
        print(num_unique_emails(test))


if __name__ == '__main__':
    main()