def in_autotests_we_trust(a, b):
    if a == b:
        print('Passou nesse primeiro teste')
    else:
        print('Falhou nesse segundo teste')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)