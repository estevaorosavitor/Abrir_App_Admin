# Executar programa com credenciais de admin.

Solução em python desenvolvida para poder abrir programas com credenciais de administrador com usuários que não tem permissão, sem precisar passar a senha ao usuário final.

A ideia veio da necessidade de alguns softwares precisarem de permissão de administrador para executar algumas funções, é o exemplo do programa MGV7 da Toledo do Brasil.

Para funcionar perfeitamente, é necessário ter um usuário local na máquina com permissão de administrador, e obviamente apenas os técnicos saberão a senha.
Será usado esse user dentro do aplciativo em python.

São 3 váriaveis que precisam ser preenchidas:
- `user` => nome de usuário do administrador local;
- `pasword` => senha do usuário administrador local;
- `program` => diretório do .exe que deseja executar.

  
