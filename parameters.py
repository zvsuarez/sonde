
class Date:
    def __init__(self, date):
        self.date = date
        self.month_word = ['Jan',
                            'Feb', 
                            'Mar', 
                            'Apr', 
                            'May', 
                            'Jun', 
                            'Jul', 
                            'Aug',
                            'Sep',
                            'Oct',
                            'Nov',
                            'Dec']
        self.hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.month = date[4:6]
        self.day = date[6:8]
        self.year = date[0:4]
        self.utc = date[-4:]
        self.meridiem = ''

    def convert(self):
        if self.date == '/':
            return 'NA'
        if len(self.date) != 12:
            return 'Invalid'
        else:
            if int(self.utc[:2]) in range(4, 16):
                self.meridiem = 'PM'
            else:
                self.meridiem = 'AM'
            return f"{self.month_word[int(self.month) % 12-1]} {self.day} {self.year} {self.hour[((int(self.utc[:2]) + 8) % 12) - 1]}:{self.utc[2:]} {self.meridiem}"


class Code:
    def __init__(self, code):
        self.code = code

    def convert(self):
        return self.code


class Dateplus:
    def __init__(self, code):
        self.day = code[0:2]
        self.utc = code[2:4]
        self.lwr = code[-1]
        self.code = code

    def day_method(self):
        if not(self.day.isnumeric()):
            if '/' in self.day:
                return 'NA'
            else:
                return 'Invalid'
        if int(self.day) >= 82 or self.day == '00':
            return 'Invalid'
        if int(self.day) in range(32, 51):
            return 'Invalid'
        if int(self.day) in range(51, 82):
            return f'Day {int(self.day) - 50}'
        else:
            return f'Day {int(self.day)}'

    def utc_method(self):
        if not(self.utc.isnumeric()):
            if '/' in self.day:
                return 'NA'
            else:
                return 'Invalid'
        if int(self.utc) > 23:
            return 'Invalid'
        else:
            return f'{self.utc}:00 UTC'

    def lwr_method(self, code):
        temp = Code(code)
        if not(self.lwr.isnumeric()):
            if '/' in self.lwr:
                return 'NA'
            else:
                return 'Invalid'
        else:
            if temp.convert() == 'TTAA':
                return f'{self.lwr}00 mb'
            if temp.convert() == 'TTCC':
                return f'{self.lwr}0 mb'
            else:
                return 'NA'

    def convert(self, code):
        day_reading = self.day_method()
        utc_reading = self.utc_method()
        lwr_reading = self.lwr_method(code)

        if len(self.code) != 5:
            return 'Invalid'
        if not(self.code.isnumeric()):
            if '/' in self.code:
                return f'{day_reading} {utc_reading} {lwr_reading}'
            else:
                return 'Invalid'
        else:
            return f'{day_reading} {utc_reading} {lwr_reading}'

    def feedback(self):
        return self.day

#temp = Dateplus('13221')
#print(temp.convert('TTAA')) #.convert(Code(''))

class Temperature:
    def __init__(self, code):
        self.code = code
        self.temp = code[:3]
        self.dew_dep = code[3:]

    def convert_temp(self):
        if not(self.temp.isnumeric()):
            if '/' in self.temp:
                return 'NA'
            else:
                return 'Invalid'
        if int(self.temp[-1]) % 2 == 0:
            return str(int(self.temp)/10)
        else:
            return str(-int(self.temp)/10)

    def convert_ddep(self):
        if not(self.dew_dep.isnumeric()):
            if '/' in self.dew_dep:
                return 'NA'
            else:
                return 'Invalid'
        if int(self.dew_dep) in range(51, 56):
            return 'NA'
        if int(self.dew_dep) == 50:
            return str(5)
        if int(self.dew_dep) > 50:
            return str(int(self.dew_dep) - 50)
        else:
            return str(int(self.dew_dep) / 10)

    def convert_dtemp(self):
        t = self.convert_temp()
        dd = self.convert_ddep()

        if len(self.code) != 5:
            return 'Invalid'
        if not(self.code.isnumeric()):
            if '/' in self.code:
                return 'NA'
            else:
                return 'Invalid'
        if dd == 'NA':
            return 'NA'
        else:
            return f'{float(t)-float(dd):.2f}{chr(176)}'


