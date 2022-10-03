import datetime

def day_of_year(date):
    return datetime.datetime.fromisoformat(date).strftime("%j").lstrip('0')

def main():
    print(day_of_year('2012-02-03'))

if __name__ == '__main__':
    main()


"""
kind of defeats the purpose of the challenge if i just use a library maybe?
i'd rather not do datetime stuff though
https://youtu.be/-5wpm-gesOY?t=370
"""