class skolēni:
    def __init__(self, vārds, uzvārds, nav = False):
        self.vārds = vārds
        self.uzvārds = uzvārds
        
    def info(self):
        return f"{self.vārds} {self.uzvārds}"
    
class saraksts:
    def __init__(self):
        self.skolēni = []
        
    def pievienot_skolenu(self, skolēns):
        self.skolēni.append(skolēns)
        
    def paradit_visus(self):
        print("Skolēnu saraksts")
        for skolēns in self.skolēni:
            print(skolēns.info())
            
    def atrast_labako(self):
        if not self.skolēni:
            print("Saraksts ir tukšs")
            return
        labakais = max(self.skolēni, key=lambda s: s.videja_atzime)
        print("Labakais skolēns ir: {labakais.vārds} ar vidējo atzīmi {labakais.videja_atzime}")
        
if __name__ =="__main__":
    saraksts = SkolēnuSaraksts() 
    
    saraksts.pievienot_skolenu(skolēns=("Arturs", 15, 8,9))
    saraksts.pievienot_skolenu(skolēns=("Anna", 15, 9,3))
    saraksts.pievienot_skolenu(skolēns=("Maksims", 16, 6,7))