user = { 'admin': False, 'active': True, 'name': 'user1'}

if user['admin']:
    if user['active']:
        print('ACTIVE - (ADMIN) %s' % (user['name']))
    else:
        print('(ADMIN) {}').format(user['name'])
elif user['active']:
    print('ACTIVE %s' % user['name'])
else:
    print(user['name'])