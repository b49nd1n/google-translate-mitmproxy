from mitmproxy import ctx
import mitmproxy.http

class LocalRedirect:

	def __init__(self):
		print('Loaded redirect addon')

	def request(self, flow: mitmproxy.http.HTTPFlow):
		ctx.log.info("pretty host is: %s" % flow.request.pretty_host)
		newhost=flow.request.host.replace('.','-')+".translate.goog"
		flow.request.path="/?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=ru&_x_tr_pto=wapp"
		ctx.log.info("pretty host is: %s" % flow.request.path)
		flow.request.host = newhost
		flow.request.headers["Host"] = newhost
		flow.request.port = 443
		flow.request.scheme = "https"
		ctx.log.info("pretty host is: %s" % flow.request)

#    var url = `https://translate.google.com/translate?anno=2&depth=1&sp=nmt4&sl=en&tl=fr&u=${info.url}`;
addons = [
	LocalRedirect()
]