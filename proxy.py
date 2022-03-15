from mitmproxy import ctx
import mitmproxy.http

class LocalRedirect:

	def __init__(self):
		print('Loaded redirect addon')

	def request(self, flow: mitmproxy.http.HTTPFlow):
		ctx.log.info("pretty host is: %s" % flow.request.pretty_host)
		_host = flow.request.host
		_host=_host.replace('-','--').replace('.','-')
		newhost=_host+".translate.goog"
		if flow.request.path=='/':
			flow.request.path="/?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=ru&_x_tr_pto=wapp"
		else:
			flow.request.path=flow.request.path+"?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=ru&_x_tr_pto=wapp"
		flow.request.host = newhost
		flow.request.headers["Host"] = newhost
		flow.request.port = 443
		flow.request.scheme = "https"
		ctx.log.info("pretty host is: %s" % flow.request)

addons = [
	LocalRedirect()
]