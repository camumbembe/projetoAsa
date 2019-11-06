
arquivo = open('/etc/named.projeto', 'a+')

nomeZona = input('Informe o nome do seu domínio:')

arquivo.write(“zone nomeZona IN {”) 
arquivo.write(“type master;”) 
arquivo.write(“file nomeZona+'.zone' ;”) 
arquivo.write(“};”) 
 
arquivo.close() 

arqZone = open('/var/named/projeto/nomedazona', 'a+')

arqZone.write("$TTL 10")
arqZone.write("$ORIGIN nomeZona+'.'")
arqZone.write("@                        IN SOA       @ root (")
arqZone.write("10;")
arqZone.write("3H;")
arqZone.write("15M;")
arqZone.write("1W;")
arqZone.write("10);")
arqZone.write("                        IN NS    @")
arqZone.write("                        IN A         192.168.102.156")
arqZone.write("www             IN      A       192.168.102.156")
arqZone.write("")
arqZone.write("")
arqZone.write("")


