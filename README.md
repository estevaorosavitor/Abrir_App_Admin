# Executar programa com credenciais de administrador.

Solução em python desenvolvida para poder abrir programas com credenciais de administrador utilizando usuários que não tem credencial, sem precisar passar a senha ao usuário final.

A ideia surgiu da necessidade de alguns softwares precisarem de permissão de administrador para executar algumas funções, é o exemplo do programa MGV7 da Toledo do Brasil.

Para funcionar perfeitamente, é necessário ter um usuário local na máquina com permissão de administrador, e obviamente apenas os técnicos saberão a senha.
Será usado esse user dentro do aplciativo em python.

São 3 váriaveis que precisam ser preenchidas:
- `user` => nome de usuário do administrador local;
- `pasword` => senha do usuário administrador local;
- `program` => diretório do .exe que deseja executar.

1) Instale a biblioteca PyInstaller: `pip install pyinstaller`
2) Monte seu arquivo executavel apartir do arquivo .py: `pyinstaller --onefile main.py`
3) Distribua para seus usuários o arquivo executável.
