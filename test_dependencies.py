#!/usr/bin/env python3
"""
Script de teste para verificar dependências antes do deploy no Streamlit Cloud
"""

import sys
import importlib

def test_imports():
    """Testa se todas as dependências necessárias estão disponíveis"""
    
    dependencies = [
        'streamlit',
        'pandas', 
        'requests',
        'datetime',
        'calendar',
        'numpy',
        'plotly.express',
        'plotly.graph_objects'
    ]
    
    print("🧪 Testando importações necessárias...")
    print("=" * 50)
    
    failed = []
    success = []
    
    for dep in dependencies:
        try:
            importlib.import_module(dep)
            print(f"✅ {dep}")
            success.append(dep)
        except ImportError as e:
            print(f"❌ {dep} - Erro: {e}")
            failed.append(dep)
    
    print("=" * 50)
    print(f"✅ Sucessos: {len(success)}")
    print(f"❌ Falhas: {len(failed)}")
    
    if failed:
        print("\n🚨 Dependências faltando:")
        for dep in failed:
            print(f"   pip install {dep}")
        return False
    else:
        print("\n🎉 Todas as dependências estão disponíveis!")
        return True

def test_streamlit_compatibility():
    """Testa compatibilidade com Streamlit"""
    try:
        import streamlit as st
        print(f"\n📋 Streamlit versão: {st.__version__}")
        
        # Testar se as funções principais estão disponíveis
        test_functions = [
            'st.markdown',
            'st.error', 
            'st.info',
            'st.columns',
            'st.container'
        ]
        
        print("\n🔧 Testando funções do Streamlit:")
        for func_name in test_functions:
            try:
                func = eval(func_name)
                print(f"✅ {func_name}")
            except:
                print(f"❌ {func_name}")
        
        return True
    except Exception as e:
        print(f"❌ Erro no Streamlit: {e}")
        return False

def main():
    print("🐍 Teste de Compatibilidade - Dashboard Financeiro")
    print("=" * 60)
    
    # Testar Python version
    python_version = sys.version_info
    print(f"🐍 Python: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 8):
        print("⚠️  Aviso: Python < 3.8 pode ter problemas de compatibilidade")
    
    # Testar imports
    imports_ok = test_imports()
    
    # Testar Streamlit
    streamlit_ok = test_streamlit_compatibility()
    
    print("\n" + "=" * 60)
    if imports_ok and streamlit_ok:
        print("🎉 SUCESSO: Pronto para deploy no Streamlit Cloud!")
        return 0
    else:
        print("🚨 FALHA: Corrija os problemas antes do deploy")
        return 1

if __name__ == "__main__":
    exit(main())
