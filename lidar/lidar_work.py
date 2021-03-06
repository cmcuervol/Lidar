# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('PDF')
import datetime as dt
import pandas as pd
import numpy as np
import struct
import sys, os, glob, locale
import matplotlib.dates as mdates
from dateutil.relativedelta import relativedelta
from mpl_toolkits.axes_grid1 import make_axes_locatable

from matplotlib.ticker import LogFormatterMathtext, LogLocator
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rc('font', family=fm.FontProperties(fname='/home/jhernandezv/Tools/AvenirLTStd-Book.ttf',).get_name(), size = 16)
plt.rc('font', family=fm.FontProperties(fname='/home/jhernandezv/Tools/AvenirLTStd-Book.ttf',).get_name(), size = 16)
typColor = '#%02x%02x%02x' % (115,115,115)
plt.rc('axes',labelcolor=typColor,edgecolor=typColor,)
plt.rc('axes.spines',right=False,top=False,left=True)
plt.rc('text',color= typColor)
plt.rc('xtick',color=typColor)
plt.rc('ytick',color=typColor)


reload (sys)
sys.setdefaultencoding ("utf-8")
locale.setlocale(locale.LC_TIME, ('es_co','utf-8'))

from pandas.plotting._core import MPLPlot

# ################################################################################
# ################################################################################
# Test Lectura Lidar

# filename = '/home/jhernandezv/Lidar/InfoLidar/AS0_180307-035517/RM1830703.553871'
# fileObj = open (filename, "rb")
#
# for i in range(8):
# 	print fileObj.readline()


#
#
# # # ################################################################################
# # # # ASCII
# files = glob.glob('InfoLidar/ASCII/20180310/*')
# ascii = Lidar(ascii=True,scan=False,output='raw')
# ascii.read(files,inplace=False)
# # #
# #
# # # ################################################################################
# # # Binario
# files = glob.glob('InfoLidar/AS0_180307-035517/RM*')
# files = glob.glob('InfoLidar/ZS0_180223-131945/RM*')
import glob

# files = glob.glob('InfoLidar/ZS0_180709-151714/RM*')      # test
files = sorted(glob.glob('/home/jhernandezv/Lidar/InfoLidar/3Ds_180703-135028/RM*') )       # test2
# files = glob.glob('InfoLidar/3Ds_180704-105519/RM*')        # test3
from lidar.lidar import Lidar
binario = Lidar(scan='Zenith',output='raw')
df1,df2 = binario.read_folder(files)
t1,t2 = binario.read_file(files[0])
t3,t4 = binario.read_file(files[1])
t5,t6 = binario.read_file(files[-1],180)
# plt.close('all')
# binario.data.groupby(axis=1,level=1).median().boxplot(column=['analog-p','analog-s'])
# binario._save_fig(textSave='_boxplot_median_analog')
# plt.close('all')
# binario.data.groupby(axis=1,level=1).median().boxplot(column=['photon-p','photon-s'])
# binario._save_fig(textSave='_boxplot_median_photon')

# binario.data.quantile(np.arange(0,1,0.01)).groupby(axis=1,level=1).median()
a=6+5




# binario = Lidar(fechaI='2018-07-04',Fechaf='2018-07-04',scan='3D')
# ()

# backup = [binario.data, binario.dataInfo]
# binario.data        = backup[0]
# binario.raw    = backup[0]
# binario.dataInfo   = backup[1]
#
# binario.plot(textSave='_test5_',parameters=['photon-p'])
# binario.plot(textSave='_test5_log',parameters=['photon-p'],output='RCS',colorbarKind='Log')
# binario.plot(textSave='_test_4D',parameters=['photon-p'],output='RCS')
# # dd, di = binario.read_folder(files)
# # '-75.5686', '6.2680'io.data.stack([1,2]).resample('30s', axis=1, level=0 ).mean().unstack([1,2])

#
# binario.plot(textSave='_test_1',parameters=['photon-p'])
# binario.plot(textSave='_test_1',parameters=['photon-p'],output='RCS')
# binario.plot(textSave='_log_test_1',output='RCS',parameters=['photon-p'],colorbarKind='Log')
# binario.plot(textSave='_test_1',output='Ln(RCS)',parameters=['photon-p'])
# binario.plot(textSave='_test_1',output='dLn(RCS)',parameters=['photon-p'],colorbarKind='Anomaly')
# binario.plot(textSave='_test_1',output='fLn(RCS)',parameters=['photon-p'])
# binario.plot(textSave='_test_1',output='fdLn(RCS)',parameters=['photon-p'],colorbarKind='Anomaly')
# binario.plot(textSave='_test_1',output='dfLn(RCS)',parameters=['photon-p'],colorbarKind='Anomaly')
# binario.plot(textSave='_test_1',output='fdfLn(RCS)',parameters=['photon-p'],colorbarKind='Anomaly')

################################################################################
# FixedPoint#
################################################################################
# date = pd.date_range('2018-08-06','2018-08-06',freq='d')[0] #'2018-06-27','2018-07-14',freq='d'):
# altura = 4.5
# binario = Lidar(fechaI=date.strftime('%Y-%m-%d'),Fechaf=date.strftime('%Y-%m-%d'),scan='FixedPoint')
# binario.read()
# binario.data = binario.data.stack([1,2]).resample('30s', axis=1, level=0 ).mean().unstack([1,2])
# binario.raw = binario.data
# binario.dataInfo = binario.dataInfo.resample('30s').mean()
# binario.dataInfo = binario.dataInfo.reindex( pd.date_range(binario.data.columns.levels[0][0],binario.data.columns.levels[0][-1],freq='30s'))
# kwgs = dict( height=altura,)# background= bkg)
# binario.plot(**kwgs )

