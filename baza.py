import sqlite3 as dbapi

conn = dbapi.connect('baza_bijele_tehnike.db')
print ("Opened database successfully")

cursor=conn.cursor()
cursor.execute('DROP TABLE bijela_tehnika')
cursor.execute('CREATE TABLE bijela_tehnika (id INTEGER, aparat TEXT, proizvodjac TEXT, boja TEXT, cijena INTEGER, stanje INTEGER)')

lista=[(1,'masina_za_ves','Beko','bijela',440,15),
       (2,'masina_za_ves','Beko','siva',470,10),
       (3,'masina_za_ves','Gorenje','bijela',460,20),
       (4,'masina_za_ves','Gorenje','siva',485,15),
       (5,'masina_za_ves','LG','bijela',640,12),
       (6,'masina_za_ves','LG','siva',680,10),
       (7,'masina_za_ves','Zanussi','bijela',430,10),
       (8,'masina_za_ves','Zanussi','siva',450,8),
       (9,'masina_za_ves','Miele','bijela',880,12),
       (10,'masina_za_ves','Miele','siva',1050,10),
       
       (11,'masina_za_sudje','Beko','bijela',455,13),
       (12,'masina_za_sudje','Beko','siva',475,11),
       (13,'masina_za_sudje','Beko','crna',485,10),
       (14,'masina_za_sudje','Gorenje','bijela',465,18),
       (15,'masina_za_sudje','Gorenje','siva',485,16),
       (16,'masina_za_sudje','Gorenje','crna',495,14),
       (17,'masina_za_sudje','Vox','bijela',435,14),
       (18,'masina_za_sudje','Vox','siva',445,12),
       (19,'masina_za_sudje','Vox','crna',455,11),
       (20,'masina_za_sudje','Elektrolux','bijela',459,13),
       (21,'masina_za_sudje','Elektrolux','siva',469,11),
       (22,'masina_za_sudje','Elektrolux','crna',480,10),
       
       (23,'masina_za_susenje','Beko','bijela',445,15),
       (24,'masina_za_susenje','Beko','siva',475,10),
       (25,'masina_za_susenje','Gorenje','bijela',465,20),
       (26,'masina_za_susenje','Gorenje','siva',490,15),
       (27,'masina_za_susenje','LG','bijela',645,12),
       (28,'masina_za_susenje','LG','siva',685,10),
       (29,'masina_za_susenje','Zanussi','bijela',435,10),
       (30,'masina_za_susenje','Zanussi','siva',455,8),
       (31,'masina_za_susenje','Miele','bijela',885,12),
       (32,'masina_za_susenje','Miele','siva',1045,10),
       
       (33,'usisivac','Samsung','crna',145,12),
       (34,'usisivac','Samsung','siva',155,12),
       (35,'usisivac','Samsung','crvena',155,12),
       (36,'usisivac','LG','crna',155,15),
       (37,'usisivac','LG','siva',165,10),
       (38,'usisivac','LG','crvena',165,10),
       (39,'usisivac','Gorenje','crna',150,15),
       (40,'usisivac','Gorenje','siva',160,10),
       (41,'usisivac','Gorenje','crvena',165,10),
       
       (42,'elektricni_sporet','Beko','bijela',405,13),
       (43,'elektricni_sporet','Beko','siva',415,11),
       (44,'elektricni_sporet','Beko','crna',425,10),
       (45,'elektricni_sporet','Gorenje','bijela',415,18),
       (46,'elektricni_sporet','Gorenje','siva',425,16),
       (47,'elektricni_sporet','Gorenje','crna',435,14),
       (48,'elektricni_sporet','Zanussi','bijela',365,14),
       (49,'elektricni_sporet','Zanussi','siva',375,12),
       (50,'elektricni_sporet','Zanussi','crna',385,11),
       (51,'elektricni_sporet','Elektrolux','bijela',369,13),
       (52,'elektricni_sporet','Elektrolux','siva',379,11),
       (53,'elektricni_sporet','Elektrolux','crna',389,10),
       
       (54,'frizider','Beko','bijela',380,20),
       (55,'frizider','Beko','siva',400,18),
       (56,'frizider','Gorenje','bijela',410,20),
       (57,'frizider','Gorenje','siva',425,20),
       (58,'frizider','Vox','bijela',370,19),
       (59,'frizider','Vox','siva',390,18),
       (60,'frizider','Zanussi','bijela',375,22),
       (61,'frizider','Zanussi','siva',395,20), 
       
       (62,'zamrzivac','Beko','bijela',480,20),
       (62,'zamrzivac','Beko','siva',500,18),
       (64,'zamrzivac','Gorenje','bijela',510,20),
       (65,'zamrzivac','Gorenje','siva',525,20),
       (66,'zamrzivac','Vox','bijela',470,19),
       (67,'zamrzivac','Vox','siva',490,18),
       (68,'zamrzivac','Zanussi','bijela',475,22),
       (69,'zamrzivac','Zanussi','siva',495,20),
       
       (70,'blender','LG','bijela',160,10),
       (71,'blender','LG','siva',170,10),
       (72,'blender','LG','crna',170,10),
       (73,'blender','Elektrolux','bijela',130,12),
       (74,'blender','Elektrolux','siva',140,12),
       (75,'blender','Elektrolux','crna',150,12),
       (76,'blender','Gorenje','bijela',160,15),
       (77,'blender','Gorenje','siva',170,15),
       (78,'blender','Gorenje','crna',180,15),
       (79,'blender','Vox','bijela',100,11),
       (80,'blender','Vox','siva',110,11),
       (81,'blender','Vox','crna',120,11),
       
       (82,'mikser','LG','bijela',100,10),
       (83,'mikser','LG','siva',110,10),
       (84,'mikser','LG','crna',120,10),
       (85,'mikser','Elektrolux','bijela',70,12),
       (86,'mikser','Elektrolux','siva',80,12),
       (87,'mikser','Elektrolux','crna',80,12),
       (88,'mikser','Gorenje','bijela',120,15),
       (89,'mikser','Gorenje','siva',125,15),
       (90,'mikser','Gorenje','crna',125,15),
       (91,'mikser','Vox','bijela',55,11),
       (92,'mikser','Vox','siva',70,11),
       (93,'mikser','Vox','crna',70,11)]

for l in lista:
    cursor.execute('''INSERT INTO bijela_tehnika VALUES (?,?,?,?,?,?)''',(l[0],l[1],l[2],l[3],l[4],l[5]))
cursor.execute('SELECT * FROM bijela_tehnika')
print (cursor.fetchall())
conn.commit()