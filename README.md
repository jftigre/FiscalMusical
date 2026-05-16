#  Fiscal Musical 

O crítico de música mais ácido, impaciente e sarcástico da internet, alimentado por Inteligência Artificial.

外 **[Acesse o projeto online aqui!](https://fiscalmusical.onrender.com/)** 外

> ⚠️ **Nota Importante de Demonstração (Ambiente de Estudos):** > Devido às políticas restritas de segurança da API do Spotify, esta aplicação encontra-se em *Modo de Desenvolvimento*. O Spotify atualmente limita o acesso de produção e cotas públicas apenas a organizações empresariais registradas. Portanto, este link funciona como um **projeto de portfólio de estudos**, sendo necessário o cadastro prévio do e-mail do usuário no painel de desenvolvedor para realizar a análise em tempo real. Para visualizar o projeto em ação sem restrições, confira a demonstração em vídeo logo abaixo!

---

##  Demonstração do Fiscal Musical 

https://github.com/user-attachments/assets/5e0d898b-b888-4c22-8c1e-426037ee8d72

---

##  Sobre o Projeto

O **Fiscal Musical** é uma aplicação web dinâmica que utiliza IA para analisar o histórico recente de reprodução dos usuários com base em dados reais consumidos diretamente da API do Spotify. 

Diferente das retrospectivas tradicionais e amigáveis de fim de ano, o Fiscal assume o papel de um "sommelier de indie" rabugento, misturado com um "tiozão do rock" inflamado e um usuário do Twitter munido de puro deboche. O resultado é um laudo pericial honesto (até demais) formatado como um autêntico cupom fiscal de mercado.

---

##  Funcionalidades

- **Autenticação Segura com Spotify (OAuth):** Login direto e seguro para ler os top 5 artistas e top 5 músicas do usuário em curto prazo.
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
