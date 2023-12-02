import ldap3
import json
from ldap3 import Server, Connection,SUBTREE,ALL_ATTRIBUTES,ALL_OPERATIONAL_ATTRIBUTES
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersInGroups

hostname = "192.168.56.102"
base_dn = "CN=Users,DC=shivareddy,DC=domain,DC=local"
user_name = "shivareddy\\administrator"
password = "Harshikam@101220"
#WIN-H9N8MKFJRLT
server = Server(hostname, port=389, use_ssl=False)
conn = Connection(server, user_name, password, auto_bind=True)

#conn.search(base_dn, '(&(objectclass=user)(sAMAccountName=sravya))',search_scope=SUBTREE, attributes = ["objectGuid", "sAMAccountName", "displayName","userPrincipalName","givenName","sn","mail"])
#conn.search(base_dn, '(&(objectclass=person)(sAMAccountName=sravya))',search_scope=SUBTREE, attributes=['sAMAccountName','userAccountControl', 'lockoutTime'])
conn.search(base_dn, '(&(objectclass=*)(sAMAccountName=sravya))',search_scope=SUBTREE, attributes=[ALL_ATTRIBUTES,ALL_OPERATIONAL_ATTRIBUTES])

response = json.loads(conn.response_to_json())

print(response)


#for i in conn.entries:
#    print('USER = {0} : {1} : {2}'.format(i.sAMAccountName.values[0], i.displayName.values[0], i.userAccountControl.values[0])