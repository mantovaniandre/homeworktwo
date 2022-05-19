from typing import final
from Database.connection import MySQLDatabase

class CreatingDataBase:
    def creatingDataBase(db: MySQLDatabase):
       print("ENTREI NA CRIAÇÃO DO BANCO DE DADOS")
       try:
           sql = """
                    CREATE TABLE tboa7006_even_esol (
                    cod_idef_unic_even VARCHAR(36) NOT NULL,
                    cod_even_gerr VARCHAR(36) NOT NULL,
                    ano_mes_apur_even VARCHAR(36) NOT NULL,
                    cod_esta_even VARCHAR(36) NOT NULL,
                    cod_prdo_apur VARCHAR(36) NOT NULL,
                    cod_idef_rtfo VARCHAR(36) NOT NULL,
                    cod_tipo_insc_rctf VARCHAR(36) NOT NULL,
                    num_insc_empr VARCHAR(36) NOT NULL,
                    cod_idef_orig_prso VARCHAR(36) NOT NULL,
                    num_cada_pess_fisi VARCHAR(36) NOT NULL,
                    dat_pgto date NOT NULL,
                    cod_tipo_pgto TINYINT NOT NULL,
                    num_reci_even VARCHAR(36),
                    cod_even_gerr_antr VARCHAR(36),
                    cod_idef_unic_even_antr VARCHAR(36),
                    txt_vers_even VARCHAR(36),
                    dat_hor_ulti_atui datetime,
                    PRIMARY KEY (cod_idef_unic_even)); 
                """
           db.execute_query(sql, [])
           db.commit()
           db.close()
           print("[INFO] TABELA CRIADA COM SUCESSO")
       
       except Exception as e:
           print("[INFO] ERRO: ", e)
        
            
