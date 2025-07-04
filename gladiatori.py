name: Gladiatore del Giorno

on:
  schedule:
    - cron: '0 20 * * *'  # Ogni giorno alle 22:00 ora italiana (20:00 UTC)
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Clona il repo
        uses: actions/checkout@v3

      - name: Installa Python e dipendenze
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Installa librerie necessarie
        run: |
          pip install pandas pillow

      - name: Esegui lo script
        run: python gladiatori.py

      - name: Salva risultati
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "Aggiornamento classifica giornaliera"
