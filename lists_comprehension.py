fraza = 'as'
with open('/usr/share/dict/words') as words:
    print([w.strip() for w in words if fraza in w ])

