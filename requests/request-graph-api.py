import requests
import json

class GraphAPI:
    def __init__(self, fb_api):
        self.base_url = "https://graph.facebook.com/v15.0/"
        self.api_fields = ['spend', 'cpc', 'cpm', 'objective', 'adset_name',
                            'adset_id', 'clicks', 'campaign_name', 'campaign_id',
                            'conversions', 'frequency', 'conversion_values',
                            'ad_name', 'ad_id']
        self.token = "&access_token=" + fb_api

    def get_insights(self, ad_acc, level="campaign"):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/insights?level=" + level
        url += "&fields="+",".join(self.api_fields)

        data = requests.get(url + self.token)
        data = json.loads(data._content.decode("utf-8"))

        return data