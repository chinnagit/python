from dbconnection import DbConnection

class DbManager:

    def createuser(self, jsondata):
        try:
            dbconnection = DbConnection()
            cursor = dbconnection.getcursor()
            query = "INSERT INTO user(id, user_name, identity_provider) \
            VALUES('"+jsondata['id']+"', '"+jsondata['userName']+"', '"+ \
                    jsondata['urn:symantec:scim:schemas:extension:symantec:2.0:User']['identityProvider']['id']+"')"
            cursor.execute(query)
            connection = dbconnection.getconnection()
            connection.commit()
            cursor.execute("SELECT * FROM user")
            myresult = cursor.fetchall()
            for user in myresult:
                print "user id: %s, name: %s " % (user[0], user[1])
        except Exception as excp:
            print'exception while inserting user ', excp



# xx = dbconnection.dbManager()

# xx.getRules()