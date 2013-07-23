import datetime
import pprint
import random
import subprocess

start_date = datetime.datetime(2013, 5, 25, 0, 0, 0)

fartbanner_rows = list(x.strip() for x in open('fartbanner.txt', 'rb'))

max_fart_len = max(len(x) for x in fartbanner_rows)

for row in xrange(len(fartbanner_rows)):
    fartbanner_rows[row] += ' ' * (max_fart_len - len(fartbanner_rows[row]))

pprint.pprint(fartbanner_rows)

commit_list = []

commit_messages = ["Work-in-progress", "Update", "Fix text file", "Editing text file", "Improved text file", "Adjustment", "Build"]

for col in xrange(max_fart_len - 1, -1, -1):
    for row in xrange(len(fartbanner_rows) - 1, -1, -1):
        item = fartbanner_rows[row][col]
        commit_count = 0
        if item == "#":
            commit_count = 2
        elif item == ".":
            commit_count = 1
        for commit_msg in xrange(commit_count):
            hr, mn, sec = random.randint(8, 18), random.randint(1, 58), random.randint(1, 58)
            commit_date = start_date.replace(hour=hr,minute=mn,second=sec)
            commit_list.append((commit_date, random.choice(commit_messages), "\n".join(fartbanner_rows)))
            fartbanner_rows[row] = fartbanner_rows[row][:-1] + '.'
        fartbanner_rows[row] = fartbanner_rows[row][:-1]
        start_date += datetime.timedelta(days=-1)

commit_list.sort()

for commit_date, commit_message, commit_file in commit_list:
    print commit_file
    with open('banner.txt', 'wb') as out:
        out.write(commit_file)
    cmdline = ["hg", "commit", "--date", "{} -0700".format(commit_date), '-m', commit_message]
    print cmdline
    print subprocess.check_output(cmdline)
    print "----"
