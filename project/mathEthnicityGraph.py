#! /usr/bin/python
print 'content-type: text/html\n'
import cgitb
cgitb.enable()

import CSintro2_project
CSintro2_project.bar()

print '''
<br><br><br><br><br><br><br><br><br><br><br><br><br>
<div>
    <a href="https://plot.ly/~margaretke/10/" target="_blank" title="" style="display: block; text-align: center;"><img src="https://plot.ly/~margaretke/10.png" alt="" style="max-width: 100%;width: 946px;"  width="946" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="margaretke:10"  src="https://plot.ly/embed.js" async></script>
</div>'''