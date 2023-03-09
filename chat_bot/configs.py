TOKEN = '5856080361:AAEslvvgLI_-mkJia-lnVG2Sc78a-nFlUJg'

TICKERS = [
    'A32', 'AAA', 'AAM', 'AAS', 'AAT', 'AAV', 'ABB', 'ABC', 'ABI', 'ABR', 'ABS', 'ABT', 'ACB', 'ACC', 'ACE', 'ACG', 'ACL', 'ACM', 'ACS', 'ACV', 'ADC', 'ADG', 'ADP', 'ADS', 'AFX', 'AG1', 'AGE', 'AGF', 'AGG', 'AGM', 'AGP', 'AGR', 'AGX', 'AIC', 'ALT', 'ALV', 'AMC', 'AMD', 'AME', 'AMP', 'AMS', 'AMV', 'ANT', 'ANV', 'APC', 'APF', 'APG', 'APH', 'API', 'APL', 'APP', 'APS', 'APT', 'ARM', 'ART', 'ASA', 'ASG', 'ASM', 'ASP', 'AST', 'ATA', 'ATB', 'ATG', 'ATS', 'AUM', 'AVC', 'AVF', 'B82', 'BAB', 'BAF', 'BAL', 'BAX', 'BBC', 'BBH', 'BBM', 'BBS', 'BBT', 'BCA', 'BCB', 'BCC', 'BCE', 'BCF', 'BCG', 'BCM', 'BCP', 'BCV', 'BDB', 'BDG', 'BDT', 'BDW', 'BED', 'BEL', 'BFC', 'BGW', 'BHA', 'BHC', 'BHG', 'BHK', 'BHN', 'BHP', 'BHT', 'BIC', 'BID', 'BIG', 'BII', 'BIO', 'BKC', 'BKG', 'BKH', 'BLF', 'BLI', 'BLN', 'BLT', 'BLW', 'BMC', 'BMD', 'BMF', 'BMG', 'BMI', 'BMJ', 'BMN', 'BMP', 'BMS', 'BMV', 'BNA', 'BNW', 'BOT', 'BPC', 'BQB', 'BRC', 'BRR', 'BRS', 'BSA', 'BSC', 'BSD', 'BSG', 'BSH', 'BSI', 'BSL', 'BSP', 'BSQ', 'BSR', 'BST', 'BT1', 'BT6', 'BTB', 'BTD', 'BTG', 'BTH', 'BTN', 'BTP', 'BTS', 'BTT', 'BTU', 'BTV', 'BTW', 'BVB', 'BVG', 'BVH', 'BVL', 'BVN', 'BVS', 'BWA', 'BWE', 'BWS', 'BXH', 'C12', 'C21', 'C22', 'C32', 'C36', 'C47', 'C4G', 'C69', 'C71', 'C92', 'CAB', 'CAD', 'CAG', 'CAN', 'CAP', 'CAR', 'CAT', 'CAV', 'CBC', 'CBI', 'CBS', 'CC1', 'CC4', 'CCA', 'CCI', 'CCL', 'CCM', 'CCP', 'CCR', 'CCT', 'CCV', 'CDC', 'CDG', 'CDH', 'CDN', 'CDO', 'CDP', 'CDR', 'CE1', 'CEG', 'CEN', 'CEO', 'CET', 'CFM', 'CFV', 'CGV', 'CH5', 'CHC', 'CHP', 'CHS', 'CI5', 'CIA', 'CID', 'CIG', 'CII', 'CIP', 'CJC', 'CK8', 'CKA', 'CKD', 'CKG', 'CKV', 'CLC', 'CLG', 'CLH', 'CLL', 'CLM', 'CLW', 'CLX', 'CMC', 'CMD', 'CMF', 'CMG', 'CMI', 'CMK', 'CMM', 'CMN', 'CMP', 'CMS', 'CMT', 'CMV', 'CMW', 'CMX', 'CNA', 'CNC', 'CNG', 'CNN', 'CNT', 'COM', 'CPA', 'CPC', 'CPH', 'CPI', 'CQN', 'CQT', 'CRC', 'CRE', 'CSC', 'CSI', 'CSM', 'CST', 'CSV', 'CT3', 'CT6', 'CTA', 'CTB', 'CTC', 'CTD', 'CTF', 'CTG', 'CTI', 'CTN', 'CTP', 'CTR', 'CTS', 'CTT', 'CTW', 'CTX', 'CVN', 'CVP', 'CVT', 'CX8', 'CYC', 'D11', 'D2D', 'DAC', 'DAD', 'DAE', 'DAG', 'DAH', 'DAN', 'DAP', 'DAS', 'DAT', 'DBC', 'DBD', 'DBM', 'DBT', 'DC1', 'DC2', 'DC4', 'DCF', 'DCG', 'DCH', 'DCL', 'DCM', 'DCR', 'DCS', 'DCT', 'DDG', 'DDH', 'DDM', 'DDN', 'DDV', 'DFC', 'DFF', 'DGC', 'DGT', 'DGW', 'DHA', 'DHB', 'DHC', 'DHD', 'DHG', 'DHM', 'DHN', 'DHP', 'DHT', 'DIC', 'DID', 'DIG', 'DIH', 'DKC', 'DL1', 'DLD', 'DLG', 'DLM', 'DLR', 'DLT', 'DM7', 'DMC', 'DMN', 'DNA', 'DNC', 'DND', 'DNE', 'DNH', 'DNL', 'DNM', 'DNN', 'DNP', 'DNT', 'DNW', 'DOC', 'DOP', 'DP1', 'DP2', 'DP3', 'DPC', 'DPD', 'DPG', 'DPH', 'DPM', 'DPP', 'DPR', 'DPS', 'DQC', 'DRC', 'DRG', 'DRH', 'DRI', 'DRL', 'DS3', 'DSC', 'DSD', 'DSG', 'DSN', 'DSP', 'DST', 'DSV', 'DTA', 'DTB', 'DTC', 'DTD', 'DTE', 'DTG', 'DTH', 'DTI', 'DTK', 'DTL', 'DTN', 'DTP', 'DTT', 'DTV', 'DUS', 'DVC', 'DVG', 'DVM', 'DVN', 'DVP', 'DVW', 'DWC', 'DWS', 'DXG', 'DXL', 'DXP', 'DXS', 'DXV', 'DZM', 'E12', 'E1VFVN30', 'E29', 'EBS', 'ECI', 'EFI', 'EIB', 'EIC', 'EID', 'EIN', 'ELC', 'EMC', 'EME', 'EMG', 'EMS', 'EPC', 'EPH', 'EVE', 'EVF', 'EVG', 'EVS', 'FBA', 'FBC', 'FCC', 'FCM', 'FCN', 'FCS', 'FDC', 'FGL', 'FHN', 'FHS', 'FIC', 'FID', 'FIR', 'FIT', 'FLC', 'FMC', 'FOC', 'FOX', 'FPT', 'FRC', 'FRM', 'FRT', 'FSO', 'FT1', 'FTI', 'FTM', 'FTS', 'FUCTVGF3', 'FUCTVGF4', 'FUCVREIT', 'FUEDCMID', 'FUEIP100', 'FUEKIV30', 'FUEKIVFS', 'FUEMAV30', 'FUESSV30', 'FUESSV50', 'FUESSVFL', 'FUEVFVND', 'FUEVN100', 'G20', 'G36', 'GAB', 'GAS', 'GCB', 'GCF', 'GDT', 'GDW', 'GEE', 'GEG', 'GER', 'GEX', 'GGG', 'GH3', 'GHC', 'GIC', 'GIL', 'GKM', 'GLC', 'GLT', 'GLW', 'GMA', 'GMC', 'GMD', 'GMH', 'GMX', 'GND', 'GPC', 'GSM', 'GSP', 'GTA', 'GTD', 'GTH', 'GTS', 'GTT', 'GVR', 'GVT', 'H11', 'HAC', 'HAD', 'HAF', 'HAG', 'HAH', 'HAI', 'HAM', 'HAN', 'HAP', 'HAR', 'HAS', 'HAT', 'HAV', 'HAX', 'HBC', 'HBD', 'HBH', 'HBS', 'HC1', 'HC3', 'HCB', 'HCC', 'HCD', 'HCI', 'HCM', 'HCT', 'HD2', 'HD6', 'HD8', 'HDA', 'HDB', 'HDC', 'HDG', 'HDM', 'HDO', 'HDP', 'HDW', 'HEC', 'HEJ', 'HEM', 'HEP', 'HES', 'HEV', 'HFB', 'HFC', 'HFX', 'HGM', 'HGT', 'HGW', 'HHC', 'HHG', 'HHN', 'HHP', 'HHR', 'HHS', 'HHV', 'HID', 'HIG', 'HII', 'HIZ', 'HJC', 'HJS', 'HKB', 'HKP', 'HKT', 'HLA', 'HLB', 'HLC', 'HLD', 'HLG', 'HLR', 'HLS', 'HLT', 'HLY', 'HMC', 'HMG', 'HMH', 'HMR', 'HMS', 'HNA', 'HNB', 'HND', 'HNF', 'HNG', 'HNI', 'HNM', 'HNP', 'HNR', 'HOM', 'HOT', 'HPB', 'HPD', 'HPG', 'HPH', 'HPI', 'HPM', 'HPP', 'HPT', 'HPW', 'HPX', 'HQC', 'HRB', 'HRC', 'HRT', 'HSA', 'HSG', 'HSI', 'HSL', 'HSM', 'HSP', 'HSV', 'HT1', 'HTC', 'HTE', 'HTG', 'HTI', 'HTL', 'HTM', 'HTN', 'HTP', 'HTR', 'HTT', 'HTV', 'HTW', 'HU1', 'HU3', 'HU4', 'HU6', 'HUB', 'HUG', 'HUT', 'HVA', 'HVG', 'HVH', 'HVN', 'HVT', 'HVX', 'HWS', 'IBC', 'IBD', 'ICC', 'ICF', 'ICG', 'ICI', 'ICN', 'ICT', 'IDC', 'IDI', 'IDJ', 'IDP', 'IDV', 'IFS', 'IHK', 'IJC', 'ILA', 'ILB', 'ILC', 'ILS', 'IME', 'IMP', 'IN4', 'INC', 'INN', 'IPA', 'IRC', 'ISG', 'ISH', 'IST', 'ITA', 'ITC', 'ITD', 'ITQ', 'ITS', 'IVS', 'JOS', 'JVC', 'KAC', 'KBC', 'KCB', 'KCE', 'KDC', 'KDH', 'KDM', 'KGM', 'KHA', 'KHD', 'KHG', 'KHL', 'KHP', 'KHS', 'KHW', 'KIP', 'KKC', 'KLB', 'KLF', 'KLM', 'KMR', 'KMT', 'KOS', 'KPF', 'KSB', 'KSD', 'KSF', 'KSH', 'KSK', 'KSQ', 'KSS', 'KST', 'KSV', 'KTC', 'KTL', 'KTS', 'KTT', 'KTU', 'KVC', 'L10', 'L12', 'L14', 'L18', 'L35', 'L40', 'L43', 'L44', 'L45', 'L61', 'L62', 'L63', 'LAF', 'LAI', 'LAS', 'LAW', 'LBC', 'LBE', 'LBM', 'LCC', 'LCD', 'LCG', 'LCM', 'LCS', 'LCW', 'LDG', 'LDP', 'LDW', 'LEC', 'LG9', 'LGC', 'LGL', 'LGM', 'LHC', 'LHG', 'LIC', 'LIG', 'LIX', 'LKW', 'LLM', 'LM3', 'LM7', 'LM8', 'LMC', 'LMH', 'LMI', 'LNC', 'LO5', 'LPB', 'LPT', 'LQN', 'LSG', 'LSS', 'LTC', 'LTG', 'LUT', 'LWS', 'M10', 'MA1', 'MAC', 'MAS', 'MBB', 'MBG', 'MBN', 'MBS', 'MCC', 'MCD', 'MCF', 'MCG', 'MCH', 'MCI', 'MCM', 'MCO', 'MCP', 'MCT', 'MDA', 'MDC', 'MDF', 'MDG', 'MEC', 'MED', 'MEF', 'MEL', 'MES', 'MFS', 'MGC', 'MGG', 'MGR', 'MH3', 'MHC', 'MHL', 'MIC', 'MIE', 'MIG', 'MIM', 'MKP', 'MKV', 'MLC', 'MLS', 'MML', 'MNB', 'MND', 'MPC', 'MPT', 'MPY', 'MQB', 'MQN', 'MRF', 'MSB', 'MSH', 'MSN', 'MSR', 'MST', 'MTA', 'MTB', 'MTC', 'MTG', 'MTH', 'MTL', 'MTP', 'MTS', 'MTV', 'MVB', 'MVC', 'MVN', 'MWG', 'NAB', 'NAC', 'NAF', 'NAG', 'NAP', 'NAS', 'NAU', 'NAV', 'NAW', 'NBB', 'NBC', 'NBE', 'NBP', 'NBT', 'NBW', 'NCS', 'NCT', 'ND2', 'NDC', 'NDF', 'NDN', 'NDP', 'NDT', 'NDW', 'NDX', 'NED', 'NET', 'NFC', 'NGC', 'NHA', 'NHC', 'NHH', 'NHP', 'NHT', 'NHV', 'NJC', 'NKG', 'NLG', 'NLS', 'NNC', 'NNG', 'NNT', 'NO1', 'NOS', 'NQB', 'NQN', 'NQT', 'NRC', 'NS2', 'NSC', 'NSG', 'NSH', 'NSL', 'NSS', 'NST', 'NT2', 'NTB', 'NTC', 'NTF', 'NTH', 'NTL', 'NTP', 'NTT', 'NTW', 'NUE', 'NVB', 'NVL', 'NVP', 'NVT', 'NWT', 'NXT', 'OCB', 'OCH', 'ODE', 'OGC', 'OIL', 'ONE', 'ONW', 'OPC', 'ORS', 'PAC', 'PAI', 'PAN', 'PAP', 'PAS', 'PAT', 'PBC', 'PBK', 'PBP', 'PBT', 'PC1', 'PCC', 'PCE', 'PCF', 'PCG', 'PCH', 'PCM', 'PCN', 'PCT', 'PDB', 'PDC', 'PDN', 'PDR', 'PDV', 'PEC', 'PEG', 'PEN', 'PEQ', 'PET', 'PFL', 'PGB', 'PGC', 'PGD', 'PGI', 'PGN', 'PGS', 'PGT', 'PGV', 'PHC', 'PHH', 'PHN', 'PHP', 'PHR', 'PHS', 'PIA', 'PIC', 'PID', 'PIS', 'PIT', 'PIV', 'PJC', 'PJS', 'PJT', 'PLA', 'PLC', 'PLE', 'PLO', 'PLP', 'PLX', 'PMB', 'PMC', 'PMG', 'PMJ', 'PMP', 'PMS', 'PMT', 'PMW', 'PNC', 'PND', 'PNG', 'PNJ', 'PNP', 'PNT', 'POB', 'POM', 'POS', 'POT', 'POV', 'POW', 'PPC', 'PPE', 'PPH', 'PPI', 'PPP', 'PPS', 'PPT', 'PPY', 'PQN', 'PRC', 'PRE', 'PRO', 'PRT', 'PSB', 'PSC', 'PSD', 'PSE', 'PSG', 'PSH', 'PSI', 'PSL', 'PSN', 'PSP', 'PSW', 'PTB', 'PTC', 'PTD', 'PTE', 'PTG', 'PTH', 'PTI', 'PTL', 'PTN', 'PTO', 'PTP', 'PTS', 'PTT', 'PTV', 'PTX', 'PV2', 'PVA', 'PVB', 'PVC', 'PVD', 'PVE', 'PVG', 'PVH', 'PVI', 'PVL', 'PVM', 'PVO', 'PVP', 'PVR', 'PVS', 'PVT', 'PVV', 'PVX', 'PVY', 'PWA', 'PWS', 'PX1', 'PXA', 'PXC', 'PXI', 'PXL', 'PXM', 'PXS', 'PXT', 'QBS', 'QCC', 'QCG', 'QHD', 'QHW', 'QNC', 'QNS', 'QNT', 'QNU', 'QNW', 'QPH', 'QSP', 'QST', 'QTC', 'QTP', 'RAL', 'RAT', 'RBC', 'RCC', 'RCD', 'RCL', 'RDP', 'REE', 'RGC', 'RIC', 'ROS', 'RTB', 'S12', 'S27', 'S4A', 'S55', 'S72', 'S74', 'S96', 'S99', 'SAB', 'SAC', 'SAF', 'SAL', 'SAM', 'SAP', 'SAS', 'SAV', 'SB1', 'SBA', 'SBD', 'SBH', 'SBL', 'SBM', 'SBR', 'SBS', 'SBT', 'SBV', 'SC5', 'SCC', 'SCD', 'SCG', 'SCI', 'SCJ', 'SCL', 'SCO', 'SCR', 'SCS', 'SCY', 'SD1', 'SD2', 'SD3', 'SD4', 'SD5', 'SD6', 'SD7', 'SD8', 'SD9', 'SDA', 'SDB', 'SDC', 'SDD', 'SDG', 'SDJ', 'SDK', 'SDN', 'SDP', 'SDT', 'SDU', 'SDV', 'SDX', 'SDY', 'SEA', 'SEB', 'SED', 'SEP', 'SFC', 'SFG', 'SFI', 'SFN', 'SGB', 'SGC', 'SGD', 'SGH', 'SGI', 'SGN', 'SGO', 'SGP', 'SGR', 'SGS', 'SGT', 'SHA', 'SHB', 'SHC', 'SHE', 'SHG', 'SHI', 'SHN', 'SHP', 'SHS', 'SHX', 'SIC', 'SID', 'SIG', 'SII', 'SIP', 'SIV', 'SJ1', 'SJC', 'SJD', 'SJE', 'SJF', 'SJG', 'SJM', 'SJS', 'SKG', 'SKH', 'SKN', 'SKV', 'SLS', 'SMA', 'SMB', 'SMC', 'SMN', 'SMT', 'SNC', 'SNZ', 'SP2', 'SPB', 'SPC', 'SPD', 'SPH', 'SPI', 'SPM', 'SPP', 'SPV', 'SQC', 'SRA', 'SRB', 'SRC', 'SRF', 'SRT', 'SSB', 'SSC', 'SSF', 'SSG', 'SSH', 'SSI', 'SSM', 'SSN', 'ST8', 'STB', 'STC', 'STG', 'STH', 'STK', 'STL', 'STP', 'STS', 'STT', 'STW', 'SUM', 'SVC', 'SVD', 'SVG', 'SVH', 'SVI', 'SVN', 'SVT', 'SWC', 'SZB', 'SZC', 'SZE', 'SZG', 'SZL', 'TA3', 'TA6', 'TA9', 'TAG', 'TAN', 'TAR', 'TAW', 'TB8', 'TBC', 'TBD', 'TBH', 'TBR', 'TBT', 'TBX', 'TC6', 'TCB', 'TCD', 'TCH', 'TCI', 'TCJ', 'TCK', 'TCL', 'TCM', 'TCO', 'TCR', 'TCT', 'TCW', 'TDB', 'TDC', 'TDF', 'TDG', 'TDH', 'TDI', 'TDM', 'TDN', 'TDP', 'TDS', 'TDT', 'TDW', 'TED', 'TEG', 'TEL', 'TET', 'TFC', 'TGG', 'TGP', 'TH1', 'THB', 'THD', 'THG', 'THI', 'THN', 'THP', 'THS', 'THT', 'THU', 'THW', 'TID', 'TIE', 'TIG', 'TIN', 'TIP', 'TIS', 'TIX', 'TJC', 'TKA', 'TKC', 'TKG', 'TKU', 'TL4', 'TLD', 'TLG', 'TLH', 'TLI', 'TLP', 'TLT', 'TMB', 'TMC', 'TMG', 'TMP', 'TMS', 'TMT', 'TMW', 'TMX', 'TN1', 'TNA', 'TNB', 'TNC', 'TNG', 'TNH', 'TNI', 'TNM', 'TNP', 'TNS', 'TNT', 'TNW', 'TOP', 'TOS', 'TOT', 'TOW', 'TPB', 'TPC', 'TPH', 'TPP', 'TPS', 'TQN', 'TQW', 'TR1', 'TRA', 'TRC', 'TRS', 'TRT', 'TS3', 'TS4', 'TSB', 'TSC', 'TSD', 'TSG', 'TSJ', 'TST', 'TTA', 'TTB', 'TTC', 'TTD', 'TTE', 'TTF', 'TTG', 'TTH', 'TTL', 'TTN', 'TTP', 'TTS', 'TTT', 'TTZ', 'TUG', 'TV1', 'TV2', 'TV3', 'TV4', 'TV6', 'TVA', 'TVB', 'TVC', 'TVD', 'TVG', 'TVH', 'TVM', 'TVN', 'TVP', 'TVS', 'TVT', 'TVW', 'TW3', 'TXM', 'TYA', 'UCT', 'UDC', 'UDJ', 'UDL', 'UEM', 'UIC', 'UMC', 'UNI', 'UPC', 'UPH', 'USC', 'USD', 'V11', 'V12', 'V15', 'V21', 'VAB', 'VAF', 'VAT', 'VAV', 'VBB', 'VBC', 'VBG', 'VBH', 'VC1', 'VC2', 'VC3', 'VC5', 'VC6', 'VC7', 'VC9', 'VCA', 'VCB', 'VCC', 'VCE', 'VCF', 'VCG', 'VCI', 'VCM', 'VCP', 'VCR', 'VCS', 'VCT', 'VCW', 'VCX', 'VDB', 'VDL', 'VDN', 'VDP', 'VDS', 'VDT', 'VE1', 'VE2', 'VE3', 'VE4', 'VE8', 'VE9', 'VEA', 'VEC', 'VEF', 'VES', 'VET', 'VFC', 'VFG', 'VFR', 'VFS', 'VGC', 'VGG', 'VGI', 'VGL', 'VGP', 'VGR', 'VGS', 'VGT', 'VGV', 'VHC', 'VHD', 'VHE', 'VHF', 'VHG', 'VHH', 'VHL', 'VHM', 'VIB', 'VIC', 'VID', 'VIE', 'VIF', 'VIG', 'VIH', 'VIM', 'VIN', 'VIP', 'VIR', 'VIT', 'VIW', 'VIX', 'VJC', 'VKC', 'VKP', 'VLA', 'VLB', 'VLC', 'VLF', 'VLG', 'VLP', 'VLW', 'VMA', 'VMC', 'VMD', 'VMG', 'VMS', 'VMT', 'VNA', 'VNB', 'VNC', 'VND', 'VNE', 'VNF', 'VNG', 'VNH', 'VNI', 'VNL', 'VNM', 'VNP', 'VNR', 'VNS', 'VNT', 'VNX', 'VNY', 'VNZ', 'VOC', 'VOS', 'VPA', 'VPB', 'VPC', 'VPD', 'VPG', 'VPH', 'VPI', 'VPR', 'VPS', 'VPW', 'VQC', 'VRC', 'VRE', 'VRG', 'VSA', 'VSC', 'VSE', 'VSF', 'VSG', 'VSH', 'VSI', 'VSM', 'VSN', 'VST', 'VTA', 'VTB', 'VTC', 'VTD', 'VTE', 'VTG', 'VTH', 'VTI', 'VTJ', 'VTK', 'VTL', 'VTM', 'VTO', 'VTP', 'VTQ', 'VTR', 'VTS', 'VTV', 'VTX', 'VTZ', 'VUA', 'VVN', 'VVS', 'VW3', 'VWS', 'VXB', 'VXP', 'VXT', 'WCS', 'WSB', 'WSS', 'WTC', 'X20', 'X26', 'X77', 'XDC', 'XDH', 'XHC', 'XLV', 'XMC', 'XMD', 'XMP', 'XPH', 'YBC', 'YBM', 'YEG', 'YTC'
]