class Wind:
    def __init__(self, code):
        self.code = code
        self.wind_dir = code[:3]
        self.wind_spd = code[3:]

    def cardinal_dir(self, value):
        dir_ind = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE','S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        ind = round(value / (360/len(dir_ind)))
        cardinal = dir_ind[ind % len(dir_ind)]
        return cardinal

    def convert(self, date):
        YY = Dateplus(date)
    
        if len(self.code) != 5:
            return 'Invalid'
        if not(self.code.isnumeric()):
            if '/' in self.wind_dir:
                return 'NA'
            if '/' in self.wind_spd:
                wind_car = self.cardinal_dir(int(self.wind_dir))
                if int(self.wind_dir) % 5 != 0:
                    return f"{int(self.wind_dir)-1}{chr(176)} {wind_car} NA"
                else:
                    return f"{self.wind_dir}{chr(176)} {wind_car} NA"
            else:
                return 'Invalid'
        if int(self.wind_dir) > 360:
            return 'OuR'    #Out of Range
        if int(self.wind_dir) % 5 != 0:
            wind_car = self.cardinal_dir(int(self.wind_dir))
            if int(YY.feedback()) > 50:
                return f"{int(self.wind_dir)-1}{chr(176)} {wind_car} {int(self.wind_spd) + 100} kt"
            else:
                return f"{int(self.wind_dir)-1}{chr(176)} {wind_car} {int(self.wind_spd) + 100} m/s"
        else:
            wind_car = self.cardinal_dir(int(self.wind_dir))
            if int(YY.feedback()) > 50:
                return f"{self.wind_dir}{chr(176)} {wind_car} {self.wind_spd} kt"
            else:
                return f"{self.wind_dir}{chr(176)} {wind_car} {self.wind_spd} m/s"

#wind = Wind('21034')
#print(wind.convert('13221')) #.convert(Dateplus(''))

class GeopotenheightA:
    def __init__(self, code):
        self.code = code
        self.geopressure = code[:2]
        self.geoheight = code[2:]
    
    def geopressure_convert(self):
        geopressure = [99, 1000, 925, 850, 700, 500, 400, 300, 250, 200, 150, 100, 88]
        if self.geopressure == '99':
            return geopressure[0]
        if self.geopressure == '00':
            return geopressure[1]
        elif self.geopressure == '92':
            return geopressure[2]
        elif self.geopressure == '85':
            return geopressure[3]
        elif self.geopressure == '70':
            return geopressure[4]
        elif self.geopressure == '50':
            return geopressure[5]
        elif self.geopressure == '40':
            return geopressure[6]
        elif self.geopressure == '30':
            return geopressure[-6]
        elif self.geopressure == '25':
            return geopressure[-5]
        elif self.geopressure == '20':
            return geopressure[-4]
        elif self.geopressure == '15':
            return geopressure[-3]
        elif self.geopressure == '10':
            return geopressure[-2]
        elif self.geopressure == '88':
            return geopressure[-1]
        else:
            return 'NA'

    def convert_altitude(self):
        geopressure = self.geopressure_convert()

        if len(self.code) != 5:
            return "Invalid"
        if not(self.code.isnumeric()):
            if '/' in self.geopressure:
                return 'NA'
            if '/' in self.geoheight:
                if geopressure == 99:
                    return 'Surface'
                if geopressure == 88:
                    return 'Tropopause'
                else:
                    return 'NA'
            else:
                return 'Invalid'
        if geopressure == 99:
            return 'Surface'
        if geopressure == 1000:
            if int(self.geoheight) >= 500:
                return f'-{int(self.geoheight)-500} m'
            else:
                return f'{int(self.geoheight)} m'
        if geopressure == 925:
            return f'{self.geoheight} m'
        if geopressure == 850:
            return f'1,{self.geoheight} m'
        if geopressure == 700:
            if int(self.geoheight) >= 500:
                return f'2,{self.geoheight} m'
            else:
                return f'3,{self.geoheight} m'
        if geopressure == 500 or geopressure == 400 or geopressure == 300:
            return f'{int(self.geoheight)}0 m'
        if geopressure == 250 or geopressure == 200 or geopressure == 150 or geopressure == 100:
            return f'1{self.geoheight}0 m'
        if geopressure == 88:
            return 'Tropopause'
        else:
            return 'NA'

    def convert_pressure(self):
        geopressure = self.geopressure_convert()
        if len(self.code) != 5:
            return "Invalid"
        if not(self.code.isnumeric()):
            if '/' in self.geoheight:
                if geopressure == 99 or geopressure == 88:
                    return 'NA'
                else:
                    return f'{geopressure} mb'
            else:
                return 'NA'
        if geopressure == 'NA':
            return 'NA'
        if self.geopressure == '99':
            if self.code[2] == '0':
                return f"1{self.code[2:]} mb"
            else:
                return f"{self.code[2:]} mb"
        if self.geopressure == '88':
            if self.code[2:] == '999':
                return 'NA'
            else:
                return f'{self.code[2:]} mb'
        else:
            return f'{geopressure} mb'


