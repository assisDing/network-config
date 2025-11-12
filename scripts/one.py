
users = ['joana', 'maria','guilhermina','zorobabel','guilhermina','guilhermina']
usuariosConfirmados = []

while users:
    confirmacaoUsuarios = users.pop()
    usuariosConfirmados.append(confirmacaoUsuarios)
    

print(f"Os seguintes usuarios foram confirmados:")

for impressao in usuariosConfirmados:
  
    print(impressao)

print("\n")
while 'guilhermina' in usuariosConfirmados:
    usuariosConfirmados.remove('guilhermina')
    

for impressaodois in usuariosConfirmados:
    print (impressaodois)
