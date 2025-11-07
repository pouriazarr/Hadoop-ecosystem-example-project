import happybase
connection = happybase.Connection('localhost', 9090)
table = connection.table('customers')
table.put(b'312', {
    b'personal_data:name': b'hasan',
    b'personal_data:last_name': b'tavakoli',
    b'simecart_data:number': b'09412323'
})
row = table.row(b'312')
print(row[b'personal_data:name'])

results = table.scan(row_prefix=b'3')
for k, v in results:
    print(k)
    print(v)

print(table.delete(b'312'))