class Maxwindlevel:
    def __init__(self, code):
        self.code = code
        self.indicator = code[:2]
        self.pressure = code[2:]

    def convert(self):
        if len(self.code) != 5:
            return 'Invalid'
        if not(self.code.isnumeric()):
            if '/' in self.code:
                return 'NA'
            else:
                return 'Invalid'
        if self.indicator != '77' and self.indicator != '66':
                return 'Invalid'
        if self.code == '77999':
            return 'NA'
        else:
            if self.indicator == '77':
                return f'{self.pressure} mb\n!Level'
            if self.indicator == '66':
                return f'{self.pressure} mb\n=Wspd-Hi'


class Windshear:
    def __init__(self, code):
        self.code = code
        self.indicator = code[0:1]
        self.below = code[1:3]
        self.above = code[3:]

    def shear_below(self):
        if not(self.below.isnumeric()):
            if '/' in self.below:
                return 'NA'
            else:
                return 'Invalid'
        else:
            return f'{self.below} kt'

    def shear_above(self):
        if not(self.above.isnumeric()):
            if '/' in self.above:
                return 'NA'
            else:
                return 'Invalid'
        else:
            return f'{self.above} kt'

    def convert(self):
        below = self.shear_below()
        above = self.shear_above()

        if len(self.code) != 5:
            return 'Invalid'
        if not(self.code.isnumeric()):
            if '/' in self.indicator:
                return 'NA'
            if '/' in self.below or '/' in self.above:
                return f'{below}\n{above}'
            else:
                return 'Invalid'
        if self.indicator != '4':
            return 'Invalid'
        else:
            return f'{below}\n{above}'