# binario.data.reindex( pd.date_range(binario.data.columns[0],binario.data.columns[-1],freq='30s'), axis=1)
# binario.data.reindex(pd.date_range(binario.data.columns.levels[0][0],binario.data.columns.levels[0][-1],freq='30s'))

#################################################################################
#Calculo CLA
################################################################################
import pandas as pd
import numpy as np
import datetime as dt
import os, locale
# os.system('rm lidar/lidar/*.pyc')
from lidar.lidar import Lidar
locale.setlocale(locale.LC_TIME, ('en_GB','utf-8'))
#
def cloud_filter(data,clouds):
    tmpData = {}
    for col in clouds.columns.levels[2]:
        tmpData[col+'-p'] = data.xs(col+'-p',axis=1,level=2).mask(clouds.xs(col,axis=1,level=2) >=.95 )
        tmpData[col+'-s'] = data.xs(col+'-s',axis=1,level=2).mask(clouds.xs(col,axis=1,level=2) >=.95 )
    return pd.concat(tmpData,names=['Parameters','Dates']).unstack(0)


# vlim = {'analog-s':[0.2,16],'analog-p':[0.2,16],'analog':[0,0.7] }


# for date in pd.date_range('2018-06-01','2018-10-01',freq='d'): #'2018-06-27','2018-07-14',freq='d'):
    # try:
# date = pd.date_range('2018-06-30','2018-06-30',freq='d')[0] #'2018-06-27','2018-07-14',freq='d'):
date = pd.date_range('2018-08-28','2018-08-28',freq='d')[0]
        #
binario =   Lidar(
    fechaI=date.strftime('%Y-%m-%d'),
    fechaF=date.strftime('%Y-%m-%d'),
    scan='FixedPoint',
    output='raw'
)

height = 4.5


binario.get_output(output='LVD')

lvd = binario.datos.loc(axis=1) [
    binario.datos.columns.levels[0] [
        binario.datos.columns.levels[0] < height
    ]
]

binario.get_output(output='RCS')



binario.datos = binario.datos.loc(axis=1) [
    binario.datos.columns.levels[0] [
        binario.datos.columns.levels[0] < height
    ]
]

# Suavizado
#Espacial
binario.datos = binario.datos.groupby(
                    level=[1,2], axis=1
                    ).rolling(16,
                        center=True,
                        min_periods=1,
                        axis=1
                        ).mean()
binario.datos.columns = binario.datos.columns.droplevel([0,1])
# Temporal
binario.datos = binario.datos.rolling(6,
                        center=True,
                        min_periods=1).mean()


binario.datos = binario.datos.resample('10T').mean()

lvd = lvd.resample('10T').mean()
backup = binario.datos.copy()
#------------------------
# Varianza Maxima
# ------------------------

# binario.datos = cloud_filter(backup, lvd)

binario.datos = binario.datos.groupby(
                    level=[1,2], axis=1
                    ).rolling(54,
                        center=True,
                        min_periods=1,
                        axis=1).var()
binario.datos.columns = binario.datos.columns.droplevel([0,1])

binario.plot(
    df=binario.datos,
    path='claTest',
    textSave='_VM',
    colorbarKind='Linear',
    height=height,
    colormap='jet',
    cbarLabel=r'$\sigma(RCS)$')

vm = binario.datos.groupby(level=[1,2],axis=1).idxmin(axis=1)
for col in vm.columns:
    vm[col] = vm[col].str[0]
#------------------------
# Gradiente minimo
#------------------------
# binario.datos = cloud_filter(backup, lvd)
binario.datos = backup.copy()
dr  = (binario.datos.columns.levels[0][2] - binario.datos.columns.levels[0][0])
binario.datos = binario.datos.groupby(level=[1,2],axis=1).diff(axis=1,periods=2) /dr


# binario.plot(
#     df=binario.datos,
#     path='claTest',
#     textSave='_GM',
#     colorbarKind='Anomaly',
#     height=height,
#     colormap='seismic',
#     cbarLabel=r'$\delta(RCS)$',
#     # vlim=[-3,15]
#     )

#get cla
gm = binario.datos.groupby(level=[1,2],axis=1).idxmin(axis=1)
for col in gm.columns:
    gm[col] = gm[col].str[0]


#################################################################################
#Calculo CLA
################################################################################

from Funciones_Lectura import lee_Ceil,lee_data_ceil
# import pandas as pd
import pandas as pd
import numpy as np
import datetime as dt
import os, locale
# os.system('rm lidar/lidar/*.pyc')
from lidar.lidar import Lidar
locale.setlocale(locale.LC_TIME, ('en_GB','utf-8'))

# vlim = {'analog-s':[0.2,16],'analog-p':[0.2,16],'analog':[0,0.7] }


# for date in pd.date_range('2018-06-01','2018-10-11',freq='d'): #'2018-06-27','2018-07-14',freq='d'):
#     try:
date = pd.date_range('2018-08-28','2018-08-28',freq='d')[0]
# date = pd.date_range('2018-06-30','2018-06-30',freq='d')[0] #'2018-06-27','2018-07-14',freq='d'):

