from datetime import date

def get_date(date_string):
    months = {"january": 1, "jan": 1, "february": 2, "feb": 2, "march": 3, "mar": 3, "april": 4, "apr": 4, "may": 5, "june": 6, "july": 7, "august": 8, "aug": 8, "september": 9, "sept": 9, "october": 10, "oct": 10, "november": 11, "nov": 11, "december": 12, "dec": 12}

    m,d,y = date_string.split()
    m = months[m.lower()]
    d = int(d)
    y = int(y)
    return date(y, m, d)


def parse_file_metadata(filepath, filename):
    with open(filepath, 'r') as f:
        try:
            f.readline()
            title = ": ".join(f.readline().strip().split(": ")[1:])
            desc = ": ".join(f.readline().strip().split(": ")[1:])
            date = ": ".join(f.readline().strip().split(": ")[1:])
            date = get_date(date)
            f_tuple = (title, date, desc, filename)
            return f_tuple
        except Exception as e:
            print(f"messed up reading {filepath}")
            print(e)
            return None

def parse_index_tags(filepath):
    with open(filepath, 'r') as f:
        try:
            lines = f.readlines()
            for line in lines:
                if "index tags" in line:
                    tags = ": ".join(line.strip().split(": ")[1:]).split(", ")
                    return tags
        except Exception as e:
            print(f"couldn't get tags from {filepath}")
            print(e)
            return None
    print(f"no tags present in {filepath}")
    return None

def parse_category_tags(filepath):
    with open(filepath, 'r') as f:
        try:
            lines = f.readlines()
            for line in lines:
                if "category tags" in line:
                    tags = ": ".join(line.strip().split(": ")[1:]).split(", ")
                    return tags
        except Exception as e:
            print(f"couldn't get tags from {filepath}")
            print(e)
            return None
    print(f"no tags present in {filepath}")
    return None

def copy_pdfified(old_filepath, new_filepath):
    with open(old_filepath, 'r') as old_f:
        try:
            old_f.readline()
            title = ": ".join(old_f.readline().strip().split(": ")[1:])
            desc = ": ".join(old_f.readline().strip().split(": ")[1:])
            date = ": ".join(old_f.readline().strip().split(": ")[1:])
            date = get_date(date)
            with open(new_filepath, 'w') as new_f:
                new_f.write(f"# {title}\n\n")
                new_f.write(f"## {date}\n\n")
                new_f.write(f"### {desc}\n\n")
                for line in old_f.readlines():
                    new_f.write(line)
        except Exception as e:
            print(f"messed up writing {old_filepath} into {new_filepath}")
            print(e)
            return None