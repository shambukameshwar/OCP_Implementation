import json
import xmltodict
import MySQLdb
from jsonpath_rw import jsonpath
from jsonpath_rw_ext import parse
import jsonpath_rw_ext as jp

with open("./ResultFile/Result/output.xml") as xml_file:

    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

    # generate the object using json.dumps()
    # corresponding to json data

    json_data = json.dumps(data_dict)

    # Write the json data to output
    # json file
    with open("output.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()
print("output file generated successfully")

# Json value retrival:

# read file from disk
json_file = open("output.json")
json_data = json.load(json_file)

for suitename in jp.match("$.robot.statistics.suite.stat[@name]", json_data):
    print(" {}".format(suitename))
suitename = suitename
# suitename = str(suitename)
# print(suitename)
# suitename = suitename.rsplit('.')[-1]
# suitename = suitename.replace("'", "")
# suitename = suitename.replace("}", "")
print(suitename)

for suitestatus in jp.match("$.robot.suite.status[@status]", json_data):
    print(" {}".format(suitestatus))
suitestatus = suitestatus
print(suitestatus)

for starttime in jp.match("$.robot.suite.status[@starttime]", json_data):
    print(" {}".format(starttime))
starttime = starttime
starttime = starttime[:4] + '-' + starttime[4:]
starttime = starttime[:7] + '-' + starttime[7:]
print(starttime)

for endtime in jp.match("$.robot.suite.status[@endtime]", json_data):
    print(" {}".format(endtime))
endtime = endtime
endtime = endtime[:4] + '-' + endtime[4:]
endtime = endtime[:7] + '-' + endtime[7:]
print(endtime)

for testpass in jp.match("$..robot.statistics.suite.stat[@pass]", json_data):
    print(" {}".format(testpass))
testpass = int(testpass)
print(testpass)

for testfail in jp.match("$..robot.statistics.suite.stat[@fail]", json_data):
    print(" {}".format(testfail))
testfail = int(testfail)
print(testfail)

totaltest = testpass + testfail
print(totaltest)

# Open database connection
db = MySQLdb.connect("localhost", "grafanaReader", "Cogni123", "robot_results")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
    "INSERT INTO SUITEDETAILS(SUITENAME, SUITESTATUS, TOTALCASES, PASSED, FAILED, STARTTIME, ENDTIME)"
    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
)
data = (suitename, suitestatus, totaltest,
        testpass, testfail, starttime, endtime)

try:
    # Executing the SQL command
    cursor.execute(insert_stmt, data)

    # Commit your changes in the database
    db.commit()

except:
    # Rolling back in case of error
    db.rollback()

print("Data inserted")

# Closing the connection
db.close()
