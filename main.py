from kivymd.app import MDApp
from kivy.lang import Builder
import sqlite3
from datetime import datetime
from fpdf import FPDF
import json
import re

class MainApp(MDApp):

    def build(self):
        print("Carregando interface.kv...")
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.criar_banco()
        return Builder.load_file("interface.kv")  # <-- RETORNE O LAYOUT DIRETO

    def criar_banco(self):
        conn = sqlite3.connect("dados.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS formulario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                data_cadastro TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def salvar_dados(self):
        nome = self.root.ids.nome_field.text
        cpf = self.root.ids.cpf_field.text
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect("dados.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO formulario (nome, cpf, data_cadastro) VALUES (?, ?, ?)", (nome, cpf, data))
        conn.commit()
        conn.close()

        print("Dados salvos:", nome, cpf)
        self.root.ids.nome_field.text = ""
        self.root.ids.cpf_field.text = ""

    def gerar_pdf(self):
        conn = sqlite3.connect("dados.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome, cpf, data_cadastro FROM formulario ORDER BY id DESC LIMIT 1")
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            nome, cpf, data_cadastro = resultado
            cpf_formatado = self.formatar_cpf(cpf)

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="DADOS DO PACIENTE", ln=True, align="C")
            pdf.cell(200, 10, txt=f"Nome: {nome}", ln=True)
            pdf.cell(200, 10, txt=f"CPF: {cpf_formatado}", ln=True)
            pdf.cell(200, 10, txt=f"Data de Cadastro: {data_cadastro}", ln=True)
            pdf.output("formulario_aph.pdf")

            self.gerar_json_tecnico(nome, cpf_formatado, data_cadastro)
            self.gerar_json_fhir(nome, cpf_formatado)

            print("PDF e JSONs gerados com sucesso.")

    def gerar_json_tecnico(self, nome, cpf, data):
        dados = {
            "formulario": "APH_v1",
            "nome": nome,
            "cpf": cpf,
            "data": data
        }
        with open("json_tecnico.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def gerar_json_fhir(self, nome, cpf):
        fhir = {
            "resourceType": "Patient",
            "name": [{"text": nome}],
            "identifier": [{"system": "http://gov.br/cpf", "value": cpf}]
        }
        with open("json_fhir.json", "w", encoding="utf-8") as f:
            json.dump(fhir, f, indent=4, ensure_ascii=False)

    def formatar_cpf(self, cpf):
        """Remove tudo que não é número e aplica a máscara xxx.xxx.xxx-xx"""
        numeros = re.sub(r'\D', '', cpf)
        if len(numeros) == 11:
            return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
        return cpf  # Retorna como está se não tiver 11 dígitos

MainApp().run()


