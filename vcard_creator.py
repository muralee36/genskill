import csv
def vcard(pat):
    fi=open(pat,encoding='utf-8')
    csv_list=list(csv.reader(fi))
    for i in csv_list:
        vcf(i)
def vcf(li):
    print(f"""BEGIN:VCARD
    VERSION:2.1
    N:{li[0]};{li[1]}
    FN:{li[1]} {li[0]}
    ORG:Authors, Inc.
    TITLE:{li[2]}
    TEL;WORK;VOICE:{li[3]}
    ADR;WORK:;;100 Flat Grape Dr.;Fresno;CA;95555;United States of America
    EMAIL;PREF;INTERNET;{li[4]}
    REV:20150922T195243Z
    END:VCARD""")
    
