###############################################################################
##  Instituicao.: UNIVERSIDADE ESTACIO DE SA
##  Curso.......: CIENCIA DE DADOS E BIG DATA ANALYTICS
##  Disciplina..: LINGUAGEM PYTHON 2.7
###############################################################################
##  Aluno.......: HERSON PEREIRA CORDEIRO DE MELO (hersonpc@gmail.com)
##  Matricula...: 201908093609
##  Data........: 2020-04-26
##  GIT.........: https://github.com/hersonpc/simple-voting-system
###############################################################################

import sys
import math
import time
import pickle
import subprocess as sp


# variaveis globais
nome_arquivo = 'db.voting.bin'
regioes = []
candidatos = []
votos = []
voto = {}

def limpar_tela():
	tmp = sp.call('clear', shell=True)
	print("#"*80)
	print("SISTEMA DE VOTACAO PYTHON        POS-GRADUACAO DATA SCIENCE E BIG DATA ANALITYCS")
	print("2020-04-26" + " "*30 + " Autor: HERSON MELO (hersonpc@gmail.com)")
	print("#"*80 + "\n")


def obter_dados():
	global regioes, candidatos, votos

	regioes = []
	candidatos = []
	votos = []

	try:
		# leitura do arquivo binario
		arquivo = open(nome_arquivo, "rb")
		payload = pickle.load(arquivo)

		# atribuindo dados
		regioes = payload["REGIOES"]
		candidatos = payload["CANDIDATOS"]
		votos = payload["VOTOS"]

		# print(regioes)
		# print(candidatos)
		# print(votos)
	except:
		print('\n\n[ATENCAO] ERRO AO CARREGAR O ARQUIVO DE DADOS!!!')
	arquivo.close()


def gravar_dados():
	global regioes, candidatos, votos
	arquivo = open(nome_arquivo, "wb")
	payload = {
		"REGIOES": regioes,
		"CANDIDATOS": candidatos,
		"VOTOS": votos
	}
	pickle.dump(payload, arquivo)
	arquivo.close()


def seeder():
	global regioes, candidatos
	regioes = []
	candidatos = []

	# inicializando regioes...
	regioes.append({
		"ID": 1,
		"REGIAO": "GOIANIA"
	})
	regioes.append({
		"ID": 2,
		"REGIAO": "SAO PAULO"
	})
	regioes.append({
		"ID": 3,
		"REGIAO": "BELO HORIZONTE"
	})
	regioes.append({
		"ID": 4,
		"REGIAO": "CEARA"
	})
	regioes.append({
		"ID": 5,
		"REGIAO": "FLORIANOPOLIS"
	})

	# inicializando candidatos...
	candidatos.append({
		"COD_CANDIDATO": 11, 
		"NOME": "PAULO PEREIRA", 
		"CARGO": "PRESIDENTE"
	})
	candidatos.append({
		"COD_CANDIDATO": 23, 
		"NOME": "MARIA SCATELLY", 
		"CARGO": "PRESIDENTE"
	})
	candidatos.append({
		"COD_CANDIDATO": 30, 
		"NOME": "HERNANDES TYLENO", 
		"CARGO": "PRESIDENTE"
	})
	candidatos.append({
		"COD_CANDIDATO": 34, 
		"NOME": "SONIA MARINHO", 
		"CARGO": "PRESIDENTE"
	})

	# regisrar votos...
	guardar_voto(montar_voto(1, 11))
	guardar_voto(montar_voto(1, 11))
	guardar_voto(montar_voto(1, 23))
	guardar_voto(montar_voto(1, 23))
	guardar_voto(montar_voto(1, 23))
	guardar_voto(montar_voto(1, 30))
	guardar_voto(montar_voto(2, 30))
	guardar_voto(montar_voto(2, 34))
	guardar_voto(montar_voto(3, 11))
	guardar_voto(montar_voto(4, 11))

	gravar_dados()