class Seasurface:
    def __init__(self, code):
        self.code = code
        self.system = code[:5]
        self.solinfra = code[0]
        self.radsys = code[1:3]
        self.tracksys = code[3:5]
        self.utc = code[6:]
        self.utc_h = code[7:9]
        self.utc_m = code[9:]

    def solar_reading(self):
        solar_text = ['NoC', 'CIMOsol+inf', 'CIMOsol/inf', 'CIMOsol', 'RADsol+inf', 'RADsol', 'COUsol+inf', 'COUsol', 'ReS', 'NA', 'Invalid']

        if not(self.solinfra.isnumeric()):
            if self.solinfra == '/':
                return solar_text[-2]
            else:
                return solar_text[-1]
        if self.solinfra == '0':
            return solar_text[0]
        if self.solinfra == '1':
            return solar_text[1]
        if self.solinfra == '2':
            return solar_text[2]
        if self.solinfra == '3':
            return solar_text[3]
        if self.solinfra == '4':
            return solar_text[4]
        if self.solinfra == '5':
            return solar_text[5]
        if self.solinfra == '6':
            return solar_text[6]
        if self.solinfra == '7':
            return solar_text[7]
        if int(self.solinfra) in range(8-14):
            return solar_text[-3]
        if self.solinfra == '15':
            return solar_text[-2]
        else:
            return solar_text[-2]

    def rad_reading(self):
        rad_text = ['ReS', 'NoRAD/PTar', 'NoRAD/ATar', 'NoRAD/Pthp', 'NoRAD/Athp', 'NoRAD/radac', 'NoRAD/ReS', 'NoRAD/unk', 'RSVIZAp-c', 'RSVIZBt-c', 'RSSDC', 'Astor', 'VIZMrkI', 'EEC-T23', 'Elin', 'GrawG', 'ReS/radalloc', 'GrawM60', 'IMSMK3', 'VIZJYMrkI', 'MeiRS2-80', 'Mes1950A', 'Mes1945A', 'MesMH73A', 'MetLabor', 'AVK-MRZ', 'MetMarz2-1', 'MetMarz2-2', 'OkiRS2-80', 'VIZValAp-c', 'Shanghairad', 'UKMOMK3', 'Vino', 'VaiRS18', 'VaiRS21', 'VaiRS80', 'VIZLoran-C', 'SprE076', 'SprE084', 'SprE085', 'SprE086', 'AIR-1680', 'AIR-1680x', 'RSMSS', 'AIR-403', 'MeiRS2-91', 'Valcom', 'VIZMrkII', 'Graw-90', 'VIZB2', 'VaiRS8057', 'VaiRS80mc', 'VaiRS80dc', 'VaiRS80pc', 'VaiRS80star', 'OrbitalSC', 'VIZtr1499', 'ReS/auto+', 'RADpr', 'RADprtr', 'RADprrr', 'RADtr', 'RADrr', 'RADdes', 'ReS/radinc', 'NA', 'Invalid']

        if not(self.radsys.isnumeric()):
            if '/' in self.radsys:
                return rad_text[-2]
            else:
                return rad_text[-1]
        if self.radsys == '00' or self.radsys =='01':
            return rad_text[0]
        if self.radsys == '02':
            return rad_text[1]
        if self.radsys == '03':
            return rad_text[2]
        if self.radsys == '04':
            return rad_text[3]
        if self.radsys == '05':
            return rad_text[4]
        if self.radsys == '06':
            return rad_text[5]
        if self.radsys == '07' or self.radsys == '08':
            return rad_text[6]
        if self.radsys == '09':
            return rad_text[7]
        if self.radsys == '10':
            return rad_text[8]
        if self.radsys == '11':
            return rad_text[9]
        if self.radsys == '12':
            return rad_text[10]
        if self.radsys == '13':
            return rad_text[11]
        if self.radsys == '14':
            return rad_text[12]
        if self.radsys == '15':
            return rad_text[13]
        if self.radsys == '16':
            return rad_text[14]
        if self.radsys == '17':
            return rad_text[15]
        if self.radsys == '18':
            return rad_text[16]
        if self.radsys == '19':
            return rad_text[17]
        if self.radsys == '20':
            return rad_text[18]
        if self.radsys == '21':
            return rad_text[19]
        if self.radsys == '22':
            return rad_text[20]
        if self.radsys == '23':
            return rad_text[21]
        if self.radsys == '24':
            return rad_text[22]
        if self.radsys == '25':
            return rad_text[23]
        if self.radsys == '26':
            return rad_text[24]
        if self.radsys == '27':
            return rad_text[25]
        if self.radsys == '28':
            return rad_text[26]
        if self.radsys == '29':
            return rad_text[27]
        if self.radsys == '30':
            return rad_text[28]
        if self.radsys == '31':
            return rad_text[29]
        if self.radsys == '32':
            return rad_text[30]
        if self.radsys == '33':
            return rad_text[31]
        if self.radsys == '34':
            return rad_text[32]
        if self.radsys == '35':
            return rad_text[33]
        if self.radsys == '36':
            return rad_text[34]
        if self.radsys == '37':
            return rad_text[35]
        if self.radsys == '38':
            return rad_text[36]
        if self.radsys == '39':
            return rad_text[37]
        if self.radsys == '40':
            return rad_text[38]
        if self.radsys == '41':
            return rad_text[39]
        if self.radsys == '42':
            return rad_text[40]
        if self.radsys == '43':
            return rad_text[41]
        if self.radsys == '44':
            return rad_text[42]
        if self.radsys == '45':
            return rad_text[43]
        if self.radsys == '46':
            return rad_text[44]
        if self.radsys == '47':
            return rad_text[45]
        if self.radsys == '48':
            return rad_text[46]
        if self.radsys == '49':
            return rad_text[47]
        if self.radsys == '50':
            return rad_text[48]
        if self.radsys == '51':
            return rad_text[49]
        if self.radsys == '52':
            return rad_text[50]
        if int(self.radsys) in range(53, 60):
            return rad_text[16]
        if self.radsys == '60':
            return rad_text[51]
        if self.radsys == '61':
            return rad_text[52]
        if self.radsys == '62':
            return rad_text[53]
        if self.radsys == '63':
            return rad_text[54]
        if self.radsys == '64':
            return rad_text[55]
        if self.radsys == '65':
            return rad_text[56]
        if int(self.radsys) in range(66, 90):
            return rad_text[-10]
        if self.radsys == '90':
            return rad_text[7]
        if self.radsys == '91':
            return rad_text[-9]
        if self.radsys == '92':
            return rad_text[-8]
        if self.radsys == '93':
            return rad_text[-7]
        if self.radsys == '94':
            return rad_text[-6]
        if self.radsys == '95':
            return rad_text[-5]
        if self.radsys == '96':
            return rad_text[-4]
        if int(self.radsys) in range(97, 100):
            return rad_text[-3]
        else:
            return rad_text[-2]

    def track_reading(self):
        track_text = ['NoWF', 'AuxODF', 'AuxRDF', 'AuxRange', 'NA', 'VLF-Omega', 'Loran-C', 'AuxWProf','SatNav', 'ReS', 'Invalid']

        if not(self.tracksys.isnumeric()):
            if '/' in self.tracksys:
                return track_text[4]
            else:
                return track_text[-1]
        if self.tracksys == '00':
            return track_text[0]
        if self.tracksys == '01':
            return track_text[1]
        if self.tracksys == '02':
            return track_text[2]
        if self.tracksys == '03':
            return track_text[3]
        if self.tracksys == '05':
            return track_text[5]
        if self.tracksys == '06':
            return track_text[-5]
        if self.tracksys == '07':
            return track_text[-4]
        if self.tracksys == '08':
            return track_text[-3]
        if int(self.tracksys) in range(9, 19):
            return track_text[-2]
        else:
            return track_text[4]

    def utc_reading(self):
        if len(self.utc) != 5:
            return 'Invalid'
        if not(self.utc.isnumeric()):
            if '/' in self.utc:
                return 'NA'
            else:
                return 'Invalid'
        if self.utc[0] != '8':
            return 'Invalid'
        if int(self.utc_h) > 23 or int(self.utc_m) > 59:
            return 'Invalid'
        else:
            return f'{self.utc_h}:{self.utc_m}'

    def convert(self):
        solar_data = self.solar_reading()
        rad_data = self.rad_reading()
        track_data = self.track_reading()
        utc_data = self.utc_reading()

        if len(self.system) != 5 or len(self.utc) != 5:
            return 'Invalid'
        if not(self.system.isnumeric()) or not(self.utc.isnumeric()):
            if '/' in self.system or '/' in self.utc:
                return f'{solar_data} {rad_data} {track_data} {utc_data}'
            else:
                return 'Invalid'
        else:
            return f'{solar_data} {rad_data} {track_data} {utc_data}'


