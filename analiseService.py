import pandas as pd
import matplotlib.pyplot as plt

# Lendo o CSV
arquivo = pd.read_csv("covid.csv")

# Mostrando as 5 primeiras linhas
print("🔹 Primeiras linhas do dataset:")
print(arquivo.head())

# Informações gerais
print("\n🔹 Informações gerais do dataset:")
print(arquivo.info())

# Estatísticas descritivas
print("\n🔹 Estatísticas descritivas:")
print(arquivo[['confirmed', 'deaths', 'confirmed_per_100k_inhabitants', 'death_rate']].describe())

# Total de casos confirmados e mortes no Brasil
total_confirmados = arquivo['confirmed'].sum()
total_mortes = arquivo['deaths'].sum()
print(f"\n📊 Total de casos confirmados: {total_confirmados:,}")
print(f"💀 Total de mortes: {total_mortes:,}")

# 🔹 Análise por estado
casos_por_estado = arquivo.groupby("state")['confirmed'].sum().sort_values(ascending=False)
mortes_por_estado = arquivo.groupby("state")['deaths'].sum().sort_values(ascending=False)

print("\n🔹 Casos confirmados por estado:")
print(casos_por_estado)

print("\n🔹 Mortes por estado:")
print(mortes_por_estado)

# Gráfico de casos confirmados por estado
plt.figure(figsize=(12,6))
casos_por_estado.plot(kind='bar', color='skyblue')
plt.title("Casos confirmados por estado")
plt.ylabel("Número de casos")
plt.xlabel("Estado")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("casos_por_estado.png")
plt.close()

# Gráfico de taxa de mortalidade por estado
taxa_mortalidade_estado = (mortes_por_estado / casos_por_estado).sort_values(ascending=False)

plt.figure(figsize=(12,6))
taxa_mortalidade_estado.plot(kind='bar', color='salmon')
plt.title("Taxa de mortalidade por estado")
plt.ylabel("Taxa de mortalidade")
plt.xlabel("Estado")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("taxa_mortalidade_por_estado.png")
plt.close()

print("\n✅ Gráficos salvos como 'casos_por_estado.png' e 'taxa_mortalidade_por_estado.png'")
