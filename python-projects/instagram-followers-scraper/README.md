# Buscador do númmero de seguidores - Instagram

# Introdução
Este script usa Selenium e o ChromeDriver para extrair o número de seguidores de uma conta do Instagram especificada. Ele salva o número de seguidores em um arquivo de texto chamado "followers.txt" no mesmo diretório em que o script está localizado.

# Como usar:
É necessário ter o Python 3 instalado -> https://www.python.org

1) Instale o Python em seu sistema, se ainda não estiver instalado.
Renomeie .env.example para .env e adicione o nome de usuário do Instagram no arquivo de exemplo.
2) Instale os pacotes necessários usando o comando pip install -r requirements.txt.
3) Abra o prompt de comando ou terminal e navegue até o diretório onde o script está salvo. Execute o script usando o comando python run.py.
4) O script procurará por uma variável de ambiente chamada USERNAME e usará seu valor como o nome da conta.
5) Aguarde o término da execução do script. Assim que terminar, o número total de seguidores para a conta do Instagram especificada será salvo em um arquivo chamado followers.txt no mesmo diretório em que o script está localizado.

Opcionalmente, se você deseja extrair os seguidores de uma conta específica do Instagram usando um argumento, pode passar o nome da conta como argumento de linha de comando. Por exemplo, python run.py nome_da_conta.

Não esquece de seguir @minhavagatech em todas as redes.