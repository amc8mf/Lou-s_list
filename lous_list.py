#Alex_Colegrove CS1111, Fall 2016

def instructors(department):
    department = department.upper()
    import urllib.request
    url = "http://stardock.cs.virginia.edu/louslist/Courses/view/" + department
    stream = urllib.request.urlopen(url)
    professors = []


    for line in stream:
        line = (line.decode("UTF-8")).strip('\n')
        line = line.split(';')
        if line[0] == department and line[4] not in professors:
            professors.append(line[4])

    professors.sort()
    return professors


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    dept_name = dept_name.upper()
    import urllib.request
    url = "http://stardock.cs.virginia.edu/louslist/Courses/view/" + dept_name
    stream = urllib.request.urlopen(url)
    info = []
    final = []
    for line in stream:
        line = (line.decode("UTF-8")).strip('\n')
        line = line.split(';')
        info.append(line)

    for a in range(0,len(info)):
        if dept_name not in info[a]:
            continue
        if has_seats_available == True:
            if int(info[a][15]) >= int(info[a][16]):
                continue
        if level != None:
            if int(level) + 1000 < int(info[a][1]):
                continue
        if not_before != None:
            if int(not_before) >= int(info[a][12]) or int(info[a][12]) == -1:
                continue
        if not_after != None or info[a][13] == -1:
            if int(not_after) <= int(info[a][13]):
                continue
        final.append(info[a])
    return final








