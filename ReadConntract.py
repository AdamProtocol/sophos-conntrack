with open('conntrack.txt','r') as test:
    content = test.readlines()

main_list_conntrack = []
conv_dict = {}

def get_details_list(conntrack):
    new_conntrack = []
    for i in conntrack:
        if i != '':
            new_conntrack.append(i)
    return new_conntrack


#create the main list of conntracks
for i in content:
    index = content.index(i)
    conv_list = i.split(' ')
    conv_list = get_details_list(conv_list)
    if conv_list[0].find('[') == 0:
        main_list_conntrack.append(conv_list)

for element in main_list_conntrack:
    element.pop()
    element.pop(0)


for eachstr in main_list_conntrack:
    for i in eachstr:
        index = eachstr.index(i)
        eachstr[index] = i.replace('=',':')

for item in main_list_conntrack:
    for check in item:
        if check.find(':') == -1:
            item.remove(check)

for conn in main_list_conntrack:
    connection = main_list_conntrack.index(conn)
    conv_dict[f'connection{connection}']= {item.split(":")[0]: item.split(":")[1] for item in conn}
    if int(connection) > 10:
        break


        
