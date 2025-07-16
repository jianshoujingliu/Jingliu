import requests


class All_Requests:
    sess = requests.session()

    def requests_upload(self, **kwargs):
        res = All_Requests.sess.request(**kwargs)
        return res