def cadastrar_regioes():
	global regioes
	obter_dados()

	limpar_tela()
	print("Cadastro de regiao:\n")
	print("="*80)
	print("{:4s} {:40s}".format("NUM", "NOME DA REGIAO"))
	print("{:4s} {:40s}".format("-"*4, "-"*40))
	for item in regioes:
		print("{:4d} {:40s}".format(item["ID"], item["REGIAO"]))
	print("="*80)
	print("\nInforme os dados para cadastra a nova regiao")
	print("ou aperte [ENTER] para voltar para o menu:\n")
	try:
		id = raw_input("Codigo da regiao: ")
		if (id == ""):
			return
		id = int(id)
		for item in regioes:
			if(item["ID"] == id):
				raise NameError('Codigo ja existe!')
	except:
		raw_input("\n[ATENCAO] Codigo invalido ou ja utilizado!")
		cadastrar_regioes()
		return

	nome = raw_input("Nome da regiao: ")[:40]
	print("="*80)

	registro = {
		"ID": id, 
		"REGIAO": nome.upper()
	}
	regioes.append(registro)
	gravar_dados()

	raw_input("\n[ATENCAO] Cadastro realizado com sucesso!")


def cadastrar_candidatos():
	global candidatos
	obter_dados()

	limpar_tela()
	print("Cadastro de candidados:\n")
	print("="*80)
	print("{:4s} {:40s} {:20s}".format("NUM", "NOME DO CANDIDATO", "CARGO"))
	print("{:4s} {:40s} {:20s}".format("-"*4, "-"*40, "-"*20))
	for item in candidatos:
		print("{:4d} {:40s} {:20s}".format(item["COD_CANDIDATO"], item["NOME"], item["CARGO"]))
	print("="*80)
	print("\nInforme os dados para cadastra um novo candidato")
	print("ou aperte [ENTER] para voltar para o menu:\n")

	try:
		numero = raw_input("Numero do candidato: ")[:4]
		if (numero == ""):
			return
		numero = int(numero)
		for item in candidatos:
			if(item["COD_CANDIDATO"] == numero):
				raise NameError('O numero informado ja pertence a outro candidato!')
	except:
		raw_input("\n[ATENCAO] Numero invalido ou ja pertence a outro candidato!")
		cadastrar_candidatos()
		return


	nome = raw_input("Nome do candidado: ")[:40]
	cargo = raw_input("Cargo (ex. Presidente): ")[:20]
	print("="*80)

	registro = {
		"COD_CANDIDATO": numero, 
		"NOME": nome.upper(), 
		"CARGO": cargo.upper()
	}
	candidatos.append(registro)
	gravar_dados()

	raw_input("\n[ATENCAO] Cadastro realizado com sucesso!")


def selecionar_regiao():
	global regioes
	limpar_tela()
	print("Identificacao da regiao de votacao:\n")
	print("="*80)
	print("{:4s} {:40s}".format("NUM", "NOME DA REGIAO"))
	print("{:4s} {:40s}".format("-"*4, "-"*40))
	for item in regioes:
		print("{:4d} {:40s}".format(item["ID"], item["REGIAO"]))
	print("="*80)
	print("\nInforme o codigo da sua regiao de votacao")
	print("ou aperte [ENTER] para cancelar e voltar para o menu:\n")

	try:
		numero = raw_input("Codigo da sua regiao: ")[:4]
		if (numero == ""):
			return -2
		numero = int(numero)
		for item in regioes:
			if(item["ID"] == numero):
				return numero
	except:
		raw_input("\n[ATENCAO] Regiao selecionada e invalida!")
		selecionar_regiao()
		return -3
	
	return -1


