
def ip_addresses(s, ip_parts=[]):
  print("%12s" % s, ip_parts)
  if len(ip_parts) == 4:
    if s:
      return []
    else:
      return [".".join(ip_parts)]
  if not s:
    return []
  res = []
  if len(s) > 2 and 100 <= int(s[:3]) <= 255:
    res += ip_addresses(s[3:], ip_parts + [s[:3]])
  if len(s) > 1 and 10 <= int(s[:2]) <= 99:
    res += ip_addresses(s[2:], ip_parts + [s[:2]])

  res += ip_addresses(s[1:], ip_parts + [s[:1]])
  if len(res) >= 1:
      print(res)
  return res

print(ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']