class Cloud:
    def __init__(self, code):
        self.code = code
        self.indicator = code[:5]
        self.cloud = code[6:]
        self.nh = code[6:7]
        self.cl = code[7:8]
        self.h = code[8:9]
        self.cm = code[9:10]
        self.ch = code[10:]

    def cloud_amount(self):
        if not(self.nh.isnumeric()):
            if self.nh == '/':
                return 'Indisc'
            else:
                return 'Invalid'
        if self.nh == '1':
            return f'{self.nh} okta'
        if int(self.nh) in range(2, 10):
            if int(self.nh) == 9:
                return 'Obscure'
            else:
                return f'{self.nh} oktas'
        else:
            return 'Invalid'

    def cloud_low(self):
        if not(self.cl.isnumeric()):
            if self.cl == '/':
                return 'Invis'
            else:
                return 'Invalid'
        if self.cl == '0':
            return 'Cl/None'
        if self.cl == '1':
            return 'Cml/HumFra'
        if self.cl == '2':
            return 'CmlStrat/MedCon'
        if self.cl == '3':
            return 'CmlStrat/Cal'
        if self.cl == '4':
            return 'Strat/CmlGen'
        if self.cl == '5':
            return 'Strat/Cml'
        if self.cl == '6':
            return 'Strat/NebFra'
        if self.cl == '7':
            return 'Strat/CmlFra'
        if self.cl == '8':
            return 'Cml/StratCml'
        if self.cl == '9':
            return 'CmlNim/Cap'
        else:
            return 'Invalid'

    def cloud_middle(self):
        if not(self.cm.isnumeric()):
            if self.cm == '/':
                return 'Invis'
            else:
                return 'Invalid'
        if self.cm == '0':
            return 'Cm/None'
        if self.cm == '1':
            return 'AltStrat/Trans'
        if self.cm == '2':
            return 'AltStrat/OpaNim'
        if self.cm == '3':
            return 'AltCml/Trans'
        if self.cm == '4':
            return 'AltCmlP/Trans'
        if self.cm == '5':
            return 'AltCmlB/TransS'
        if self.cm == '6':
            return 'AltCml/CmlGen'
        if self.cm == '7':
            return 'AltCml/TransM'
        if self.cm == '8':
            return 'AltCml/CasFlo'
        if self.cm == '9':
            return 'AltCml/Chaos'
        else:
            return 'Invalid'
    
    def cloud_high(self):
        if not(self.ch.isnumeric()):
            if self.ch == '/':
                return 'Invis'
            else:
                return 'Invalid'
        if self.ch == '0':
            return 'Ch/None'
        if self.ch == '1':
            return 'CirNPi/FibUnc'
        if self.ch == '2':
            return 'Cir/Spi'
        if self.ch == '3':
            return 'CirSpi/CmlNimGen'
        if self.ch == '4':
            return 'CirPi/FibUnc'
        if self.ch == '5':
            return f'Cir/CirStrat<45{chr(176)}'
        if self.ch == '6':
            return f'Cir/CirStrat>45{chr(176)}'
        if self.ch == '7':
            return 'CirStrat'
        if self.ch == '8':
            return 'CirStratNPi'
        if self.ch == '9':
            return 'CirCml'
        else:
            return 'Invalid'

    def height(self):
        if not(self.h.isnumeric()):
            if self.h == '/':
                return 'NA'
            else:
                return 'Invalid'
        if self.h == '0':
            return '0-50m'
        if self.h == '1':
            return '50-100m'
        if self.h == '2':
            return '100-200m'
        if self.h == '3':
            return '200-300m'
        if self.h == '4':
            return '300-600m'
        if self.h == '5':
            return '600-1000m'
        if self.h == '6':
            return '1000-1500m'
        if self.h == '7':
            return '1500-2000m'
        if self.h == '8':
            return '2000-2500m'
        if self.h == '9':
            return '2500m-/Cnone'
        else:
            'Invalid'
        
    def convert(self):
        nh_reading = self.cloud_amount()
        cl_reading = self.cloud_low()
        cm_reading = self.cloud_middle()
        ch_reading = self.cloud_high()
        h = self.height()

        if len(self.indicator) != 5 or len(self.cloud) != 5:
            return 'Invalid'
        if not(self.indicator.isnumeric()) or not(self.cloud.isnumeric()):
            if '/' in self.indicator:
                return 'NA'
            if '/' in self.cloud:
                return f'{nh_reading} {cl_reading} {h} {cm_reading} {ch_reading}'
            else:
                return 'Invalid'
        if self.indicator != '41414':
            return 'Invalid'
        else:
            return f'{nh_reading} {cl_reading} {h} {cm_reading} {ch_reading}'


