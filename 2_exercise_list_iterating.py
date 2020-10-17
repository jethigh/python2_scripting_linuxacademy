users = [ { 'admin': False, 'active': True, 'name': 'user1'},
        { 'admin': False, 'active': True, 'name': 'user2'},
        { 'admin': True, 'active': True, 'name': 'user3'},
        { 'admin': False, 'active': False, 'name': 'user4'},
        { 'admin': True, 'active': False, 'name': 'user5'}
]

counter = 1
for user in users:
    if user['admin']:
        if user['active']:
            print('%i. ACTIVE - (ADMIN) %s' % (counter, user['name']))
        else:
            print('{}. (ADMIN) {}').format(counter, user['name'])
    elif user['active']:
        print('%s. ACTIVE %s' % (counter, user['name']))
    else:
        print('{}. {}'.format(counter,user['name']))
    counter += 1
