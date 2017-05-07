#! /usr/bin/python
print 'content-type: text/html\n'
import cgitb
cgitb.enable()

import CSintro2_project
CSintro2_project.bar()

print '''
<br><br><br><br><br><br><br><br><br><br><br><br><br>
<div>
    <a href="https://plot.ly/~vin.jia/3/" target="_blank" title="Col2" style="display: block; text-align: center;"><img src="https://plot.ly/~vin.jia/3.png" alt="Col2" style="max-width: 100%;width: 1121px;"  width="1121" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="vin.jia:3"  src="https://plot.ly/embed.js" async></script>
</div>
'''