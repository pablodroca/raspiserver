import psutil
import os
import netifaces
from netifaces import AF_INET
from pyramid.view import view_config
import RPi.GPIO as GPIO
import time
import logging
log = logging.getLogger(__name__)

p = None

@view_config(route_name='home', renderer='templates/home.pt')
def home_view(request):
    wlan_ip = __get_ip('wlan0')
    lan_ip = __get_ip('eth0')
    return {'wlan_ip': wlan_ip,
            'lan_ip': lan_ip,
            'cpu': '%s%%' % psutil.cpu_percent(),
            'memory': '%s%%' % psutil.virtual_memory().percent
        }

@view_config(route_name='shutdown', renderer='string')
def shutdown_view(request):
    os.system("poweroff")
    return 'Executing shutdown...'

@view_config(route_name='led_mode_on', renderer='string')
def led_mode_on(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    return 'Led Enabled'

@view_config(route_name='led_on', renderer='string')
def led_on(request):
    GPIO.output(7, GPIO.HIGH)
    log.info('Detected: led on')
    return 'Led ON'

@view_config(route_name='led_off', renderer='string')
def led_off(request):
    GPIO.output(7, GPIO.LOW)
    return 'Led OFF'

@view_config(route_name='led_mode_off', renderer='string')
def led_mode_off(request):
    GPIO.cleanup()
    return 'Led Disabled'

def __get_ip(interface):
    interfaces = set(netifaces.interfaces())
    if interface in interfaces:
        ip = netifaces.ifaddresses(interface).setdefault(AF_INET, [{'addr':'No IP addr'}])[0]['addr']
        return ip
    else:
        return ''

@view_config(route_name='pwm_on', renderer='string')
def pwm_on(request):
    global p
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35,GPIO.OUT)
    p = GPIO.PWM(35,100)
    p.start(0)

@view_config(route_name='pwm_set', renderer='string', request_param='dutycycle')
def pwm_set(request):
    global p
    dc = float(request.params['dutycycle'])
    p.ChangeDutyCycle(dc)

@view_config(route_name='pwm_off', renderer='string')
def pwm_off(request):
    global p
    p.stop()

