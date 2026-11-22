CSS = """
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=DM+Mono:wght@400;500&display=block" rel="stylesheet">
<style>
@page{size:1600px 1000px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans',sans-serif;color:#161922;background:#ECEEF2}
.page{width:1600px;height:1000px;padding:80px 96px;position:relative;overflow:hidden;page-break-after:always;background:#ECEEF2}
.page.ink{background:#161922;color:#ECEEF2}.page.acc{background:#FF8A3D;color:#161922}
h1{font:800 120px/0.95 'Bricolage Grotesque';letter-spacing:-.04em}
h2{font:800 72px/1 'Bricolage Grotesque';letter-spacing:-.035em;margin-bottom:34px}
h3{font:700 30px/1.15 'Bricolage Grotesque';letter-spacing:-.02em;margin:0 0 10px}
p,li{font-size:22px;line-height:1.5;color:#3C4150}.ink p,.ink li{color:#c9cdd8}.acc p{color:#3a2a1e}
.k{font:500 20px/1 'DM Mono';color:#D9600F;letter-spacing:.01em;margin-bottom:22px}.ink .k{color:#FFB07A}.acc .k{color:#161922}
.foot{position:absolute;left:96px;right:96px;bottom:40px;display:flex;justify-content:space-between;font:500 16px 'DM Mono';color:#7C8494}
.cols{display:grid;gap:44px}.c2{grid-template-columns:1fr 1fr}.c3{grid-template-columns:1fr 1fr 1fr}.c4{grid-template-columns:repeat(4,1fr)}
.card{background:#fff;border-radius:22px;padding:28px}.ink .card{background:#22252B}
.sw{height:150px;border-radius:18px;margin-bottom:14px}
.mono{font-family:'DM Mono';font-weight:500}
ul{padding-left:24px}li{margin-bottom:6px}
.pill{display:inline-block;font:500 16px 'DM Mono';padding:7px 14px;border-radius:999px;background:#fff;margin:0 6px 6px 0}
.do{border-left:0;}.tick{color:#14906d;font-weight:700}.cross{color:#d2413a;font-weight:700}
table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:9px 10px;border-bottom:1px solid #DFE2E8;font-size:16px;vertical-align:top}th{font:500 14px 'DM Mono';color:#7C8494}
img.th{border-radius:10px;box-shadow:0 10px 24px -14px rgba(22,25,34,.4)}
</style>"""
