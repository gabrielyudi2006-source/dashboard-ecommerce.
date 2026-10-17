# Dashboard de E-commerce com Dash

Aplicação interativa desenvolvida com Python, Pandas, Plotly e Dash, usando o arquivo `ecommerce_estatistica.csv`.

## Funcionalidades
- Filtro de produtos por marca
- Indicadores de preço e nota média
- Distribuição de preços, notas e descontos
- Marcas com mais produtos
- Gráfico de dispersão entre preço e nota

## Como executar

```bash
pip install -r requirements.txt
python app.py
```

Abra o endereço local exibido no terminal (normalmente http://127.0.0.1:8050/).

## Entrega
Envie o link do repositório GitHub contendo `app.py`, `requirements.txt`, `README.md` e `ecommerce_estatistica.csv`.

**Observação:** o GitHub hospeda o código, mas não executa o servidor Dash automaticamente. Para disponibilizar um link público do painel, é necessário hospedar a aplicação em um serviço de deploy, como Render, usando `gunicorn app:server`.
