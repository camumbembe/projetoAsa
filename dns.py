
arquivo = open('/etc/named.projeto', 'a+')

nomeZona = input('Informe o nome do seu domínio:')

arquivo.write(“zone nomeZona IN {”) 
arquivo.write(“type master;”) 
arquivo = open('teste.txt', 'a+')

nomeZona = input('Informe o nome do seu domínio:')



arquivo.write( """zone "{0}" IN {{
type master;
file "{0}.zone";  
}};""".format(nomeZona))

#arquivo.write(teste.format(nomeZona))

arquivo.close()

arqZone = open('teste2.txt', 'a+')

arqZone.write(""" $TTL 10
   $ORIGIN nomeZona.
   @                        IN SOA       @ root (
   10;
   3H;
   15M;
   1W;
            10);
      IN NS    @
      IN A         192.168.102.156
www             IN      A       192.168.102.156
""")

arqZone.close()

