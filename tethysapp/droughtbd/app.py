from tethys_sdk.base import TethysAppBase, url_map_maker


class Droughtbd(TethysAppBase):
    """
    Tethys app class for Droughtbd.
    """

    name = 'Drought Watch - Bangladesh'
    index = 'droughtbd:Home'
    icon = 'droughtbd/images/icon.gif'
    package = 'droughtbd'
    root_url = 'droughtbd'
    color = '#16a085'
    description = ''
    tags = 'Drought-Watch'
    enable_feedback = False
    feedback_emails = []


    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='Home',
                url='droughtbd',
                controller='droughtbd.controllers.Current.home'
            ),UrlMap(
                name='CurrentHome',
                url='droughtbd/current',
                controller='droughtbd.controllers.Current.home'
            ), UrlMap(
                name='SeasonalHome',
                url='droughtbd/seasonal',
                controller='droughtbd.controllers.Seasonal.home'
            ), UrlMap(
                name='OutlookHome',
                url='droughtbd/outlook',
                controller='droughtbd.controllers.Outlook.home'
            ),
            UrlMap(
                name='geomList',
                url='api/getGeomList',
                controller='droughtbd.api.getGeomList'
            ),
            UrlMap(
                name='Stats',
                url='api/getJsonFromAPI',
                controller='droughtbd.api.getJsonFromBLDAS'
            ),
            UrlMap(
                name='AreaUnder',
                url='api/getAreaUnder',
                controller='droughtbd.api.getAreaUnderFromBLDAS'
            ),
            UrlMap(
                name='LTAstats',
                url='api/getLTAStats',
                controller='droughtbd.api.getLTAStats'
            ),
            UrlMap(
                name='SAAreaUnder',
                url='api/seasonagg',
                controller='droughtbd.api.getSeasonalAggregatedRatio'
            ),
            UrlMap(
                name='PercentageOfNormal',
                url='api/percentageOfNormal',
                controller='droughtbd.api.getPercentageOfNormal'
            ),
            UrlMap(
                name='forecast',
                url='api/getSpatialAverageForecast',
                controller='droughtbd.api.getSpatialAverageForecast'
            ),
        )

        return url_maps
