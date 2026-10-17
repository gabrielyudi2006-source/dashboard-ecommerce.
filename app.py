import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Carrega os dados do projeto.
df = pd.read_csv('ecommerce_estatistica.csv')
for coluna in ['Preço', 'Nota', 'Desconto', 'N_Avaliações']:
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

app = Dash(__name__)
server = app.server
marcas = sorted(df['Marca'].dropna().astype(str).unique())
app.layout = html.Div([
    html.H1('Dashboard de E-commerce', style={'textAlign': 'center'}),
    html.P('Análise interativa de produtos, preços, avaliações e descontos.', style={'textAlign': 'center'}),
    html.Label('Filtrar por marca:'),
    dcc.Dropdown(id='marca', options=[{'label': 'Todas as marcas', 'value': '__todas__'}] + [{'label': m, 'value': m} for m in marcas], value='__todas__', clearable=False),
    html.Div(id='indicadores', style={'margin': '20px 0', 'fontSize': '18px'}),
    dcc.Graph(id='grafico-precos'),
    dcc.Graph(id='grafico-notas'),
    dcc.Graph(id='grafico-marcas'),
    dcc.Graph(id='grafico-descontos'),
    dcc.Graph(id='grafico-dispersao'),
], style={'maxWidth': '1100px', 'margin': 'auto', 'padding': '24px', 'fontFamily': 'Arial, sans-serif'})

@app.callback(
    Output('indicadores', 'children'),
    Output('grafico-precos', 'figure'),
    Output('grafico-notas', 'figure'),
    Output('grafico-marcas', 'figure'),
    Output('grafico-descontos', 'figure'),
    Output('grafico-dispersao', 'figure'),
    Input('marca', 'value'),
)
def atualizar(marca):
    dados = df if marca == '__todas__' else df[df['Marca'].astype(str) == marca]
    indicadores = f'Produtos: {len(dados)} | Preço médio: R$ {dados["Preço"].mean():.2f} | Nota média: {dados["Nota"].mean():.2f}'
    precos = px.histogram(dados, x='Preço', nbins=25, title='Distribuição dos preços')
    notas = px.histogram(dados, x='Nota', nbins=15, title='Distribuição das notas')
    contagem = dados['Marca'].fillna('Não informada').value_counts().head(10).reset_index()
    contagem.columns = ['Marca', 'Quantidade']
    grafico_marcas = px.bar(contagem, x='Marca', y='Quantidade', title='10 marcas com mais produtos')
    descontos = px.histogram(dados, x='Desconto', nbins=20, title='Distribuição dos descontos')
    dispersao = px.scatter(dados, x='Preço', y='Nota', hover_data=['Título'], title='Preço x Nota dos produtos')
    return indicadores, precos, notas, grafico_marcas, descontos, dispersao

if __name__ == '__main__':
    app.run(debug=True)
