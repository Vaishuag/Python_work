class Cuboid:
    def __init__(self,l,b,h):               
        self.len=l
        self.bre=b 
        self.hei=h 
    
    def l_area(self):
        return self.len*self.bre

    def t_area(self):
        return 2*(self.len*self.bre+self.bre*self.hei)   
    
    def volum(self):
        return self.len*self.bre*self.hei
c1=Cuboid(6,8,4)

print('lateral Area',c1.l_area())
print('Total surface area',c1.t_area())
print('Volumn',c1.volum())
                     









    #init : initialization , in cunstructor there is always be a one extar argu [self]