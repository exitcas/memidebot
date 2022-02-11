# Code from https://repl.it/@TheDrone7/discordpy-rewrite#keep_alive.py
from flask import Flask
from threading import Thread
app = Flask("")

@app.route('/')
def main():
  return ":D"

def run():
  app.run(host="0.0.0.0", port=2984)

def keep_alive():
  server = Thread(target=run)
  server.start()