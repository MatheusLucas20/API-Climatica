# 🌤️ Consumo de API Climática com Python (`requests`)

Este projeto é uma aplicação em Python desenvolvida para consumir dados em tempo real da API global **OpenWeatherMap**. O objetivo principal foi entender na prática como realizar requisições HTTP, manipular respostas no formato JSON e estruturar códigos modularizados integrando serviços externos de backend.

---

## 🧠 Conceitos de Engenharia de Software Aplicados

Para ir além de um script básico, estruturei o código aplicando boas práticas de desenvolvimento de software:

* **Integração com APIs REST:** Utilização da biblioteca `requests` para realizar requisições do tipo `GET` em endpoints externos.
* **Manipulação de JSON:** Tratamento de dicionários e listas aninhadas complexas retornadas pela API para extrair dados específicos (`main.temp` e `weather[0].main`).
* **Tratamento de Performance (`timeout`):** Configuração de `timeout=5` na requisição para evitar que o terminal trave indefinidamente caso o servidor externo sofra uma queda ou instabilidade.
* **Modularização Dinâmica:** Separação das responsabilidades em funções limpas:
  * `get_weather_API(city)`: Cuida exclusivamente da comunicação física com a API.
  * `get_weather_City(city)`: Trata os dados de temperatura e realiza o cálculo matemático de conversão de Kelvin para Celsius com arredondamento.
  * `get_weather_main(city)`: Extrai o estado atual do clima (Ex: Clear, Clouds, Rain).
* **Boas Práticas de Organização:** Arquitetura limpa utilizando a validação de escopo padrão do mercado (`if __name__ == '__main__':`).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Biblioteca `requests`** (Instalada via `pip install requests`)
* **API OpenWeatherMap** (Serviço de dados meteorológicos globais)

---

## 💻 Como Executar o Projeto

### 1. Pré-requisitos
É necessário instalar a biblioteca `requests` antes de rodar o script:
```bash
pip install requests
