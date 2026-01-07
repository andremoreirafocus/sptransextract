Este projeto faz download de informações da SPTRANS:
- arquivos GTFS do portal do desenvolvedor
- posição dos ônibus de SP usando a API da SPTRANS
- credenciais necessárias se encontram no arquivo .env do projeto usando as seguintes variáveis:
BASE_URL = "https://api.olhovivo.sptrans.com.br/v2.1"
TOKEN =  <insira o seu token>
INTERVALO = 120  # 2 minutos em segundos
LOGIN = <insira seu login>
PASSWORD = <insira sua senha>

Para executar: 
pip install -r requirements.txt
python ./main.py