def selecionar_candidato():
	global regioes
	limpar_tela()

	print("\nAgora, informe o numero de seu candidado escolhido:\n")

	print("="*80)
	print('  {:3s} {:40s} {:20s}'.format("NUM", "CANDIDATO", "CARGO"))
	print('  {:3s} {:40s} {:20s}'.format("-"*3, "-"*40, "-"*20))

	for candidato in candidatos:
    		print('  {:3d} {:40s} {:20s}'.format(
			candidato["COD_CANDIDATO"], 
			candidato["NOME"], 
			candidato["CARGO"]))

	print("="*80)
	print("Ou digite [ENTER] para cancelar e voltar para o menu.")

	try:
		candidato_escolhido = raw_input("\nDigite o numero do seu candidado: ")[:4]
		if (candidato_escolhido == ""):
			return -2
		candidato_escolhido = int(candidato_escolhido)
		for candidato in candidatos:
			if(candidato["COD_CANDIDATO"] == candidato_escolhido):
				voto.update({ "ESCOLHIDO": candidato })
				return candidato_escolhido
	except:
		raw_input("\n[ATENCAO] O codigo do candidato selecionado e invalido!")
		selecionar_candidato()
		return -3
	
	return -1


def print_center(texto, tam_tela = 80):
	tam = len(texto)
	espacos_a_esquerda = int(math.floor((tam_tela - tam) / 2))
	print(" "*espacos_a_esquerda + texto)


def guardar_voto(registro):
	global votos
	confirmar = 0

	if( ("CREATED_AT" not in registro) or ("LOCAL" not in registro) or ("ESCOLHIDO" not in registro) ):
		raw_input('\n[ATENCAO] Este voto nao pode ser armazenado!')
		return False
	
	votos.append({
		"CREATED_AT": time.time(),
		"VOTO": registro
	})
	return True


def montar_voto(regiao_id, candidato_id):
	global votos, regioes, candidatos
	payload = {}

	for regiao in regioes:
		if(regiao["ID"] == regiao_id):
			payload.update({ "LOCAL": regiao })

	for candidato in candidatos:
		if(candidato["COD_CANDIDATO"] == candidato_id):
			payload.update({ "ESCOLHIDO": candidato })

	payload.update({ "CREATED_AT": 0 })

	return payload


def confirmar_voto(registro):
	global voto
	confirmar = 0

	if( ("CREATED_AT" not in registro) or ("LOCAL" not in registro) or ("ESCOLHIDO" not in registro) ):
		raw_input('\n[ATENCAO] Este voto nao pode ser confirmado!')
		return
	
	limpar_tela()
	print_center("="*33)
	print_center("ATENCAO")
	print_center("CONFIRMACAO DE VOTO")
	print_center("="*33)
                                                            

	print("\nVoce escolheu o candidato:\n")
	print("\t{:10s} {:d}".format("Num:", voto["ESCOLHIDO"]["COD_CANDIDATO"]))
	print("\t{:10s} {:40s}".format("Nome:", voto["ESCOLHIDO"]["NOME"]))
	print("\t{:10s} {:20s}".format("Cargo:", voto["ESCOLHIDO"]["CARGO"]))
	print("\n"+"="*80)
	
	confirmar = raw_input("Desja confirmar seu voto? [S/N]: ")
	if((confirmar == "s") or (confirmar == "S")):
		guardar_voto(registro)
		gravar_dados()
		
		limpar_tela()
		print_center("="*33)
		print_center("ATENCAO")
		print_center("VOTO REGISTRADO COM SUCESSO!")
		print_center("="*33)
		raw_input('\n\n[ATENCAO] Seu voto foi registrado com sucesso!')
	else:
		raw_input('\n[ATENCAO] Voce nao confirmou seu voto, por isto este voto nao sera registrado!')

	if(confirmar == 0):
		raw_input('\n[ATENCAO] Opcao invalida, nenhum voto foi registrado!')


def votar():
	global candidatos, voto
	limpar_tela()
	obter_dados()

	# limpa o voto
	voto = {}

	regiao_id = selecionar_regiao()
	if(regiao_id <= 0):
		raw_input("\n[ATENCAO] Regiao informada e invalida, esta votacao foi cancelada.")
		return
	
	candidato_id = selecionar_candidato()
	if(candidato_id <= 0):
		raw_input("\n[ATENCAO] O candidato informado e invalido, esta votacao foi cancelada.")
		return
	
	registro = montar_voto(regiao_id, candidato_id)
	confirmar_voto(registro)

	return


