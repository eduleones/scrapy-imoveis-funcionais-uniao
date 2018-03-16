# scrapy-imoveis-funcionais-uniao
*Scrapy dos Imóveis Funcionais da União. Pega o Endereço, Orgão Responsável e a Situação

## O que é necessário instalar?
### Python 3
#### Windows
##### Se você utiliza o sistema operacional windows, é  recomendado instalar o Python3 pelo [Anaconda](https://www.anaconda.com/download/) 

#### Ubuntu Linux e derivados
##### Necessário instalar as seguintes dependências:
     sudo apt-get install build-essential python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev gcc
     sudo apt-get install python3 python3-dev
     
#### Fedora Linux e derivado
     sudo yum install python3-devel gcc  # Fedora 26
     sudo dnf install python3-devel gcc  # Fedora 27
  
### Bibliotecas a serem utilizadas:

    pip install -r requirements.txt

## Executando
### Salvando os imóveis em um JSON

    scrapy crawl imoveis -o imoveis.json
    
### Salvando os imóveis no MongoDB Atlas
#### Configurações MongoDB, editar o arquivo vagas/setting.py 
    # Descomente a linha: 'imoveis_funcionais.pipelines.MongoPipeline': 300,
    
    ITEM_PIPELINES = {
    'imoveis_funcionais.pipelines.VagasPipeline': 300,
    'imoveis_funcionais.pipelines.MongoPipeline': 300,
    }
    
    # Adicione as configurações da sua conta MongoDB Atlas:
    
    # Configurações MongoDB Atlas - Exemplo:
    MONGO_URI = 'mongodb+srv://<user>:<password>@cluster0-hql3l.mongodb.net/test'
    MONGO_DATABASE = 'Vagas'
    
#### Executando e salvando no MongoDB Atlas
    scrapy crawl imoveis
