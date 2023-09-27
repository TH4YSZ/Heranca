import os

def op_invalida():
    print("Opção inválida.")
    os.system("pause")
    os.system("cls")
    
class ProduçãoAúdioVisual:
    def definição (self):
        print ("Uma produção audiovisual é a criação de conteúdo que combina elementos visuais e sonoros, como filmes, vídeos, comerciais e programas de TV, para comunicar mensagens, contar histórias ou entreter o público. Envolve pré-produção, gravação e pós-produção para criar uma experiência completa.")

class Filmes(ProduçãoAúdioVisual):
    def definição2 (self):
        print ("Um filme é uma produção audiovisual que combina imagens em movimento, áudio e muitas vezes diálogo para contar histórias, transmitir mensagens ou entreter o público.")

class Séries(ProduçãoAúdioVisual):
    def definição3 (self):
        print ("Uma série é uma forma de produção audiovisual que consiste em episódios consecutivos, geralmente com uma trama contínua. Cada episódio contribui para o desenvolvimento de uma história mais ampla e pode pertencer a diferentes gêneros.")
    
###################################################################################################################################
#Genero dos filmes
class Ação_Filmes(Filmes):
    def filmesação(self):
        print("Esta é a lista dos filmes de ação disponíveis:\n")
        
        
class Aventura_Filmes(Filmes):
    def filmesaventura(self):
        print("Esta é a lista dos filmes de aventura disponíveis:\n")
        
        
class Comédia_Filmes(Filmes):
    def filmescomédia(self):
        print("Esta é a lista dos filmes de comédia disponíveis:\n")
        

class Romance_Filmes(Filmes):
    def filmesromance(self):
        print("Esta é a lista dos filmes de romance disponíveis:\n")
        
        
###############################################################################################
#Genero das séries
class Ação_Séries(Séries):
    def seriesação(self):
        print("Esta é a lista das séries de ação disponíveis:\n")
        
        
class Comédia_Séries(Séries):
    def seriescomédia(self):
        print("Esta é a lista das séries de comédia disponíveis:\n")
        


class Romance_Séries(Séries):
    def seriesromance(self):
        print("Esta é a lista das séries de romance disponíveis:\n")
        

                  
pav = ProduçãoAúdioVisual ()  
filmes = Filmes()
series = Séries()
aç_fil = Ação_Filmes()
av_fil = Aventura_Filmes()
com_fil = Comédia_Filmes()
rom_fil = Romance_Filmes()
aç_ser = Ação_Séries()
com_ser = Comédia_Séries()
rom_ser = Romance_Séries()

y = 0