def apuracao(tipo = "CANDIDATO"):
	global regioes, candidatos, votos
	limpar_tela()
	obter_dados()

	apuracao_regiao = {}
	for regiao in regioes:
		estrutura = {}
		for candidato in candidatos:
			estrutura[candidato["NOME"]] = 0
		apuracao_regiao[regiao["REGIAO"]] = estrutura

	print("Resultado da apuracao dos votos realizados:\n")
	print("="*80)
	if(tipo == "CANDIDATO"):
		print_center("APURACAO POR CANDIDATO")
		print(" "*15+'{:3s} {:40s} {:5s}'.format("NUM", "CANDIDATO", "VOTOS"))
		print(" "*15+'{:3s} {:40s} {:5s}'.format("-"*3, "-"*40, "-"*5))
		
		for candidato in candidatos:
			total_votos = 0
			for voto in votos:
				if(voto["VOTO"]["ESCOLHIDO"]["COD_CANDIDATO"] == candidato["COD_CANDIDATO"]):
					total_votos += 1

			print(" "*15+'{:3d} {:40s} {:5d}'.format(
				candidato["COD_CANDIDATO"], 
				candidato["NOME"], 
				total_votos))
	elif(tipo == "REGIAO"):
		print_center("APURACAO POR REGIAO")
		print(" "*5+'{:20s} {:40s} {:5s}'.format("REGIAO", "CANDIDATO", "VOTOS"))
		print(" "*5+'{:20s} {:40s} {:5s}'.format("-"*20, "-"*40, "-"*5))
		for candidato in candidatos:
			for voto in votos:
				if(voto["VOTO"]["ESCOLHIDO"]["COD_CANDIDATO"] == candidato["COD_CANDIDATO"]):
					apuracao_regiao[voto["VOTO"]["LOCAL"]["REGIAO"]][candidato["NOME"]] += 1

		for item_regiao in apuracao_regiao:
			# print(item_regiao)
			for item_candidato in apuracao_regiao[item_regiao]:
				# print(item_candidato)
				if(apuracao_regiao[item_regiao][item_candidato] > 0):
					print(" "*5+'{:20s} {:40s} {:5d}'.format(
						item_regiao, 
						item_candidato, 
						apuracao_regiao[item_regiao][item_candidato]))

	print("="*80)

	raw_input('\n\nPresione [ENTER] para voltar ao menu. ')


def menu():
	limpar_tela()
	print("Selecione uma das opcoes listadas abaixo e informe o codigo:\n")
	print("="*80)
	opcoes = [
		{ "id": 1, "desc": "Votar"},
		{ "id": 2, "desc": "Exibir apuracao dos votos por candidato"},
		{ "id": 3, "desc": "Exibir apuracao dos votos por regiao"},
		{ "id": 7, "desc": "Cadastrar novos regioes"},
		{ "id": 8, "desc": "Cadastrar novos candidatos"},
		{ "id": 9, "desc": "Sair do aplicativo"},
	]
	for op in opcoes:
    		print("  [{:1d}] - {:20s}".format(op["id"], op["desc"].upper()))
	print("="*80)

	try:
		opcao = int(raw_input("Opcao: ")[:1])
	except:
		menu()

	if(opcao == 9):
		limpar_tela()
		print("\nAplicativo finalizado!\n\n".upper())
		sys.exit(1)
	elif(opcao == 1):
		votar()
	elif(opcao == 2):
		apuracao()
	elif(opcao == 3):
		apuracao("REGIAO")
	elif(opcao == 7):
		cadastrar_regioes()
	elif(opcao == 8):
		cadastrar_candidatos()
	menu()


# Inicio da aplicacao
# seeder() # se disparado permite preencher com dados de teste
obter_dados()
menu()