scan= '3D'
now = dt.datetime.now()
instance =   Lidar(
        fechaI=(now-dt.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M'),
        fechaF=now.strftime('%Y-%m-%d %H:%M'),
        scan=scan,
        output='raw',
        path='CalidadAire/Lidar/'
    )
# binario =   Lidar(
#     fechaI=date.strftime('%Y-%m-%d'),
#     fechaF=date.strftime('%Y-%m-%d'),
#     scan='FixedPoint',
#     # scan='3D',
#     output='raw',
#     # path='CalidadAire/Lidar'
# )


# binario.get_output(output='RCS')
# binario.datos.loc(axis=1)[:,:,'photon-p'] * binario.datosInfo.loc[0,'BinWidth_photon-p']
# backup = [binario.datos.copy(), binario.datosInfo.copy()]
# # binario.datos        = backup[0]
# # binario.raw    = backup[0].copy()
# # binario.datosInfo   = backup[1]'cython_test', #
#
# binario.datos = binario.datos.resample('30s').mean()
# binario.raw = binario.raw.resample('30s').mean()
# binario.datosInfo = binario.datosInfo.resample('30s').mean()
#


kwgs = dict(
    height=4.5,
    # height=12,
    # path= 'claTest',
    # path= date.strftime('%m-%d'),
    cla=False #True
)

# binario.plot(output = 'raw',**kwgs )
#
#
# binario.plot(output = 'P(r)',
#     totalSignal=True,
#     vlim=[0,135],
#     parameters=['photon-s','photon-p'],
#     **kwgs )
# #
# binario.plot(output = 'P(r)',
#     totalSignal=True,
#     vlim=[5,34],
#     parameters=['analog-s','analog-p'],
#     **kwgs )
#
# binario.plot(output = 'S(r)',totalSignal=True,**kwgs )
# binario.plot(output = 'LVD',
#     totalSignal=True,
#     vlim=[0.25,1],
#     **kwgs )

binario.plot(
    output='RCS',
    **kwgs
)
binario.plot(
    output='LVD',
    **kwgs
)



binario.plot(
    output='RCS',
    parameters=['analog-b'],
    vlim = [.15,20],#[1,20],
    **kwgs
)

binario.plot(
    parameters=['analog-s','analog-p'],
    vlim=[.1,16], #[1,16]
    output='RCS',
    **kwgs
)

binario.plot(
    parameters=['photon-s','photon-p'],
    vlim=[9,200], #[15,350]
    output='RCS',
    **kwgs
)

binario.plot(
    output='RCS',
    parameters=['photon-b'],
    vlim = [10,200],
    **kwgs
)
import pandas as pd
import numpy as np
import datetime as dt
import os, locale
# os.system('rm lidar/lidar/*.pyc')
from lidar.lidar import Lidar
locale.setlocale(locale.LC_TIME, ('en_GB','utf-8'))

# vlim = {'analog-s':[0.2,16],'analog-p':[0.2,16],'analog':[0,0.7] }


# for date in pd.date_range('2018-06-01','2018-10-11',freq='d'): #'2018-06-27','2018-07-14',freq='d'):
#     try:
date = pd.date_range('2018-09-07','2018-09-07',freq='d')[0]
# date = pd.date_range('2018-06-30','2018-06-30',freq='d')[0] #'2018-06-27','2018-07-14',freq='d'):
        #
binario =   Lidar(
    fechaI=date.strftime('%Y-%m-%d'),
    fechaF=date.strftime('%Y-%m-%d'),
    scan='Zenith',
    # scan='3D',
    output='raw'
)


# binario.get_output(output='RCS')
# binario.datos.loc(axis=1)[:,:,'photon-p'] * binario.datosInfo.loc[0,'BinWidth_photon-p']
# backup = [binario.datos.copy(), binario.datosInfo.copy()]
# # binario.datos        = backup[0]
# # binario.raw    = backup[0].copy()
# # binario.datosInfo   = backup[1]'cython_test', #
#
# binario.datos = binario.datos.resample('30s').mean()
# binario.raw = binario.raw.resample('30s').mean()
# binario.datosInfo = binario.datosInfo.resample('30s').mean()
#


kwgs = dict(
    height=6,
    # height=12,
    path= 'claTest',
    # path= date.strftime('%m-%d'),
    cla=True
)

# binario.plot(output = 'raw',**kwgs )
# binario.plot(output = 'S(r)',totalSignal=True,**kwgs )

# binario.plot(output = 'P(r)',
#     totalSignal=True,
#     vlim=[0,135],
#     parameters=['photon-s','photon-p'],
#     **kwgs )
#
# binario.plot(output = 'P(r)',
#     totalSignal=True,
#     vlim=[5,34],
#     parameters=['analog-s','analog-p'],
#     **kwgs )
#
# binario.plot(output = 'LVD',
#     totalSignal=True,
#     vlim=[0.25,1],
#     **kwgs )

binario.plot(
    output='RCS',
    parameters=['analog-b'],
    vlim = [.15,20],#[1,20],
    **kwgs
)

binario.plot(
    parameters=['analog-s','analog-p'],
    vlim=[.1,16], #[1,16]
    output='RCS',
    **kwgs
)

binario.plot(
    parameters=['photon-s','photon-p'],
    vlim=[9,200], #[15,350]
    output='RCS',
    **kwgs
)

binario.plot(
    output='RCS',
    parameters=['photon-b'],
    vlim = [10,200],
    **kwgs
)
import pandas as pd
import numpy as np
import datetime as dt
import os, locale
# os.system('rm lidar/lidar/*.pyc')
from lidar.lidar import Lidar
locale.setlocale(locale.LC_TIME, ('en_GB','utf-8'))

# vlim = {'analog-s':[0.2,16],'analog-p':[0.2,16],'analog':[0,0.7] }


# for date in pd.date_range('2018-06-01','2018-10-11',freq='d'): #'2018-06-27','2018-07-14',freq='d'):
#     try:
# date = pd.date_range('2018-08-17','2018-08-17',freq='d')[0]
date = pd.date_range('2018-06-30','2018-06-30',freq='d')[0] #'2018-06-27','2018-07-14',freq='d'):
        #
binario =   Lidar(
    fechaI=date.strftime('%Y-%m-%d'),
    fechaF=date.strftime('%Y-%m-%d'),
    # scan='FixedPoint',
    scan='3D',
    output='raw'
)


# binario.get_output(output='RCS')
# binario.datos.loc(axis=1)[:,:,'photon-p'] * binario.datosInfo.loc[0,'BinWidth_photon-p']
# backup = [binario.datos.copy(), binario.datosInfo.copy()]
# # binario.datos        = backup[0]
# # binario.raw    = backup[0].copy()
# # binario.datosInfo   = backup[1]'cython_test', #
#
# binario.datos = binario.datos.resample('30s').mean()
# binario.raw = binario.raw.resample('30s').mean()
# binario.datosInfo = binario.datosInfo.resample('30s').mean()
#


kwgs = dict(
    height=5.5,
    # height=12,
    path= 'claTest',
    # path= date.strftime('%m-%d'),
    cla=True
)
binario.plot(
    output='RCS',
    **kwgs
)
# binario.plot(output = 'raw',**kwgs )
# binario.plot(output = 'S(r)',totalSignal=True,**kwgs )

# binario.plot(output = 'P(r)',
#     totalSignal=True,
#     vlim=[0,135],
#     parameters=['photon-s','photon-p'],
#     **kwgs )
#
# binario.plot(output = 'P(r)',
#     totalSignal=True,
#     vlim=[5,34],
#     parameters=['analog-s','analog-p'],
#     **kwgs )
#
# binario.plot(output = 'LVD',
#     totalSignal=True,
#     vlim=[0.25,1],
#     **kwgs )

binario.plot(
    output='RCS',
    parameters=['analog-b'],
    vlim = [.15,20],#[1,20],
    **kwgs
)

binario.plot(
    parameters=['analog-s','analog-p'],
    vlim=[.1,16], #[1,16]
    output='RCS',
    **kwgs
)

binario.plot(
    parameters=['photon-s','photon-p'],
    vlim=[9,200], #[15,350]
    output='RCS',
    **kwgs
)

binario.plot(
    output='RCS',
    parameters=['photon-b'],
    vlim = [10,200],
    **kwgs
)

        binario.plot( output='Ln(RCS)', **kwgs )

        binario.plot(output='dLn(RCS)',  **kwgs)

        binario.plot(output='fLn(RCS)', **kwgs)

        binario.plot(output='fdLn(RCS)',  **kwgs)

        binario.plot(output='dfLn(RCS)', **kwgs)

        binario.plot(output='fdfLn(RCS)' , **kwgs)

        for location in ['amva','siata','itagui']:
            # binario = Lidar(fechaI='20180801',Fechaf='20180801',scan='FixedPoint',output='raw')
            ceil = lee_Ceil(
                ceilometro=location,
                Fecha_Inicio=binario.datosInfo.index[0].strftime('%Y%m%d %H:%M'), Fecha_Fin=binario.datosInfo.index[-1].strftime('%Y%m%d %H:%M') ) #'%Y-%m-%d %H:%M:%S'
            # ceil         = lee_Ceil(ceilometro=location,  Fecha_Inicio='20180801 10:45', Fecha_Fin='20180801 13:25' )
            ceil.columns            = (ceil.columns+1)/100.
            ceil[ceil < 100]        = 100
            ceil[ceil.isnull()]     = 100
            if ceil.size > 0:
                binario.plot_lidar(
                    ceil.index,ceil.columns,ceil.T,
                    textSave='Ceilometro_'+location,
                    colorbarKind='Log',
                    vlim=[10,13000],
                    cbarlabel=r'Intensidad Backscatter $[10^{-9}m^{-1}sr^{-1}]$',
                    path='jhernandezv/Lidar/FixedPoint/' +kwgs['path'],
                    colormap = binario.ceilCmap
                )
    except:
        import traceback
        traceback.print_exc()
        pass
# #

# binario.plot( output='Ln(RCS)', **kwgs )
################################################################################
# Ceilomoetro
# from Funciones_Lectura import lee_Ceil,lee_data_ceil
# # #
# fecha_test = pd.date_range('2018-08-03 09:35:00', '2018-08-03 18:56:30',freq='30s')#binario.data.columns.levels[0]
# ceil =lee_data_ceil('amva',fecha_test[0].strftime('%Y-%m-%d %H:%M:%S'),fecha_test[-1].strftime('%Y-%m-%d %H:%M:%S') ) #fecha_test[0].strftime('%Y%m%d %H:%M'),fecha_test[-1].strftime('%Y%m%d %H:%M'),'amva')
# ceil.columns = (ceil.columns+1)/100.
# ceil[ceil < 100] = 100
# ceil[ceil.isnull()] = 100
# #
# binario.plot_lidar(ceil.index,ceil.columns,ceil.T,textSave='Ceilometro_AMVA',colorbarKind='Log',vlim=[10,13000],cbarlabel='Intensidad Backscatter $[10^{-9}m^{-1}sr^{-1}]$',**kwgs)
##############################################################################
        #

        # binario.plot(output='dLn(RCS)',colorbarKind='Anomaly',  **kwgs)

        # binario.plot(output='fLn(RCS)', **kwgs)

        # binario.plot(output='fdLn(RCS)',colorbarKind='Anomaly',  **kwgs)

        # binario.plot(output='dfLn(RCS)', colorbarKind='Anomaly', **kwgs)

        # binario.plot(output='fdfLn(RCS)', colorbarKind='Anomaly',  **kwgs)

        #10 km
        # kwgs = dict(  height=10,textSave='_10km',path='10km')# background= bkg)
        #
        # binario.plot(output = 'P(r)', **kwgs )
        #
        # binario.plot( output='RCS', **kwgs )
        #
        #
        # binario.plot( output='Ln(RCS)', **kwgs )
        # # #
        #
        # # binario.plot(output='dLn(RCS)',colorbarKind='Anomaly',  **kwgs)
        #
        # binario.plot(output='fLn(RCS)', **kwgs)
        #
        # # binario.plot(output='fdLn(RCS)',colorbarKind='Anomaly',  **kwgs)
        #
        # # binario.plot(output='dfLn(RCS)', colorbarKind='Anomaly', **kwgs)
        #
        # binario.plot(output='fdfLn(RCS)', colorbarKind='Anomaly',  **kwgs)
        #
        # kwgs.pop('textSave')
        # binario.plot(textSave='_log_10km', output='RCS',colorbarKind='Log',  **kwgs)


    # except:
    #     pass


# # ################################################################################
# backgroud = '2018-06-30 19:07'
# bkg = pd.read_csv('Background_test.csv',index_col=0,header=[0,1])
# bkg = pd.read_csv('Background.csv',index_col=0,header=[0,1])
# bkg.columns.set_levels(map(lambda x: int(x),bkg.columns.levels[0].values), level=0,inplace=True)
# # bkg = bkg.rolling(30,center=True,min_periods=1).mean()
# bkg = {'analog-p':5.307, 'analog-s':4.9846, 'photon-p':0.26578, 'photon-s':0.26578}

# x = bkg.loc[bkg.index>15,pd.IndexSlice[:,'photon-s']]
# x[x>0].min() - x[x>0].min().min() *18**2

# bkg.loc[:,pd.IndexSlice[:,'analog-s']]  = 4.9846
# bkg.loc[:,pd.IndexSlice[:,'analog-p']]  = 5.307
# bkg.loc[:,pd.IndexSlice[:,['photon-p','photon-s']] ]  = 0.26578#0.13289

# bkg.loc[:,pd.IndexSlice[:,'analog-p']]  =
# ################################################################################
# from Funciones_Lectura import lee_Ceil,lee_data_ceil
# import pandas as pd
import pandas as pd
import numpy as np
import datetime as dt
import os, locale
# os.system('rm lidar/lidar/*.pyc')
from lidar.lidar import Lidar
locale.setlocale(locale.LC_TIME, ('en_GB','utf-8'))


# for date in pd.date_range('2018-02-23','2018-10-11',freq='d'): #'2018-06-27','2018-07-14',freq='d'):
#     try:
date = pd.date_range('2018-10-11','2018-10-11',freq='d')[0] #'2018-06-27','2018-07-14',freq='d'):

binario = Lidar(
fechaI=date.strftime('%Y-%m-%d'),
fechaF=date.strftime('%Y-%m-%d'),
scan='Azimuth',
output='raw'
)

# # backup = [binario.raw, binario.dataInfo]
# # binario.data        = backup[0]
# # binario.raw    = backup[0]
# # binario.dataInfo   = backup[1]
#
#
# kwgs = dict(parameters=['photon-p'], dates=binario.dataInfo.index, make_gif=True, path= date.strftime('%Y-%m-%d-bkg-nonan'),height=altura, background= bkg)
# kwgs = dict(height=altura,path='vlim',dates =binario.dataInfo.index[binario.dataInfo.index.hour <1 ])
kwgs = dict(
    height=.8,
    path= date.strftime('%m-%d'),
    textSave='',
    dates=binario.datos.index,
    makeGif=True,
)

binario.plot(output = 'P(r)',
    totalSignal=True,
    vlim=[0,135],
    parameters=['photon-s','photon-p'],
    scp=False,
    **kwgs )

binario.plot(output = 'P(r)',
    totalSignal=True,
    vlim=[5,34],
    parameters=['analog-s','analog-p'],
    scp=False,
    **kwgs )

binario.plot(
    parameters=['analog-s','analog-p'],
    vlim=[0.15,16], #[15,350]
    output='RCS',
    **kwgs
)

binario.plot(
    output='RCS',
    parameters=['analog-b'],
    vlim = [0.15,20],
    **kwgs
)



binario.plot(
    parameters=['photon-s','photon-p','photon-b'],
    vlim=[9,200], #[15,350]
    output='RCS',
    **kwgs
)

binario.plot(
    output='LVD',
    totalSignal=True,
    vlim = [0.25,1],
    **kwgs
)
kwgs['scp'] = False
binario.plot( output='Ln(RCS)', **kwgs )
# #

binario.plot(output='dLn(RCS)', **kwgs)

binario.plot(output='fLn(RCS)', **kwgs)

binario.plot(output='fdLn(RCS)',  **kwgs)

binario.plot(output='dfLn(RCS)',  **kwgs)

binario.plot(output='fdfLn(RCS)', **kwgs)


    except:
        pass
# binario.plot(
#     output='RCS',
#     parameters=['photon-b'],
#     vlim = [10,200],
#     **kwgs
# )
#### Informe de Actividades
#
# #
# #
# binario.plot( output='P(r)',**kwgs )
#
# binario.plot( output='RCS', **kwgs )
#
# binario.plot(textSave='_log', output='RCS',colorbarKind='Log',  **kwgs)
#
#
# binario.plot( output='Ln(RCS)', **kwgs )
# # #
#
# binario.plot(output='dLn(RCS)',colorbarKind='Anomaly',  **kwgs)
#
# binario.plot(scp=False,output='fLn(RCS)', **kwgs)
#
# binario.plot(output='fdLn(RCS)',colorbarKind='Anomaly',  **kwgs)
#
# binario.plot(output='dfLn(RCS)', colorbarKind='Anomaly', **kwgs)
#
# binario.plot(output='fdfLn(RCS)', colorbarKind='Anomaly',  **kwgs)

    # except:
    #     pass
# binario.plot(textSave='_test', parameters=['photon-p'], output='RCS', colorbarKind='Log', dates=binario.dataInfo.index, make_gif=True, path= '2018-07-04',scp=False)
# binario.plot(textSave='_test', parameters=['photon-p'], output='fdfLn(RCS)', colorbarKind='Anomaly', dates=binario.dataInfo.index, make_gif=True, path= '2018-07-04') #,vlim=[-2,4]
# binario.profiler(zenith=True,textSave='_RCS_log_test',parameter='analog-s',linear=False)
# binario.profiler(zenith=True,textSave='_RCS_log_test',parameter='analog-p',linear=False)
# binario.profiler(zenith=True,textSave='_RCS_log_test',parameter='photon-s',linear=False)
# binario.profiler(zenith=True,textSave='_RCS_log_test',parameter='photon-p',linear=False)
#
# binario.profiler(zenith=True,textSave='_RCS_log_test',parameter='photon-p',linear=False)

# plt.close('all')
# # # #  pd.concat({'ascii':ascii.data[ascii.data.columns.levels[0][1]].sort_index(axis=1), 'binario':binario.data[binario.data.columns.levels[0][1]].sort_index(axis=1)} , axis = 1)
# # #
# # ascii.data[ascii.data.columns.levels[0][1]]
# binario.get_output(output='RCS')
# x = binario.data[binario.data.columns.levels[0][1]]
# # x.mask(x==0,inplace=True)
# x.plot(xlim=(0,4000),subplots=True,figsize=(14,8),layout=(2,2),logy=True)
# plt.savefig('Figuras/Datos_Lidar_RCS.png',bbox_inches='tight' )
# os.system('scp Figuras/Datos_Lidar_RCS.png jhernandezv@siata.gov.co:/var/www/jhernandezv/Lidar/')
# # #
#
# binario.data.mask(binario.data<=0,inplace=True)
# binario.data = np.log(binario.data)
# binario.profiler(zenith=True,textSave='_RCS_logdata_test',parameter='analog-s')
# binario.profiler(zenith=True,textSave='_RCS_logdata_test',parameter='analog-p')
# binario.profiler(zenith=True,textSave='_RCS_logdata_test',parameter='photon-s')
# binario.profiler(zenith=True,textSave='_RCS_logdata_test',parameter='photon-p')
#
#
# # #binario.data['2018-03-07 03:55:24'].iloc[:1200]
#
# # # #Plot
# plt.close('all')
# # # #  pd.concat({'ascii':ascii.data[ascii.data.columns.levels[0][1]].sort_index(axis=1), 'binario':binario.data[binario.data.columns.levels[0][1]].sort_index(axis=1)} , axis = 1)
# # #
# # ascii.data[ascii.data.columns.levels[0][1]]
# x = binario.data[binario.data.columns.levels[0][4]]
# # x.mask(x==0,inplace=True)
# x.plot(xlim=(0,4000),subplots=True,figsize=(14,8),layout=(2,2),logy=True)
# plt.savefig('Figuras/Datos_Lidar_RCS_log.png',bbox_inches='tight' )
# os.system('scp Figuras/Datos_Lidar_RCS_log.png jhernandezv@siata.gov.co:/var/www/jhernandezv/Lidar/')
# #
# # # #
# # #
#
# #Plot
# plt.close('all')
# binario.data[binario.data.columns.levels[0][1]].plot(xlim=(0,4000),subplots=True,figsize=(14,8),layout=(2,2))
# plt.savefig('Figuras/Datos_Lidar_Binario_derived_rezago18.png',bbox_inches='tight' )
# os.system('scp Figuras/Datos_Lidar_Binario_derived_rezago18.png jhernandezv@siata.gov.co:/var/www/jhernandezv/Lidar/')
#
# # # ################################################################################
# # # Regresion Mediana
# x   = ascii.data.groupby(axis=1,level=1).median()
# y   = binario.data.groupby(axis=1,level=1).median()
# z = pd.concat({'ascii':x,'binario':y},axis=1)
#
# plt.close('all')
# z.plot(xlim=(0,4000),subplots=True,figsize=(24,12),layout=(2,4))
# plt.savefig('Figuras/Datos_Lidar_media_derived.png',bbox_inches='tight')
# os.system('scp Figuras/Datos_Lidar_media_derived.png jhernandezv@siata.gov.co:/var/www/jhernandezv/Lidar/')
#
#
# # for rezago in range(19):
# rezago=0
# plt.close('all')
# fig = plt.figure(figsize=(18,18))
# ax = {}
# for ix,col in enumerate(z.columns.levels[1].values):
#     print col,ix
#     # ax[ix] = fig.add_subplot(1 if ix <2 else 2,(ix%2)+1,(ix%2)+1)
#     ax[ix] = fig.add_subplot(2,2,ix+1)
#
#     # rl  = stats.linregress(x[col],y.loc[y.index [rezago:rezago-18]  if rezago<18 else y.index [18:],col])
#     rl  = stats.linregress(x[col],y[col])
#     title = 'slope = {} \nintercept = {} \nrvalue = {}'.format(rl.slope,rl.intercept,rl.rvalue)
#     # dataplot = z.xs(col,axis=1,level=1)
#     # ax[ix].scatter(x[col],y.loc[y.index [rezago:rezago-18]  if rezago<18 else y.index [18:],col],ylabel=col,)
#     ax[ix].scatter(x[col],y[col],ylabel=col,)
#     ax[ix].set_title(title)
#     ax[ix].legend()
# plt.savefig('Figuras/Datos_Lidar_RL_derived.png',bbox_inches='tight')
# os.system('scp Figuras/Datos_Lidar_RL_derived.png jhernandezv@siata.gov.co:/var/www/jhernandezv/Lidar/')


# from pandas.plotting import scatter_matrix
# plt.close('all')
# scatter_matrix(z, alpha=0.2, figsize=(24, 24), diagonal='kde')
# plt.savefig('Figuras/Datos_Lidar_median.scatter.png',bbox_inches='tight')
# os.system('scp Figuras/Datos_Lidar_median.scatter.png jhernandezv@siata.gov.co:/var/www/jhernandezv/Lidar/')
#
#
# y.loc[y.index[:-18],['analog-p','analog-s']] = y.loc[y.index[18:],['analog-p','analog-s']].values
# y.loc[y.index[-18:],['analog-p','analog-s']] = np.NaN
# z = pd.concat({'ascii':x,'binario':y},axis=1)
#
# plt.close('all')
# scatter_matrix(z, alpha=0.2, figsize=(24, 24), diagonal='kde')
# plt.savefig('Figuras/Datos_Lidar_median.scatter-18.png',bbox_inches='tight')
# os.system('scp Figuras/Datos_Lidar_median.scatter-18.png jhernandezv@siata.gov.co:/var/www/jhernandezv/Lidar/')
#
#
#
# ################################################################################
# # # # Multiple Linear Regression
#
# z = pd.concat({'ascii':ascii.data,'binario':binario.data})
#
# LR = pd.DataFrame() #columns =['slope','intercept','rvalue', 'pvalue', 'stderr'])
# for col in z.columns:
#     print col
#     y = z.loc['binario',col]
#     lr = stats.linregress(z.loc['ascii',col].values, (y.loc[y.index[18:]] if 'analog' in col[1] else y.loc[y.index[:-18]]).values  )
#     LR = LR.append( pd.DataFrame({'slope':lr.slope, 'intercept':lr.intercept, 'rvalue':lr.rvalue, 'pvalue':lr.pvalue, 'stderr':lr.stderr}, index=[col] ) )
#
# LR.index = pd.MultiIndex.from_tuples(LR.index)
# LR = LR.unstack()
#
#
# plt.close('all')
# plt.locator_params(axis='x', nbins=3)
# LR[['intercept','slope']].plot(kind='kde',subplots=True, layout=(2,4),figsize=(26,15), sharex=False )
# plt.savefig('Figuras/Datos_Lidar_Hist_LR.png',bbox_inches='tight')
# os.system('scp Figuras/Datos_Lidar_Hist_LR.png jhernandezv@siata.gov.co:/var/www/jhernandezv/Lidar/')
#
# LR[['intercept','slope','rvalue']].max()
# LR[['intercept','slope','rvalue']].min()


#
# # ################################################################################
# #                 HISTORY
# # ################################################################################
# #
# Error = []
# os.system('mkdir Datos')
# dates = pd.date_range('20171219','20180522',freq='d')
#
# for d in dates:
# # d = dates[0]
#     os.system('rm -r Datos/*')
#     os.system('scp -r jhernandezv@192.168.1.62:/mnt/ALMACENAMIENTO/LIDAR/Scanning_Measurements/{}/* Datos/'.format( d.strftime('%Y%m%d')))
#
#     #Zenith
#     folders = glob.glob('Datos/ZS*')
#     if len(folders) > 0 :
#         os.system('ssh jhernandezv@siata.gov.co "mkdir /var/www/jhernandezv/Lidar/Zenith/{}/"'.format( d.strftime('%Y%m%d')))
#         for folder in folders:
#             files   = glob.glob('{}/RM*'.format(folder))
#             self    = Lidar(output='RCS')
#             self.read(files,)
#
#             try:
#                 self.plot(textSave = '_{}'.format(self.dataInfo.index[0].strftime('%H:%M')), path = 'jhernandezv/Lidar/Zenith/{}/'.format(d.strftime('%Y%m%d')),colorbarKind='Log')
#             except:
#                 Error.append(folder)
#                 pass
#
#     #Azimuth
#     folders = glob.glob('Datos/A*')
#     if len(folders) > 0 :
#         os.system('ssh jhernandezv@siata.gov.co "mkdir /var/www/jhernandezv/Lidar/Azimuth/{}/"'.format( d.strftime('%Y%m%d')))
#         for folder in folders:
#             files   = glob.glob('{}/RM*'.format(folder))
#             self    = Lidar(output='RCS')
#             self.read(files)
#             try:
#                 self.plot(zenith=False, colorbarKind='Log', \
#                     textSave = '_{}'.format(self.dataInfo.index[0].strftime('%H:%M')), \
#                     path = 'jhernandezv/Lidar/Azimuth/{}/'.format(d.strftime('%Y%m%d')))
#             except:
#                 Error.append(folder)
#                 pass
#
# ##############################################################################
# Error = []
# Zenith = {}
# #Fixed points
# # dates = pd.date_range('20171219','20180522',freq='d')
# dates = pd.date_range('20180425','20180522',freq='d')
# for d in dates:
# # d = dates[0]
#     os.system('rm -r Datos/*')
#     os.system('scp -r jhernandezv@192.168.1.62:/mnt/ALMACENAMIENTO/LIDAR/Fixed_Point/{}/* Datos/'.format( d.strftime('%Y%m%d')))
#
#     files = glob.glob('Datos/RM*')
#     if len(files) > 0:
#         os.system('ssh jhernandezv@siata.gov.co "mkdir /var/www/jhernandezv/Lidar/FixedPoint/{}/"'.format( d.strftime('%Y%m%d')))
#         self = Lidar(scan=False,output='RCS')
#         self.read(files)
#
#         try:
#             Zenith [d.strftime('%Y%m%d')] = self.plot(colorbarKind='Log',zenith=False, \
#                 textSave = '_{}'.format(self.dataInfo.index[0].strftime('%H:%M')), \
#                 path = 'jhernandezv/Lidar/FixedPoint/{}/'.format(d.strftime('%Y%m%d')))
#         except:
#             Error.append(d.strftime('%Y%m%d'))
#             pass
#
# print Zenith
# ###############################################################################
# #3Ds
# os.system('rm Figuras/*')
# os.system('mkdir Datos')
# # dates = pd.date_range('20180624','20180717',freq='d')
# dates = pd.date_range('20180704','20180705',freq='d')
#
# for d in dates:
# # d = dates[0]
#     os.system('rm -r Datos/*')
#     os.system('scp -r jhernandezv@192.168.1.62:/mnt/ALMACENAMIENTO/LIDAR/Scanning_Measurements/{}/* Datos/'.format( d.strftime('%Y%m%d')))
#
#     folders = glob.glob('Datos/3D*')
#     if len(folders) > 0 :
#         os.system('ssh jhernandezv@siata.gov.co "mkdir /var/www/jhernandezv/Lidar/3D/{}/"'.format( d.strftime('%Y%m%d')))
#         for folder in folders:
#             files   = glob.glob('{}/RM*'.format(folder))
#             self    = Lidar(output='RCS',ascii=d.strftime('%Y-%m-%d') in ['2018-06-24','2018-06-25','2018-06-26'] )
#             print folder
#             self.read(files,tresd=True)
#             try:
#                 self.plot(colorbarKind='Log', textSave ='_{}'.format(self.dataInfo.index[0].strftime('%H:%M')), \
#                         path= '{}3D/{}/'.format(self.kwargs['path'],d.strftime('%Y%m%d')), vlim=[6.7,9])
#             except:
#                 Error.append(folders)
#                 pass
#         # os.system('convert -delay 20 -loop 0 {}*.png {}.gif'.format())
#         for col in self.data.columns.levels[1].values:
#             os.system( 'convert -delay 20 -loop 0 Figuras/Lidar_Scanning_RCS_{}_* Figuras/lidar_Scanning_RCS_{}_{}.gif'.format(col,col,d.strftime('%Y%m%d')))
#             os.system('scp Figuras/lidar_Scanning_RCS_{}_{}.gif jhernandezv@siata.gov.co:/var/www/jhernandezv/Lidar/3D/{}/ '.format(col,d.strftime('%Y%m%d'),d.strftime('%Y%m%d')) )

class Employee(object):

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def testmethod(self,any):
        print 'Test 1'



# class Developer(Employee):
#
#     raise_amt = 1.10
#
#     def __init__(self, test):
#         self.test = test
#
#     def set_dev(self,first, last, pay, prog_lang):
#         super(Developer,self).__init__(first, last, pay)
#         self.prog_lang = prog_lang
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer,self).__init__(first, last, pay)
        self.prog_lang = prog_lang






class Manager(Developer):
    raise_amt = 1.2

    def __init__(self, first, last, pay,prog_lang='python', employees=None):
        super(Manager,self).__init__(first, last, pay, prog_lang)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def testmethod(self,any):
        print 'Test 2'

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, 'Python', [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()
