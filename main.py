from flask import Flask, escape, request, render_template
import tools

# app = Flask(__name__, static_url_path='/public')
# app = Flask(__name__, static_folder='public')    
app = Flask(__name__)


# @app.route('/')
# def static_serve(path):
#     return send_from_directory(app.static_folder, path)


@app.route("/")
def main():
    return render_template('index.html')

# @app.route('/<string:page_name>/')
# def render_static(page_name):
#     return send_from_directory('%s.html' % page_name)

@app.route('/x/stop_kodi')
def stop_kodi():
    tools.stop_kodi()
    return 'ok'

@app.route('/x/restart_kodi')
def restart_kodi():
    tools.restart_kodi()
    return 'ok'

@app.route('/x/start_kodi')
def start_kodi():
    tools.start_kodi()
    return 'ok'

@app.route('/x/stop_hyperion')
def stop_hyperion():
    tools.stop_hyperion()
    return 'ok'

@app.route('/x/restart_hyperion')
def restart_hyperion():
    tools.restart_hyperion()
    return 'ok'

@app.route('/x/start_hyperion')
def start_hyperion():
    tools.start_hyperion()
    return 'ok'

@app.route('/x/hyperion_interactive')
def hyperion_interactive():
    tools.hyperion_interactive()
    return 'ok'

@app.route('/x/hyperion_sendcolor')
def hyperion_sendcolor():
    tools.hyperion_sendcolor(request.args.get('color'))
    return 'ok'

@app.route('/x/reboot_rpi')
def reboot_rpi():
    tools.reboot_rpi()
    return 'ok'

@app.route('/x/poweroff_rpi')
def poweroff_rpi():
    tools.poweroff_rpi()
    return 'ok'

app.run(host='0.0.0.0', port=5000)