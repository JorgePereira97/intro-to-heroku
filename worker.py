import psycopg2
import time
import os

'''connection = psycopg2.connect(user = "isneqpdtrrraup",
                              password = "d6f221a93bf2e038e37179cf4e0d4a18c321241340b0bf4368439fa212fc9b06",
                              host = "ec2-176-34-183-20.eu-west-1.compute.amazonaws.com",
                              port = "5432",
                              database = "delcjv8nidnnch")'''

#connection = psycopg2.connect("postgres://isneqpdtrrraup:d6f221a93bf2e038e37179cf4e0d4a18c321241340b0bf4368439fa212fc9b06@ec2-176-34-183-20.eu-west-1.compute.amazonaws.com:5432/delcjv8nidnnch")

connection = psycopg2.connect(os.environ['DATABASE_URL'])

cursor = connection.cursor()

cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")


'''repeater = int(input("Want to repeat this process how many times? "))
timer = int(input("How many seconds between each repeat? "))'''

for y in range(100):    
    print("\n")
    tableToSync = '''SELECT * FROM test.valuestosync'''
    tableSynced = '''SELECT * FROM test.valuessynced'''
    
    cursor.execute(tableToSync)
    toInsert = cursor.fetchall()
    
    print(y + 1,": Inserting in Sync table \n", toInsert)
    for x in toInsert:
        stringToInsert = "Insert into test.valuessynced(valord, sync) values (" + str(x[0]) + ", 's')"
        cursor.execute(stringToInsert)
        stringToExe = "Update test.valuestosync set sync = 's' WHERE valorc = " + str(x[0])
        cursor.execute(stringToExe)
        connection.commit()
     
    cursor.execute(tableToSync + " WHERE sync = 's'")
    toDelete = cursor.fetchall()
         
    print(y + 1,": Deleting To Sync table \n", toDelete)
    for x in toDelete:
        stringToDel = "DELETE FROM test.valuestosync where valorc = " + str(x[0])
        cursor.execute(stringToDel)
        connection.commit()
    
    if(y is not 99):
        time.sleep(20)
