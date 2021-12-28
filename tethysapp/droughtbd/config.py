# from t
from tethysapp.droughtbd.app import Droughtbd
TethysAppName=Droughtbd.package
initilizationData={
    'country':'Bangladesh',
    'navLogoImage':'/static/'+TethysAppName+'/images/noimage.png',
    'defaultView':{
        'center': [10047766.429131685, 2726986.91541812],
        'zoom': 6
    },
    'TethysAppName':TethysAppName,
    'AdminLevel':'l2Dhaka',
}
# let aa=app.map.getView().calculateExtent()
# let center=[(aa[0]+aa[2])/2,(aa[1]+aa[3])/2]
