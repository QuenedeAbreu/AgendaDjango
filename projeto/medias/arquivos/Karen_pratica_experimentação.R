dados1 <- read.csv("C:/Users/LABEST/Desktop/Dados/Dados/dados1.txt", sep="")
dados1

colnames(dados1)
attach( dados1 )

# Grafico de interação
# Fator A: tipo de manejo
# Fator B: silagem
# Variavel resposta: Ganho de peso
interaction.plot(manejo,silagem, GP)

interaction.plot(silagem, manejo, GP)

# medidas descritivas
tapply( GP ,list( manejo,silagem), mean # media
tapply( GP, list(manejo,silagem), sd) # desvio padrao

# Ajuste do modelo anov: Exp Fatorial
library(ExpDes.pt)
res = fat2.dic(manejo,silagem,GP)
plotres(res)

# Teste de Bartlett
# H0: variancia homogeneas
# Ha: as variancias nao sao homogeneas
bartlett.test( GP ~ paste0( manejo, silagem) )

###Ajuste de parcelas subdivididas: Exemplo 4
dados4 <- read.csv("C:/Users/LABEST/Desktop/Dados/Dados/dados4.txt", sep="")
dados4
colnames( dados4 ) 
attach(dados4)
# ajustar a anova
# Fator A (parcelas): Diluente
# Fator B (subparcelas): Tempo
# Variavel resposta: motilidade
psub2.dbc(Diluente,Tempo,Bloco,y)


psub2.dbc(Diluente,Tempo,Bloco,y, quali = c(TRUE,FALSE)

          
          
          