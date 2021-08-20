exports = []  #__:skip 
require = None #__:skip

App = require("./App")['default']
vue = require("vue")

app = vue.createApp(App)

exports['default'] = app.mount("#app")
