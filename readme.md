# bigtech-lang-stats

Projeto de Engenharia de Dados com o objetivo de identificar as linguagens de programação mais utilizadas pelas maiores empresas de tecnologia no GitHub.

## 🚀 Objetivo

Construir um pipeline de dados para extrair, transformar e analisar dados públicos do GitHub, a fim de descobrir quais linguagens de programação são mais utilizadas por empresas como Google, Microsoft, Amazon, Meta, Apple, entre outras.

## 🔧 Tecnologias Utilizadas

- Python
- GitHub API
- Pandas
- PostgreSQL
- Jupyter Notebook (para análises exploratórias e visualização)

## 🛠️ Estrutura do Projeto

```
bigtech-lang-stats/
├── notebooks/                # Análises e visualizações
├── src/                      # Scripts de extração, transformação e carga
│   ├── extract/
│   ├── transform/
│   └── load/
├── data/                     # Dados brutos e processados
├── requirements.txt
└── README.md
```

## 📊 Etapas do Pipeline

1. **Extração**  
   - Coleta de dados dos repositórios públicos de empresas selecionadas via GitHub API.

2. **Transformação**  
   - Limpeza dos dados, padronização e categorização das linguagens.

3. **Armazenamento**  
   - Dados armazenados em banco de dados relacional para consultas e análises.

4. **Análise**  
   - Geração de relatórios com estatísticas e visualizações sobre as linguagens mais utilizadas.

## 🧠 Empresas Alvo

- Google
- Microsoft
- Amazon
- Meta (Facebook)
- Apple
- Netflix
- Twitter (X)
- Uber
- Airbnb

## 📈 Resultados Esperados

- Ranking das linguagens mais utilizadas por cada empresa.
- Comparação entre stacks de diferentes big techs.
- Identificação de tendências tecnológicas no ecossistema das grandes empresas.

## 📌 Como Contribuir

1. Fork este repositório
2. Crie uma branch com sua feature: `git checkout -b minha-feature`
3. Commit suas alterações: `git commit -m 'Minha nova feature'`
4. Push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a licença MIT.