#-*- coding: utf-8 -*-
from compo.models import Trader, Company, TraderForm
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse

from tickerparse import tickerparse
from stockgetter import netfonds_price
from models import Company, CompanyManager
ticker_pair = [['ABG Sundal Collier Holding', 'ASC'], ['AF Gruppen', 'AFG'], ['AGR Group', 'AGR'], ['AKVA Group', 'AKVA'], ['Acta Holding', 'ACTA'], ['Aker', 'AKER'], ['Aker BioMarine', 'AKBM'], ['Aker Seafoods', 'AKS'], ['Aker Solutions', 'AKSO'], ['Algeta', 'ALGETA'], ['American Shipping Company', 'AMSC'], ['Apptix', 'APP'], ['Archer ', 'ARCHER'], ['Arendals Fossekompani', 'AFK'], ['Atea', 'ATEA'], ['Aurskog Sparebank', 'AURG'], ['Austevoll Seafood', 'AUSS'], ['Avocet Mining', 'AVM'], ['BW Offshore Limited', 'BWO'], ['BWG Homes', 'BWG'], ['Bakkafrost', 'BAKKA'], ['Belships', 'BEL'], ['Bergen Group', 'BERGEN'], ['Bionor Pharma ', 'BIONOR'], ['Biotec Pharmacon', 'BIOTEC'], ['Birdstep Technology', 'BIRD'], ['Blom', 'BLO'], ['Bonheur', 'BON'], ['Borgestad', 'BOR'], ['Bouvet', 'BOUVET'], ['Byggma', 'BMA'], ['Cermaq', 'CEQ'], ['Clavis Pharma', 'CLAVIS'], ['Codfarmers', 'COD'], ['Comrod Communication', 'COMROD'], ['ContextVision', 'COV'], ['Copeinca', 'COP'], ['DNB', 'DNB'], ['DNB OBX', 'OBXEDNB'], ['DNB OBX Derivat BULL', 'OBXEDDBULL'], ['DNB OBX Derivat Bear', 'OBXEDDBEAR'], ['DNO International', 'DNO'], ['DOF', 'DOF'], ['Data Respons', 'DAT'], ['Deep Sea Supply', 'DESSC'], ['Det norske oljeselskap', 'DETNOR'], ['DiaGenic', 'DIAG'], ['Dockwise', 'DOCK'], ['Dolphin Group ', 'DOLP'], ['Domstein', 'DOM'], ['EOC', 'EOC'], ['EVRY', 'EVRY'], ['Eidesvik Offshore', 'EIOF'], ['Eitzen Chemical', 'ECHEM'], ['Eitzen Maritime Services', 'EMS'], ['Ekornes', 'EKO'], ['Electromagnetic Geoservices', 'EMGS'], ['Eltek', 'ELT'], ['Fairstar Heavy Transport', 'FAIR'], ['Fara', 'FARA'], ['Farstad Shipping', 'FAR'], ['Fred. Olsen Energy', 'FOE'], ['Fred. Olsen Production', 'FOP'], ['Frontline', 'FRO'], ['Funcom', 'FUNCOM'], ['GC Rieber Shipping', 'RISH'], ['Ganger Rolf', 'GRO'], ['Gjensidige Forsikring ', 'GJF'], ['Golden Ocean Group', 'GOGL'], ['Goodtech', 'GOD'], ['Grieg Seafood', 'GSF'], ['Gyldendal', 'GYL'], ['Hafslund ser. A', 'HNA'], ['Hafslund ser. B', 'HNB'], ['Havila Shipping', 'HAVI'], ['Helgeland Sparebank', 'HELG'], ['Hexagon Composites', 'HEX'], ['Hol Sparebank', 'HOLG'], ['Hurtigruten', 'HRG'], ['Høegh LNG Holdings', 'HLNG'], ['Høland og Setskog Sparebank', 'HSPG'], ['I.M. Skaugen', 'IMSK'], ['IGE Resources ', 'IGE'], ['Imarex', 'IMAREX'], ['Indre Sogn Sparebank', 'ISSG'], ['Infratek', 'INFRA'], ['InterOil Exploration and Production', 'IOX'], ['Intex Resources', 'ITX'], ['Itera ', 'ITE'], ['Jason Shipping', 'JSHIP'], ['Jinhui Shipping and Transportation', 'JIN'], ['Kitron', 'KIT'], ['Klepp Sparebank', 'KLEG'], ['Kongsberg Automotive Holding', 'KOA'], ['Kongsberg Gruppen', 'KOG'], ['Kværner', 'KVAER'], ['Lerøy Seafood Group', 'LSG'], ['Marine Harvest', 'MHG'], ['Medistim', 'MEDI'], ['Melhus Sparebank', 'MELG'], ['Morpol ', 'MORPOL'], ['Namsos Trafikkselskap', 'NAM'], ['Navamedic', 'NAVA'], ['Nes Prestegjelds Sparebank', 'NESG'], ['Nio', 'NIO'], ['Norda', 'NORD'], ['Nordic Semiconductor', 'NOD'], ['Norse Energy Corp.', 'NEC'], ['Norsk Hydro', 'NHY'], ['Norske Skogindustrier', 'NSG'], ['Northern Logistic Property', 'NLPR'], ['Northern Offshore', 'NOF'], ['Northland Resources', 'NAUR'], ['Norway Pelagic', 'NPEL'], ['Norway Royal Salmon ', 'NRS'], ['Norwegian Air Shuttle', 'NAS'], ['Norwegian Car Carriers', 'NOCC'], ['Norwegian Energy Company', 'NOR'], ['Norwegian Property', 'NPRO'], ['Oceanteam Shipping', 'OTS'], ['Odfjell ser. A', 'ODF'], ['Odfjell ser. B', 'ODFB'], ['Olav Thon Eiendomsselskap', 'OLT'], ['Opera Software', 'OPERA'], ['Orkla', 'ORK'], ['PSI Group', 'PSI'], ['Panoro Energy', 'PEN'], ['Petroleum Geo-Services', 'PGS'], ['Petrolia ', 'PDR'], ['Photocure', 'PHO'], ['Polarcus', 'PLCS'], ['Polaris Media', 'POL'], ['Pronova BioPharma', 'PRON'], ['Prosafe', 'PRS'], ['Protector Forsikring', 'PROTCT'], ['Q-Free', 'QFR'], ['Questerre Energy Corporation', 'QEC'], ['Renewable Energy Corporation', 'REC'], ['Repant', 'REPANT'], ['Reservoir Exploration Technology', 'RXT'], ['Rieber & Søn', 'RIE'], ['Rocksource', 'RGT'], ['Royal Caribbean Cruises', 'RCL'], ['SAS AB', 'SAS-NOK'], ['SalMar', 'SALM'], ['Sandnes Sparebank', 'SADG'], ['Scana Industrier', 'SCI'], ['Schibsted', 'SCH'], ['SeaBird Exploration', 'SBX'], ['Seadrill', 'SDRL'], ['Selvaag Bolig ', 'SBO'], ['Sevan Drilling', 'SEVDR'], ['Sevan Marine', 'SEVAN'], ['Siem Offshore', 'SIOFF'], ['Siem Shipping', 'SSI'], ['SinOceanic Shipping', 'SINO'], ['Skiens Aktiemølle', 'SKI'], ['Solstad Offshore', 'SOFF'], ['Solvang', 'SOLV'], ['Songa Offshore', 'SONG'], ['SpareBank 1 Buskerud-Vestfold', 'SBVG'], ['SpareBank 1 Nord-Norge', 'NONG'], ['SpareBank 1 Nøtterøy - Tønsberg', 'NTSG'], ['SpareBank 1 Ringerike Hadeland', 'RING'], ['SpareBank 1 SMN', 'MING'], ['SpareBank 1 SR-Bank', 'SRBANK'], ['SpareBank 1 Østfold Akershus', 'SOAG'], ['Sparebanken Møre', 'MORG'], ['Sparebanken Pluss', 'PLUG'], ['Sparebanken Vest', 'SVEG'], ['Sparebanken Øst', 'SPOG'], ['Spectrum', 'SPU'], ['Statoil', 'STL'], ['Stolt-Nielsen', 'SNI'], ['Storebrand', 'STB'], ['Storm Real Estate', 'STORM'], ['Subsea 7', 'SUBC'], ['TGS-NOPEC Geophysical Company', 'TGS'], ['TTS Group', 'TTS'], ['Telenor', 'TEL'], ['Telio Holding', 'TELIO'], ['The Scottish Salmon Company', 'SSC'], ['Tide', 'TIDE'], ['Tomra Systems', 'TOM'], ['Totens Sparebank', 'TOTG'], ['Transit Invest', 'GRR'], ['Veidekke', 'VEI'], ['Veripos', 'VPOS'], ['Vizrt', 'VIZ'], ['Voss Veksel- og Landmandsbank', 'VVL'], ['Wentworth Resources', 'WRL'], ['Wilh. Wilhelmsen ', 'WWASA'], ['Wilh. Wilhelmsen Holding ser. A', 'WWI'], ['Wilh. Wilhelmsen Holding ser. B', 'WWIB'], ['Wilson', 'WILS'], ['Yara International', 'YAR']]


def join_compo_view(request):
    if request.method == 'POST':
        pass
    else:
        form = TraderForm()
        t = get_template('compo.html')
        c = RequestContext(request, {'form':form})
        return HttpResponse(t.render(c))

def compo_start(request):
	for pair in ticker_pair:
		ticker = pair[1]+".OSE"
		price = netfonds_price(ticker)
		if price != "price":
			company = Company.objects.create_company(pair[0],ticker,price,0.0)
	return HttpResponse("Done!")
def compo_end(request):
	for pair in ticker_pair:
		ticker = pair[1]+".OSE"
		price = netfonds_price(ticker)
		if price != "price":
			#Company.objects.filter(ticker=pair[0]).update(end_price=price)
			obj = Company.objects.get(ticker=ticker)
			obj.end_price = price
			obj.save()
	return HttpResponse("Done!")