TYPE_LIST = ['PRICE_UPPER', 'PRICE_LOWER']

# Message
UNSUPPORTED_CONDITION_MSG = "Điều kiện không được hỗ trợ: " 
UNSUPPORTED_TICKER_MSG = "Mã chứng khoán không được hỗ trợ: "
NEGATIVE_THRESHOLD_MSG = "Hãy nhập số dương"
WELCOME_MESSAGE = """
Welcome to tudvFDP.

Bot này sẽ giúp bạn theo dõi giá những chỉ báo của những mã chứng khoán trên thị trường.
Bạn có thể tạo thông báo với bot này, và một khi điều kiện thõa mãn, chúng tôi sẽ gửi bạn một message.Thử tạo thông báo ngay bây giờ với /add.

Ngoài ra, bạn còn có thể xem được dữ liệu giá đóng cửa, giá các chỉ báo, hoặc là xem thông tin dự đoán giá chứng khoán cho ngày mai. Thử xem ngay với /viewdata và /predictdata

Nếu bạn cần giúp đỡ, nhập /help.
"""
HELP_MESSAGE = """
Danh sách các lệnh:

/add - thêm một điều kiện để nhận thông báo
/viewdata - xem được giá đóng cửa, giá các chỉ báo của các mã đăng ký
/update - cập nhật một điều kiện nhận thông báo đang tồn tại
/remove - xóa một điều kiện nhận thông báo
/list - xem tất cả các điều kiện nhận thông báo của bạn
/predictdata - xem giá dự đoán của các mã chứng khoán đăng ký
/cancel - xóa tất cả các điều kiện. 
"""
NO_CONDITION_MESSAGE = "Bạn chưa có một điều kiện nhận thông báo nào. Tạo ngay với /add"
NO_CONDITION_ON_TICKER_MESSAGE = "Bạn không có một điều kiện trên mã  %s. Tạo một điều kiện với /add \{ticker\} \{price_upper/price_lower\} \{threshold\}"

#db config

# mysql
mysql_host = 'localhost'
mysql_database = 'stockalert'
mysql_username = 'root'
mysql_password = 'tudv'
mysql_port = 3380

# apache druid
druid_host = 'localhost'
druid_port = 8082

# alert message
GT_MESSAGE = "Thông báo {}: {} đã trên ngưỡng của bạn {} %!!\nGiá hiện tại: {}"
LT_MESSAGE = "Thông báo {}: {} đã duới ngưỡng của bạn {} %!!\nGiá hiện tại: {}"

# attributes to set alerts on
ATTR_BUTTON = [["PRICE", "VOLUME"], ["OBV", "RSI"], ["MACD"]]
ATTR = ["PRICE", "VOLUME", "OBV", "RSI", "MACD"]
DIRECTION_BUTTON = [["less", "greater"]]
