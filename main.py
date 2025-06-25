def in_autotests_we_trust(a, b):
    if a == b:
        print('Passou nesse teste')
    else:
        print('Falhou nesse teste')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)