class GeopotenheightC:
    def __init__(self, code):
        self.code = code
        self.geopressure = code[:2]
        self.geoheight = code[2:]

    def geopressure_convert(self):
        geopressure = [99, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1, 88]
        if self.geopressure == '99':
            return geopressure[0]
        if self.geopressure == '70':
            return geopressure[1]
        elif self.geopressure == '50':
            return geopressure[2]
        elif self.geopressure == '30':
            return geopressure[3]
        elif self.geopressure == '20':
            return geopressure[4]
        elif self.geopressure == '10':
            return geopressure[5]
        elif self.geopressure == '07':
            return geopressure[6]
        elif self.geopressure == '05':
            return geopressure[7]
        elif self.geopressure == '03':
            return geopressure[-4]
        elif self.geopressure == '02':
            return geopressure[-3]
        elif self.geopressure == '01':
            return geopressure[-2]
        elif self.geopressure == '88':
            return geopressure[-1]
        else:
            return 'NA'

    def convert_altitude(self):
        geopressure = self.geopressure_convert()

        if len(self.code) != 5:
            return "Invalid"
        if not(self.code.isnumeric()):
            if '/' in self.geopressure:
                return 'NA'
            if '/' in self.geoheight:
                if geopressure == 99:
                    return 'Surface'
                if geopressure == 88:
                    return 'Tropopause'
                else:
                    return 'NA'
            else:
                return 'Invalid'
        if geopressure == 99:
            return 'Surface'
        if geopressure == 70:
            return f'18,{self.geoheight} m'
        if geopressure == 50:
            return f'20,{self.geoheight} m'
        if geopressure == 30:
            return f'23,{self.geoheight} m'
        if geopressure == 20:
            return f'26,{self.geoheight} m'
        if geopressure == 10:
            if int(self.geoheight) >= 500:
                return f'30,{self.geoheight} m'
            else:
                return f'31,{self.geoheight} m'
        if geopressure == 7:
            return f'33,{self.geoheight} m'
        if geopressure == 5:
            return f'35,{self.geoheight} m'
        if geopressure == 3:
            return f'39,{self.geoheight} m'
        if geopressure == 2:
            return f'42,{self.geoheight} m'
        if geopressure == 1:
            return f'47,{self.geoheight} m'
        if geopressure == 88:
            return 'Tropopause'
        else:
            return 'NA'

    def convert_pressure(self):
        geopressure = self.geopressure_convert()
        if len(self.code) != 5:
            return 'Invalid'
        if not(self.code.isnumeric()):
            if '/' in self.geoheight:
                if geopressure == 99 or geopressure == 88:
                    return 'NA'
                else:
                    return f'{geopressure} mb'
            else:
                return 'NA'
        if geopressure == 'NA':
            return 'NA'
        if self.geopressure == '99':
            if self.code[2] == '0':
                return f"1{self.code[2:]} mb"
            else:
                return f"{self.code[2:]} mb"
        if self.geopressure == '88':
            if self.code[2:] == '999':
                return 'NA'
            else:
                return f'{self.code[2:]} mb'
        else:
            return f'{geopressure} mb'


