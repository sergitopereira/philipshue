# philipshue

# Usage Example
```
from http_hue_api.http_hue_api import PyHue
a=PyHue(hub_ip="192.168.X.X.", user_name="5vP*************")
a.scan_lights()


In [17]: a.scan_lights()
+----+-------------------+-------+-----------+
| ID | NAME              | STATE | UPDATE    |
+----+-------------------+-------+-----------+
| 1  | Kitchen           | ON    | noupdates |
| 2  | Living room       | OFF   | noupdates |
| 3  | Front door        | OFF   | noupdates |
| 4  | Stairs            | OFF   | noupdates |
| 5  | GameRoom2         | OFF   | noupdates |
| 6  | GameRoom1         | OFF   | noupdates |
| 9  | Outside right     | ON    | noupdates |
| 10 | Outside main door | ON    | noupdates |
| 11 | Outside Left      | OFF   | noupdates |
| 12 | Laundry           | OFF   | noupdates |
| 13 | Outide window     | OFF   | noupdates |
| 14 | Sofi lamp         | OFF   | noupdates |
| 15 | Living room lamp  | ON    | noupdates |
| 16 | Caro lamp         | OFF   | noupdates |
| 17 | Sergio Lamp       | OFF   | noupdates |
+----+-------------------+-------+-----------+

a.light(1,False)
light 1 has been turned OFF

a.light(1,True)
light 1 has been turned ON
```