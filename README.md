# ⚡ Calculadora de Consumo de Energia

Este programa foi desenvolvido para auxiliar no cálculo do consumo mensal de eletrodomésticos, convertendo a potência em Watts para quilowatts-hora (kWh).

![Python](https://img.shields.io/badge/Linguagem-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

## 📖 Sobre o Projeto
O sistema recebe dados de potência e tempo de uso para fornecer uma estimativa do impacto de um aparelho na conta de luz mensal. Foi criado como parte da disciplina de **Desenvolvimento de Sistemas I**.
## 📐 Fórmula Aplicada
Para obter o resultado em kWh, o código utiliza a seguinte lógica:
- **Consumo (kWh)** = (Potência (W) * Horas de uso * 30 dias) / 1000

## 🚀 Como Executar
1. Certifique-se de ter o **Python** instalado.
2. Baixe o arquivo principal do repositório.
3. No terminal ou CMD, execute:
```bash
python consumo_energia.py
