
class Liftedindex:
    def __init__(self, code):
        self.indicator = code[:5]
        self.index = code[6:]
        self.value = code[9:]

    def convert(self):

        if len(self.indicator) != 5 or len(self.index) != 5:
            return 'Invalid'
        if not(self.indicator.isnumeric()) or not(self.index.isnumeric()):
            if '/' in self.indicator or '/' in self.index:
                return 'NA'
            else:
                return 'Invalid'
        if self.indicator != '10164':
            return 'Invalid'
        if self.index[:3] != '000':
            return 'Invalid'
        else:
            if int(self.value) in range(0, 41):
                return f'{self.value}'
            if int(self.value) in range(51, 91):
                return f'-{(int(self.value)-50)}'
            if int(self.value) == 91:
                return 'RH<20%\nCalcF'
            if int(self.value) == 92:
                return 'RHmiss\nbase'

#lifted = Liftedindex('10164 00092')
#print(lifted.convert())

class Meanwindlevel:
    def __init__(self, code):
        self.indicator = code[:5]
        self.group1 = code[6:11]
        self.group2 = code[12:]

    def convert(self):
        if len(self.indicator) != 5 or len(self.group1) != 5 or len(self.group2) != 5:
            return 'Invalid'
        if not(self.indicator.isnumeric()) or not(self.group1.isnumeric()) or not(self.group2.isnumeric()):
            if '/' in self.indicator:
                return 'NA'
            if '/' in self.group1 or '/' in self.group2:
                return f'{Wind(self.group1).convert()}\n{Wind(self.group2).convert()}'
            else:
                return 'Invalid'
        if self.indicator != '10194':
            return 'Invalid'
        else:
            return f'{Wind(self.group1).convert()}\n{Wind(self.group2).convert()}'

#mean = Meanwindlevel('10194 33222 22024')
#print(mean.convert())

'''
class Regionalcode:
    def __init__(self, code):
        self.code = code
        self.indicator = code[:5]
        self.additional = code[6:]

    def convert(self):
        pass

class Nationalcode:
    def __init__(self, code):
        self.code = code
    
    def convert(self):
        pass
'''

class AddInfo:
    def __init__(self, code):
        self.indicator = code[:5]
        self.group1 = code[6:11]
        self.stat_lvl = code[6:8]
        self.pressure = code[8:11]
        self.wind = code[12:]

    def group1_read(self):
        if len(self.group1) != 5:
            return 'Invalid'
        if not(self.group1.isnumeric()):
            if '/' in self.group1:
                return 'NA'
            else:
                return 'Invalid'
        if self.pressure[0] == '0':
            return f'1{self.pressure} mb'
        else:
            return f'{self.pressure} mb'


    def convert(self):
        group1_data = self.group1_read()
        if len(self.indicator) != 5 or len(self.group1) != 5 or len(self.wind) != 5:
            return 'Invalid'
        if not(self.indicator.isnumeric()) or not(self.group1.isnumeric()) or not(self.wind.isnumeric()):
            if '/' in self.indicator:
                return 'NA'
            if '/' in group1_data or self.wind:
                return f'{group1_data}\n{Wind(self.wind).convert()}'
            else:
                return 'Invalid'
        if self.indicator != '21212':
            return 'Invalid'
        else:
            return f'{group1_data}\n{Wind(self.wind).convert()}'

#add = AddInfo('21212 00009 09004')
#print(add.convert())