# Model_interoperabilidade
✅ Descrição Geral do Projeto Este sistema:  Utiliza KivyMD para a interface gráfica.  Usa SQLite para armazenar os dados localmente.  Gera um PDF com os dados mais recentes.  Exporta dois arquivos JSON: um técnico e um no padrão FHIR (interoperabilidade em saúde).

# 🩺 Formulário APH - Sistema com Interoperabilidade FHIR

Este é um sistema simples desenvolvido em **Python** com **KivyMD**, voltado para o preenchimento de formulários de atendimento pré-hospitalar (APH), com **interface gráfica**, **armazenamento local em SQLite**, **geração de PDF** e **exportação de dados em JSON** no padrão técnico e **FHIR** (padrão internacional de interoperabilidade em saúde).

---

## ✨ Funcionalidades

- 📋 Interface gráfica para entrada de dados (nome, CPF)
- 💾 Armazenamento local dos dados em banco SQLite
- 📄 Geração automática de PDF com os dados salvos
- 🧾 Geração de JSON técnico com dados estruturados
- 🌐 Geração de JSON no padrão HL7 FHIR (recurso `Patient`)

---

## 🖼️ Interface Gráfica

> Interface desenvolvida com [KivyMD](https://kivymd.readthedocs.io/)

![Exemplo da Interface](screenshot.png) <!-- Opcional: substitua por uma imagem real -->

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- KivyMD
- SQLite3
- fpdf2
- json
- regex (re)

---

## 🏗️ Estrutura do Projeto

📁 projeto/
├── main.py # Arquivo principal com a lógica do app
├── interface.kv # Layout da interface gráfica
├── dados.db # Banco de dados SQLite
├── formulario_aph.pdf # PDF gerado com os dados
├── json_tecnico.json # Dados exportados em formato técnico
├── json_fhir.json # Dados exportados no padrão FHIR


---

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/formulario-aph.git
cd formulario-aph

Observações adicionais.
Antes de rodar, precisa ter as dependências instaladas.

pip install kivymd fpdf

📥 Pré-requisitos
Python 3.7 ou superior

Pip atualizado

Sistema compatível com GUI (Windows, Linux ou Android via Buildozer)

🛠️ Futuras Melhorias (opcional)
Integração com outros recursos FHIR (Observation, Encounter)

Geração de QR Code com os dados

Versão Android com Buildozer

Integração com serviços de saúde (ex: RNDS)

👨‍💻 Autor
José Gonçalves Barcellos Junior

Mestrando(a) em Informática em Saúde | UFSC

Leia a Licneça de uso. 

