#  Fiscal Musical 

O crítico de música mais ácido, impaciente e sarcástico da internet, alimentado por Inteligência Artificial.

---

![Demonstração do Fiscal Musical] <img width="1280" height="720" alt="Fiscal-Musical" src="https://github.com/user-attachments/assets/8f3efe5d-0d85-4e17-b117-b77ed22834d6" />


##  Sobre o Projeto

O **Fiscal Musical** é uma aplicação web dinâmica que utiliza IA para analisar o histórico recente de reprodução dos usuários com base em dados reais consumidos diretamente da API do Spotify. 

Diferente das retrospectivas tradicionais e amigáveis de fim de ano, o Fiscal assume o papel de um sommelier rabugento. O resultado é um laudo pericial honesto (até demais) formatado como um autêntico cupom fiscal de mercado.

---

##  Funcionalidades

- **Autenticação Segura com Spotify (OAuth):** Login direto e seguro.
- **Análise Pericial com IA:** Integração com o modelo `gemini-2.5-flash` através da biblioteca `google-genai` para processamento de linguagem natural e geração de um texto altamente personalizado e sarcástico.
- **Identidade Visual de Recibo (Design System):** Layout responsivo simulando um cupom fiscal clássico, otimizado para leitura tanto em desktops quanto em dispositivos móveis.
- **Mecanismo Antispam (UX):** Botão interativo com script de *loading* que desabilita novos cliques e exibe um aviso de "Análise em andamento", evitando requisições duplicadas e protegendo o consumo de tokens das APIs.

---

##  Tecnologias Utilizadas

| Categoria | Tecnologia |
| :--- | :--- |
| **Backend** | Python 3.14+ / Flask |
| **Inteligência Artificial** | Google GenAI (Gemini 2.5 Flash) |
| **Integração de Áudio** | Spotipy (Spotify Web API) |
| **Frontend** | HTML5 / CSS3 (Design Responsivo & Semântico) |
| **Servidor de Produção** | Gunicorn |
| **Hospedagem / Nuvem** | Render |

---
