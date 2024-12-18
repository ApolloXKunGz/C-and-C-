"""GMT Calculate"""
ct = input()#เวลาตอนนี้ อยู่ในรูป HH:MM A.M./P.M. Ex. 03:00 P.M.
cgmt = input()#GMT ตอนนี้(ถ้าเป็น GMTที่ลงด้วยจุดทศนิยม จะเปลี่ยนเป็นนาทีเลย เช่น GMT 5.30 = xx:30 AM/PM)
tgmt = input()#GMT ของเวลาที่ต้องการจะหา

def twentyformat(t, zone):
    """แปลงเวลาเป็น 24 ชั่วโมง"""
    h, minutes = map(int, t.split(':'))
    if zone == 'P.M.' and h != 12:
        h += 12
    elif zone == 'A.M.' and h == 12:
        h = 0
    return h, minutes

def twelformat(h, minutes):
    """แปลงเวลาเป็น 12 ชั่วโมง"""
    zone = 'A.M.'
    if not h:
        h = 12
    elif h == 12:
        zone = 'P.M.'
    elif h > 12:
        h -= 12
        zone = 'P.M.'
    return f"{h:02}:{minutes:02} {zone}"

def parse_gmt(gmt_str):
    """แปลง GMT ที่เป็นทศนิยมให้เป็นนาที"""
    sign = -1 if gmt_str.startswith('-') else 1
    h, minutes = (gmt_str.lstrip('+-').split('.') + ['0'])[:2]
    return sign * (int(h) * 60 + int(minutes))

def caldiff(cta, cgmta, tgmta):
    """คำนวณเวลาที่ต่างจาก GMT"""
    t, zone = cta.split()
    ch, cm = twentyformat(t, zone)

    gmtdiff_minutes = parse_gmt(str(tgmta)) - parse_gmt(str(cgmta))

    totalmin = ch * 60 + cm
    totalmin += gmtdiff_minutes


    newh = (totalmin // 60) % 24
    newmin = totalmin % 60

    return twelformat(newh, newmin)

nt = caldiff(ct, cgmt, tgmt)
print(nt)
