import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# URLs para abrir
urls = [
    "https://pt.wix.com/",
    "https://www.diamondbigger.com/",
    "https://www.pipefy.com/pt-br/",
    "https://supabase.com/",
    "https://stripe.com/en-br",
]

# Abre cada URL
for url in urls:
    navegador.execute_script("window.open('', '_blank');")
    navegador.switch_to.window(navegador.window_handles[-1])
    navegador.get(url)
    time.sleep(0.5)

# Mantém o navegador aberto
input("Pressione Enter para encerrar o programa...")