class SigLevelsBB:
    def __init__(self, code):
        self.code = code
        self.stat_lvl = code[:2]
        self.pressure = code[2:5]
        self.temp = code[6:]

    def convert_lvl(self):
        if len(self.code) != 5:
            return 'Invalid'
        if not(self.stat_lvl.isnumeric()):
            if '/' in self.stat_lvl:
                return 'NA'
            else:
                return 'Invalid'
        if self.stat_lvl == '00':
            return 'Station'
        else:
            return self.stat_lvl

    def convert_pressure(self):
        if len(self.code) != 5:
            return 'Invalid'
        if not(self.pressure.isnumeric()):
            if '/' in self.pressure:
                return 'NA'
            else:
                return 'Invalid'
        if self.pressure[0] == '0':
            return f'1{self.pressure} mb'
        else:
            return f'{self.pressure} mb'


class SigLevelsDD:
    def __init__(self, code):
        self.code = code
        self.stat_lvl = code[:2]
        self.pressure = code[2:5]
        self.temp = code[6:]

    def convert_lvl(self):
        if len(self.code) != 5:
            return 'Invalid'
        if not(self.stat_lvl.isnumeric()):
            if '/' in self.stat_lvl:
                return 'NA'
            else:
                return 'Invalid'
        if self.stat_lvl == '00':
            return 'Station'
        else:
            return self.stat_lvl

    def convert_pressure(self):
        if len(self.code) != 5:
            return 'Invalid'
        if not(self.pressure.isnumeric()):
            if '/' in self.pressure:
                return 'NA'
            else:
                return 'Invalid'
        #if self.pressure[0] == '0':
            #return f'1{self.pressure} mb'
        if self.stat_lvl == '00':
            if self.pressure[0] == '0':
                return f'1,{self.pressure} mb'
            else:
                return f'{self.pressure} mb'
        else:
            if self.pressure[0] == '0':
                return f'{(1000+int(self.pressure))} mb'
            else:
                return f'{int(self.pressure)} mb'


