from Database.connection import MySQLDatabase

class InsertingDataIntoTheDatabase:
    def inserting(db: MySQLDatabase):
        
        try:
            
            db.connect()
            
            sql1 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA7512002021071612340321900000001", "S1200", 202009, "NO", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql2 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA7512002021071612340321900000002", "S1200", 202009, "ER", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql3 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA7512002021071612340321900000003", "S1200", 202009, "EP", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql4 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA7512002021071612340321900000004", "S1200", 202009, "SA", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql5 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA7512002021071612340321900000005", "S1200", 202009, "EP", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql6 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA7512002021071612340321900000006", "S1200", 202009, "ER", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql7 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA7512002021071612340321900000007", "S1200", 202009, "EP", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql8 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA7512002021071612340321900000008", "S1200", 202009, "SA", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql9 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA7512002021071612340321900000009", "S1200", 202009, "EX", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql10 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000010", "S1200", 202009, "SA", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql11 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000011", "S1200", 202009, "SA", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql12 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000012", "S1200", 202009, "ER", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql13 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000013", "S1200", 202009, "EX", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql14 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000014", "S1200", 202009, "SA", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql15 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000015", "S1200", 202009, "SA", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql16 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000016", "S1200", 202009, "NO", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql17 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000017", "S1200", 202009, "EX", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql18 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000018", "S1200", 202009, "EP", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql19 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000019", "S1200", 202009, "RP", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            sql20 = """
                    INSERT INTO tboa7006_even_esol
                        (cod_idef_unic_even, cod_even_gerr, ano_mes_apur_even,
                        cod_esta_even, cod_prdo_apur, cod_idef_rtfo, cod_tipo_insc_rctf, num_insc_empr,
                        cod_idef_orig_prso, num_cada_pess_fisi, dat_pgto, cod_tipo_pgto, num_reci_even,
                        cod_even_gerr_antr, cod_idef_unic_even_antr, txt_vers_even, dat_hor_ulti_atui) 
                        VALUES
                        ("IDOA75120020210716123403219000000020", "S1200", 202009, "SA", 1, "1", 1, "12345678910121", "P", "12345678901", "2010-01-12", 1, "1.1.0000000000610688001", "IDOA7512002021071612340321900000001", "IDOA7512002021071612340321900000001", "S1.0", NOW())
                """
            
            db.execute_query(sql1, {})
            db.commit()
            print("[INFO] DADOS INSERIDOS NA TABELA CORRETAMENTE")
        except Exception as e:
            print("[INFO] ERRO: ", e)
                