import nmap
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.nmap (.*)")
async def nmap_fun(event):
    await event.edit("`Processing...`")
    nm = nmap.PortScanner()
    await event.edit("Scanning now...")
    for host in nm.all_hosts():
        result = '----------------------------------------------------'
        result += 'Host : %s (%s)' % (host, nm[host].hostname())
        result += 'State : %s' % nm[host].state()
        for proto in nm[host].all_protocols():
            result += '----------'
            result += 'Protocol : %s' % proto

            lport = sorted(nm[host][proto].keys())
            for port in lport:
                result += ('port : %s\tstate : %s' %
                           (port, nm[host][proto][port]['state']))
                await event.edit(result)

CMD_HELP.update({
    "nmap":
    ".nmap <url/ip>\
    \nUsage: Does a simple port scan on given IP/URL .\
    \nExample of a valid IP : `127.0.0.1`"
})
