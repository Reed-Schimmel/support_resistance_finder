import numpy as np

class Sup_Res_Finder():
    def isSupport(self, df,i):
        support = df['Low'][i] < df['Low'][i-1]  and df['Low'][i] < df['Low'][i+1] \
        and df['Low'][i+1] < df['Low'][i+2] and df['Low'][i-1] < df['Low'][i-2]

        return support

    def isResistance(self, df,i):
        resistance = df['High'][i] > df['High'][i-1]  and df['High'][i] > df['High'][i+1] \
        and df['High'][i+1] > df['High'][i+2] and df['High'][i-1] > df['High'][i-2] 

        return resistance
        
    def find_levels(self, df):
        levels = []
        s =  np.mean(df['High'] - df['Low'])
        
        for i in range(2, df.shape[0]-2):
            if self.isSupport(df,i):
                l = df['Low'][i]
            
                if np.sum([abs(l-x) < s  for x in levels]) == 0:
                    levels.append((i,l))
            
            elif self.isResistance(df,i):
                l = df['High'][i]
            
                if np.sum([abs(l-x) < s  for x in levels]) == 0:
                    levels.append((i,l))
                    
        return levels