class Dateminus:
    def __init__(self, code):
        self.code = code

    def __init__(self, code):
        self.day = code[0:2]
        self.utc = code[2:4]
        self.tme = code[-1]
        self.code = code

    def day_method(self):
        if not(self.day.isnumeric()):
            if '/' in self.day:
                return 'NA'
            else:
                return 'Invalid'
        if int(self.day) >= 82 or self.day == '00':
            return 'Invalid'
        if int(self.day) in range(32, 51):
            return 'Invalid'
        if int(self.day) in range(51, 82):
            return f'Day {int(self.day) - 50}'
        else:
            return f'Day {int(self.day)}'

    def utc_method(self):
        if not(self.utc.isnumeric()):
            if '/' in self.day:
                return 'NA'
            else:
                return 'Invalid'
        if int(self.utc) > 23:
            return 'Invalid'
        else:
            return f'{self.utc}:00 UTC'

    def tme_method(self):
        equip = ['P/WME', 'Opttheo', 'Radtheo', 'Radar', 'Pf/WME', 'Omega', 'Loran-C', 'WindProf', 'SatNav', 'ReS']
        
        if not(self.lwr.isnumeric()):
            if '/' in self.lwr:
                return 'NA'
            else:
                return 'Invalid'
        if self.tme == '0':
            return equip[0]
        elif self.tme == '1':
            return equip[1]
        elif self.tme == '2':
            return equip[2]
        elif self.tme == '3':
            return equip[3]
        elif self.tme == '4':
            return equip[4]
        elif self.tme == '5':
            return equip[-5]
        elif self.tme == '6':
            return equip[-4]
        elif self.tme == '7':
            return equip[-3]
        elif self.tme == '8':
            return equip[-2]
        elif self.tme == '9':
            return equip[-1]
        else:
            return 'NA'

    def convert(self):
        day_reading = self.day_method()
        utc_reading = self.utc_method()
        tme_reading = self.tme_method()

        if len(self.code) != 5:
            return 'Invalid'
        if not(self.code.isnumeric()):
            if '/' in self.code:
                return f'{day_reading} {utc_reading} {tme_reading}'
            else:
                return 'Invalid'
        else:
            return f'{day_reading} {utc_reading} {tme_reading}'

    def feedback(self):
        return self.day


class Isobar:
    def __init__(self, code):
        self.code = code
        self.indicator = code[:2]
        self.n_isobar = code[2]
        self.pressure = code[3:]
    
    def convert_isobar(self):
        isobars = [850, 700, 500, 400, 300, 250, 200, 150, 100]
        
        if self.pressure == '85':
            return f'{isobars[0]} mb'
        elif self.pressure == '70':
            return f'{isobars[1]} mb'
        elif self.pressure == '50':
            return f'{isobars[2]} mb'
        elif self.pressure == '40':
            return f'{isobars[3]} mb'
        elif self.pressure == '30':
            return f'{isobars[4]} mb'
        elif self.pressure == '25':
            return f'{isobars[-4]} mb'
        elif self.pressure == '20':
            return f'{isobars[-3]} mb'
        elif self.pressure == '15':
            return f'{isobars[-2]} mb'
        elif self.pressure == '10':
            return f'{isobars[-1]} mb'
        else:
            return 'NA'

    def convert_n_iso(self):
        return self.n_isobar

#data = Isobar('55385')
#print(data.convert_n_iso())
#print(data.convert_isobar())