while y == 0:
    print ("\nBEM-VINDO AO MALTFLIX! Um software que te proporciona sinopses de produções audiovisuais. Para você que não sabe o que é esse tipo de produção, aqui vai uma definição: \n")
    pav.definição()
    try:
        menu = int(input("Você deseja ver sinopse do que?\n \n[1] Filmes \n[2] Séries \n[3] Sair \n \nDigite a opção desejada: "))
        match menu:
            case 1:
                os.system("cls")
                filmes.definição2()
                try:
                    gen = int(input("\nA lista de filme de qual genêro você deseja ver? \n[1] Ação \n[2] Aventura \n[3] Comédia \n[4] Romance \n[5] Voltar \n[6] Sair \n \nDigite a opção desejada: "))
                    match gen:
                        case 1: #Filmes ação
                            os.system("cls")
                            aç_fil.filmesação()
                            op1 = int(input("[1] Velozes & Furiosos \n[2] A Origem \n[3] 007 - Operação Skyfall \n[4] Voltar \n[5] Sair\n \nDigite a opção desejada: "))
                            match op1:
                                case 1:
                                    os.system("cls")
                                    print("Velozes & Furiosos \n \n2001 | Classificação etária:12 | 1h 46min | Ação \n \nSinopse: Domenic Toretto é o líder de uma gangue de corridas de ruas em Los Angeles que está sendo investigado pela polícia por roubo de equipamentos eletrônicos. Para investigá-lo é enviado Brian Spindler, que se infiltra na gangue na intenção de descobrir se Toretto é realmente o autor dos crimes e se há alguém mais por trás deles. \n \nEstrelando: Vin Diesel, Paul Walker, Michelle Rodriguez")
                                    os.system("pause")
                                    os.system("cls")
                                case 2:
                                    os.system("cls")
                                    print("A Origem \n \n2010 | Classificação etária:16 | 2h 28min | Ação \n \nSinopse: A Origem (ou Inception) é um filme de ficção científica que conta a história de um grupo de golpistas que utiliza uma máquina de invadir sonhos para conquistar os seus objetivos mais audaciosos. \n \nEstrelando: Leonardo DiCaprio,Joseph Gordon-Levitt,Cillian Murphy")    
                                    os.system("pause")
                                    os.system("cls")
                                case 3:
                                    os.system("cls")
                                    print("007 - Operação Skyfall \n \n2012 | Classificação etária:14 | 2h 23min | Ação \n \nSinopse: Na trama de 007 - Operação Skyfall, a lealdade do agente 007 a M é testada quando o passado dela volta a assombrá-la. Com o MI6 sob ataque, Bond deve rastrear e destruir a ameaça, mesmo que isso tenha um custo pessoal \n \nEstrelando: Daniel Craig ,Javier Bardem ,Judi Dench")    
                                    os.system("pause")
                                    os.system("cls")
                                case 4:
                                    os.system("cls")
                                case 5:
                                    y = 1
                                case _:
                                    op_invalida()
                                
                        case 2: #Filmes aventura
                            os.system("cls")
                            av_fil.filmesaventura()
                            op2 = int(input("[1] Super Mario Bros. O Filme \n[2] Gato de Botas 2: O Último Pedido \n[3] Miraculous: Le Film \n[4] Voltar \n[5] Sair \n \nDigite a opção desejada: "))
                            match op2:
                                case 1:
                                    os.system("cls")
                                    print("Super Mario Bros. O Filme \n \n2023 | Classificação etária: livre | 1h 32min | Aventura/Comédia \n \nSinopse: Mario é um encanador junto com seu irmão Luigi. Um dia, eles vão parar no reino dos cogumelos, governado pela Princesa Peach, mas ameaçado pelo rei dos Koopas, que faz de tudo para conseguir reinar em todos os lugares.")
                                    os.system("pause")
                                    os.system("cls")
                                case 2:
                                    os.system("cls")
                                    print("Gato de Botas 2: O Último Pedido \n \n2022 | Classificação etária: livre | 1h 40min | Aventura/Comédia \n \nSinopse: O Gato de Botas descobre que sua paixão pela aventura cobrou seu preço: ele já gastou oito de suas nove vidas. Ele então parte em uma jornada épica para encontrar o mítico Último Desejo e restaurar suas nove vidas.")
                                    os.system("pause")
                                    os.system("cls")
                                case 3:
                                    os.system("cls")
                                    print("Miraculous: Le Film \n \n2023 | Classificação etária: livre | 1h 45min | Aventura/Animação \n \nSinopse: Ladybug une forças com Cat Noir, o vigilante mascarado, para derrotar uma equipe de vilões que ameaçam destruir Paris. O que a garota não sabe é que, por trás da máscara de seu companheiro, se esconde um pessoa que ela conhece muito bem.")
                                    os.system("pause")
                                    os.system("cls")
                                case 4:
                                    os.system("cls")
                                case 5:
                                    y = 1
                                case _:
                                    op_invalida()
                        

                        case 3: #Filmes comédia
                                os.system("cls")
                                com_fil.filmescomédia()
                                op3 = int(input("[1] Free Guy \n[2] Trem-Bala \n[3] Legalmente loira \n[4] Voltar \n[5] Sair \n \nDigite a opção desejada: "))
                                match op3:
                                    case 1:
                                        os.system("cls")
                                        print("Free Guy\n \n 2021 | Classificação etária: 12 | 1h 55min | Comédia \n \nSinopse: Preso numa entediante rotina como caixa bancário, Guy tem sua vida estremecida ao descobrir que é na verdade personagem de um jogo realista de videogame. Enquanto digere a realidade, vai precisar lidar com o fato de que é o único capaz de salvar esse mundo aberto. \n \nEstrelando: Ryan Reynold, Jodie Comer, Joe Keery.")
                                        os.system("pause")
                                        os.system("cls")
                                    case 2:
                                        os.system("cls")
                                        print("Trem-bala\n \n 2022 | Classificação etária: 16 | 2h 06min | Comédia \n \nSinopse: Em Trem-Bala, Ladybug (Brad Pitt) é um assassino azarado, determinado a fazer seu trabalho pacificamente depois de muitas missões saírem dos trilhos. Quase desistindo de sua carreira, ele é recrutado por Maria Beetle (Sandra Bullock) para coletar uma maleta em um trem-bala indo de Tóquio para Morioka. \n \nEstrelando: Brad Pitt, Aaron Taylor-Johnson, Joey King.")
                                        os.system("pause")
                                        os.system("cls")    
                                    case 3:
                                        os.system("cls")
                                        print("Legalmente Loira\n \n 2001 | Classificação etária: Livre | 1h 34min | Comédia \n \nSinopse: Elle namora Warner, o garoto mais bonito do colégio, com quem pretende futuramente se casar. Mas ele a acha fútil demais, no fim das contas. Elle então decide provar sua inteligência para manter firme o romance. \n \nEstrelando: Reese Whiterspoon, Jennifer Coolidge, Luke Wilson.")
                                        os.system("pause")
                                        os.system("cls")
                                    case 4:
                                        os.system("cls")
                                    case 5:
                                        y = 1
                                    case _:
                                        op_invalida() 
                        case 4: #Filmes romance
                            os.system("cls")
                            rom_fil.filmesromance()
                            op4 = int(input("\n[1] Continência ao Amor \n[2] A Barraca do Beijo \n[3] Para Todos os Garotos que Já Amei \n[4] Voltar  \n[5] Sair\n \nDigite a opção desejada: "))
                            match op4:
                                case 1:
                                    os.system("cls")
                                    print("Continência ao Amor \n \n2022 | Classificação etária:14 | 2h 4min | Romance \n \nSinopse: Uma cantora se casa por conveniência com um militar prestes a ir para a guerra, mas uma tragédia transforma esse relacionamento de fachada em realidade. \n \nEstrelando: Sofia Carson, Nicholas Galitzine, Chosen Jacobs.")
                                    os.system("pause")
                                    os.system("cls")
                                case 2:
                                    os.system("cls")
                                    print("A Barraca do Beijo \n \n2018 | Classificação etária:12 | 1h 46min | Romance \n \nSinopse: O primeiro beijo de Elle vira um romance proibido com o cara mais gato da escola, mas acaba colocando em risco a relação com seu melhor amigo. \n \nEstrelando: Joey King, Joel Courtney, Jacob Elordi")
                                    os.system("pause")
                                    os.system("cls")
                                case 3:
                                    os.system("cls")
                                    print("Para Todos os Garotos qu eu Já Amei \n \n2018 | Classificação etária:12 | 1h 40min | Romance \n \nSinopse: Lara Jean adora escrever cartas de amor secretas para seus paqueras. Só não contava que um dia elas seriam misteriosamente enviadas! \n \nEstrelando: Lana Condor, Noah Centineo, Janel Parrish")
                                    os.system("pause")
                                    os.system("cls")
                                case 4:
                                    os.system("cls")
                                case 5:
                                    y = 1
                                case _:
                                    op_invalida()
                except Exception as erro:
                    print("Opção inválida.")
                    os.system("pause")
                    os.system("cls")
                    
            case 2:
                os.system("cls")
                series.definição3()
                try:
                    gen2 = int(input("\nA lista de série de qual genêro você deseja ver? \n [1] Ação \n [2] Comédia \n [3] Romance \n [4] Voltar \n [5] Sair \n \nDigite a opção desejada: "))
                    match gen2:
                        case 1: #Séries ação
                            os.system("cls")
                            aç_ser.seriesação()
                            opç1 = int(input("[1] Game of Thrones \n[2] Loki \n[3] The Walking Dead \n[4] Voltar \n[5] Sair \n \nDigite a opção desejada: "))
                            match opç1:
                                case 1:
                                    os.system("cls")
                                    print("Game of Thrones \n \n 2011 | Classificação etária: 16 | 8 temporadas | Ação \n \nSinopse: A história gira em torno de uma batalha entre os Sete Reinos, onde duas famílias dominantes estão lutando pelo controle do Trono de Ferro, cuja posse possivelmente assegurará a sobrevivência durante o inverno que está por vir. \n \nEstrelando: Emilia Clarke, Sophie Turner, Maisie Williams")
                                    os.system("pause")
                                    os.system("cls")
                                case 2:
                                    os.system("cls")
                                    print("Loki \n \n 2021 | Classificação etária: 14 | 2 temporadas | Ação \n \nSinopse: A série acompanhará Loki — irmão de Thor, príncipe de Asgard, Deus da Mentira e má influência intergaláctica — depois de roubar o Tesseract (cubo que contém uma das joias do infinito) em Vingadores: Ultimato. A história será a versão do personagem. \n \nEstrelando: Tom Hiddleston, Sophia Di Martino, Jonathan Majors")
                                    os.system("pause")
                                    os.system("cls")
                            
                                case 3:
                                    os.system("cls")
                                    print("The Walking Dead \n \n 2010 | Classificação etária: 16 | 11 temporadas | Ação \n \nSinopse: conta a história de um grupo de sobreviventes, liderados pelo xerife Rick Grimes (Andrew Lincoln), após um apocalipse zumbi. Toda a população da Terra é infectada por um vírus misterioso que transforma os mortos em zumbis. \n \nEstrelando: Norman Reedus, Andrew Lincoln, Melissa McBride")
                                    os.system("pause")
                                    os.system("cls")
                                case 4:
                                    os.system("cls")
                                case 5:
                                    y = 1
                                case _:
                                    op_invalida()

                        case 2: #Séries comédia
                            os.system("cls")
                            com_ser.seriescomédia()
                            opç2 = int(input("[1] Brooklyn Nine-Nine \n[2] Ginny e Georgia \n[3] The Good Place \n[4] Voltar \n[5] Sair \n \nDigite a opção desejada: "))
                            match opç2:
                                case 1:
                                    os.system("cls")
                                    print("Brooklyn Nine-Nine \n \n2013 | Classificação etária:14 | 8 temporadas | Comédia \n \nSinopse: O brilhante e imaturo detetive Jake Peralta precisa aprender a seguir as regras e trabalhar em equipe quando um capitão exigente assume o comando de seu esquadrão. \n \nEstrelando:Andy Samberg, Andre Braugher, Stephanie Beatriz")
                                    os.system("pause")
                                    os.system("cls")
                                case 2:
                                    os.system("cls")
                                    print("Ginny e Georgia \n \n2021 | Classificação etária:16 | 2 temporadas | Comédia dramática \n \nSinopse: Em busca de uma nova chance, Georgia leva os filhos Ginny e Austin para morar em outra cidade. Só que recomeçar do zero não é tão simples assim. \n \nEstrelando: Brianne Howey, Antonia Gentry, Diesel La Torraca")
                                    os.system("pause")
                                    os.system("cls")
                                case 3:
                                    os.system("cls")
                                    print("Tho Good Place \n \n2016 | Classificação etária:14 | 4 temporadas | Comédia \n \nSinopse: Depois de morrer, a egocêntrica Eleanor é enviada por engano ao lado bom do Além. Agora ela está determinada a se tornar uma pessoa melhor para continuar lá. \n \nEstrelando: Kristen Bell,Ted Danson,William Jackson Harper")
                                    os.system("pause")
                                    os.system("cls")
                                case 4:
                                    os.system("cls")
                                case 5:
                                    y = 1
                                case _:
                                    op_invalida()

                        case 3: #Séries romance
                            os.system("cls")
                            rom_ser.seriesromance()
                            opç3 = int(input("[1] Vinte e Cinco, Vinte e Um \n[2] Beleza Verdadeira \n[3] Passarela de Sonhos \n[4] Voltar \n[5] Sair \n \nDigite a opção desejada: "))
                            match opç3:
                                case 1:
                                    os.system("cls")
                                    print("Vinte e Cinco, Vinte e Um \n \n2022 | Classificação etária:12 | 1 temporada | Romance \n \nSinopse: Em uma época de crise financeira, o sonho de Na Hee-do de se tornar uma grande esgrimista é ameaçado, mas a garota não desiste e luta para alcançar seus objetivos. Ao mesmo tempo, ela descobre o amor junto com o Back Yi-jin. \n \nEstrelando: Kim Tae-ri, Nam Joo-hyuk, Kim Ji-yeon.")
                                    os.system("pause")
                                    os.system("cls")
                                case 2:
                                    os.system("cls")
                                    print("Beleza Verdadeira \n \n2020 | Classificação etária:14 | 1 temporada | Romance \n \nSinopse: Uma estudante esconde seu passado doloroso e aprende técnicas de maquiagem que a tornam popular. \n \nEstrelando: Cha Eun Woo, Moon Ga Young, Hwang In Yeop, Park Yoo Na.")
                                    os.system("pause")
                                    os.system("cls")
                                case 3:
                                    os.system("cls")
                                    print("Passarela de Sonhos \n \n2020 | Classificação etária:12 | 1 temporada | Romance \n \nSinopse: Dois atores e uma maquiadora lutam para conquistar espaço em um mundo que valoriza mais a classe social do que seus sonhos. \n \nEstrelando: Park Bo-gum, Park So-dam, Byeon Woo-seok.")
                                    os.system("pause")
                                    os.system("cls")
                                case 4:
                                    os.system("cls")
                                case 5:
                                    y = 1
                                case _:
                                    op_invalida()
                        case 4:
                            os.system("cls")
                        case 5:
                            y = 1
                        case _:
                            op_invalida()
                except Exception as erro:
                    print("Opção inválida.")
                    os.system("pause")
                    os.system("cls")
            case 3:
                y = 1
            case _:
                op_invalida()
    except Exception as erro:
        print("Opção inválida.")
        os.system("pause")
        os.system("cls")