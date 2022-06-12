import re

_db_types = {
            'postgresql': 'postgres',
            }
_parametrs = {
            'targetServerType=master': 'target_session_attrs=read-write',
            'sslmode=verify-full': 'sslmode=verify-full',
            'prepareThreshold=0': '',
            'ssl=true': '',
            }


def translate(init_db):
    db_type = re.search(r'(\w:^/)?(\w+)(://)', init_db)[2]
    serverlist = str(','.join([i[0] for i in re.findall
                (r"((http://|https://)?(((\w+\.){1,3}\w+))(:\d{2,4})?)", init_db)]))
    db_name = re.search(r'(\w/){1}(\w+)(\s)?', init_db)[2]
    parametrslist_java = [i[1] for i in re.findall(r"(\?|&)((\w+=\w+)(-\w+)?)", init_db)]
    if parametrslist_java:
        parametrslist_python = '?' + str('&'.join(([_parametrs[i] for i in parametrslist_java if _parametrs[i]])))
    else:
        parametrslist_python = ''
    return f'{_db_types[db_type]}://db_user:dbpass@{serverlist}/{db_name}{parametrslist_python}'


if __name__ == '__main__':
    tests = ('jdbc:postgresql://server1.ru,server2.ru,' \
                'server3.ru:6432/sheme1',

                'jdbc:postgresql://server1.ru/sheme1',

                'jdbc:postgresql://server1.ru:6432/sheme1',

                'jdbc:postgresql://server1.ru,192.168.1.1,' \
                'server3.ru:6432/sheme1?&targetServerType=master&ssl=true',

                'jdbc:postgresql://http://server1.ru:6432,192.168.1.1:6432,' \
                'server3.ru:6432/sheme1?&targetServerType=master&ssl=true&sslmode=verify-full' \
                '&prepareThreshold=0',

                'jdbc:postgresql://http://app.server1.ru:6432,https://192.168.1.1:6432,' \
                'bd1.app.server3.ru:6432/sheme1?&targetServerType=master&ssl=true&sslmode=verify-full' \
                '&prepareThreshold=0',

                'postgresql://http://app.server1.ru:6432,https://192.168.1.1:6432,' \
                'server3.ru:6432/sheme1?&targetServerType=master&ssl=true&sslmode=verify-full' \
                '&prepareThreshold=0',
             )

    for test in tests:
        print(translate(test))
