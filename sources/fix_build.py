import os
import shutil
import subprocess

def run_make():
    # Corrigir o problema com 'ls: cannot access 'documentation/*.py': No such file or directory'
    # Certifique-se de que o diretório documentation existe antes de listar arquivos dentro dele
    if os.path.exists('documentation'):
        os.system('ls documentation/*.py')

    # Remover o diretório 'fonts' de forma segura
    if os.path.exists('fonts'):
        shutil.rmtree('fonts')

    # Executar os comandos do Makefile
    subprocess.run(['make', 'build'])

def fix_otfautohint():
    # Corrigir erros otfautohint
    try:
        subprocess.run(['otfautohint', '../fonts/otf/Zoika_display.otf'])
        # Se não houver exceção, toque no arquivo de marcação
        open('../fonts/otf/Zoikafont-Bold.otf.autohintstamp', 'a').close()
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar otfautohint: {e}")

def fix_gftools_autohint():
    # Corrigir erros gftools-autohint
    try:
        subprocess.run(['gftools-autohint', '../fonts/ttf/Zoika_display.ttf'])
        # Se não houver exceção, toque no arquivo de marcação
        open('../fonts/ttf/Zoikafont-Bold.ttf.autohintstamp', 'a').close()
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar gftools-autohint: {e}")

def main():
    # Executar todas as correções
    run_make()
    fix_otfautohint()
    fix_gftools_autohint()

if __name__ == "__main__":
    main()
