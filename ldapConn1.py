import ldap3
import json
from ldap3 import Server, Connection
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersInGroups

server = Server('WIN-H9N8MKFJRLT', port=389, use_ssl=False)
conn = Connection(server, 'Administrator@shivareddy.domain.local','Harikam@01072017',auto_bind=True)
#print(server.schema)
conn.search('dc=domain,dc=local','(&(objectclass=user))')
entry = conn.entries[0]
print(entry)
print(conn)
#response = json.loads(conn.response_to_json())
#print(response)

#for i in conn.entries:
#    print('USER = {0} : {1} : {2}'.format(i.sAMAccountName.values[0], i.displayName.values[0], i.userAccountControl.values[0])