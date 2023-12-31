
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AIP APORT ARCHIVO BACKUP BODY BUCKET COPY CREATE DELETE DELETE_ALL FROM IP MODIFY NAME OPEN PATH PORT RECOVERY RENAME RUTA SERVER STRING TO TRANSFER TYPE TYPE_FROM TYPE_TOinicio : lexico\n    lexico : lexico comandos\n                | comandos\n    comandos : maincomando subcomando\n                | maincomando\n    maincomando : CREATE\n                | DELETE\n                | COPY\n                | TRANSFER\n                | RENAME\n                | MODIFY\n                | BACKUP\n                | RECOVERY\n                | DELETE_ALL\n                | OPEN\n    subcomando : subcomando sub\n                    | sub\n    sub : TYPE tipo\n            | NAME nombre\n            | BODY STRING\n            | PATH RUTA\n            | FROM RUTA\n            | TO RUTA\n            | TYPE_TO tipo\n            | TYPE_FROM tipo\n            | IP AIP\n            | PORT APORT\n    tipo : BUCKET\n            | SERVER\n    nombre : ARCHIVO\n                | STRING\n\n                | RUTA\n    '
    
_lr_action_items = {'CREATE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[5,5,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'DELETE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[6,6,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'COPY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[7,7,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'TRANSFER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[8,8,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'RENAME':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[9,9,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'MODIFY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[10,10,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'BACKUP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[11,11,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'RECOVERY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[12,12,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'DELETE_ALL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[13,13,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'OPEN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[14,14,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[0,-1,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-2,-4,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'TYPE':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[18,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,18,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'NAME':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[19,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,19,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'BODY':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[20,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,20,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'PATH':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[21,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,21,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'FROM':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[22,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,22,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'TO':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[23,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,23,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'TYPE_TO':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[24,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,24,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'TYPE_FROM':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[25,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,25,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'IP':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[26,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,26,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'PORT':([4,5,6,7,8,9,10,11,12,13,14,16,17,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[27,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,27,-17,-16,-18,-28,-29,-19,-30,-31,-32,-20,-21,-22,-23,-24,-25,-26,-27,]),'BUCKET':([18,24,25,],[30,30,30,]),'SERVER':([18,24,25,],[31,31,31,]),'ARCHIVO':([19,],[33,]),'STRING':([19,20,],[34,36,]),'RUTA':([19,21,22,23,],[35,37,38,39,]),'AIP':([26,],[42,]),'APORT':([27,],[43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'lexico':([0,],[2,]),'comandos':([0,2,],[3,15,]),'maincomando':([0,2,],[4,4,]),'subcomando':([4,],[16,]),'sub':([4,16,],[17,28,]),'tipo':([18,24,25,],[29,40,41,]),'nombre':([19,],[32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> lexico','inicio',1,'p_inicio','gramar.py',125),
  ('lexico -> lexico comandos','lexico',2,'p_lexico','gramar.py',132),
  ('lexico -> comandos','lexico',1,'p_lexico','gramar.py',133),
  ('comandos -> maincomando subcomando','comandos',2,'p_comandos','gramar.py',143),
  ('comandos -> maincomando','comandos',1,'p_comandos','gramar.py',144),
  ('maincomando -> CREATE','maincomando',1,'p_main_comando','gramar.py',158),
  ('maincomando -> DELETE','maincomando',1,'p_main_comando','gramar.py',159),
  ('maincomando -> COPY','maincomando',1,'p_main_comando','gramar.py',160),
  ('maincomando -> TRANSFER','maincomando',1,'p_main_comando','gramar.py',161),
  ('maincomando -> RENAME','maincomando',1,'p_main_comando','gramar.py',162),
  ('maincomando -> MODIFY','maincomando',1,'p_main_comando','gramar.py',163),
  ('maincomando -> BACKUP','maincomando',1,'p_main_comando','gramar.py',164),
  ('maincomando -> RECOVERY','maincomando',1,'p_main_comando','gramar.py',165),
  ('maincomando -> DELETE_ALL','maincomando',1,'p_main_comando','gramar.py',166),
  ('maincomando -> OPEN','maincomando',1,'p_main_comando','gramar.py',167),
  ('subcomando -> subcomando sub','subcomando',2,'p_subcomando','gramar.py',173),
  ('subcomando -> sub','subcomando',1,'p_subcomando','gramar.py',174),
  ('sub -> TYPE tipo','sub',2,'p_sub','gramar.py',187),
  ('sub -> NAME nombre','sub',2,'p_sub','gramar.py',188),
  ('sub -> BODY STRING','sub',2,'p_sub','gramar.py',189),
  ('sub -> PATH RUTA','sub',2,'p_sub','gramar.py',190),
  ('sub -> FROM RUTA','sub',2,'p_sub','gramar.py',191),
  ('sub -> TO RUTA','sub',2,'p_sub','gramar.py',192),
  ('sub -> TYPE_TO tipo','sub',2,'p_sub','gramar.py',193),
  ('sub -> TYPE_FROM tipo','sub',2,'p_sub','gramar.py',194),
  ('sub -> IP AIP','sub',2,'p_sub','gramar.py',195),
  ('sub -> PORT APORT','sub',2,'p_sub','gramar.py',196),
  ('tipo -> BUCKET','tipo',1,'p_tipo','gramar.py',204),
  ('tipo -> SERVER','tipo',1,'p_tipo','gramar.py',205),
  ('nombre -> ARCHIVO','nombre',1,'p_nombre','gramar.py',210),
  ('nombre -> STRING','nombre',1,'p_nombre','gramar.py',211),
  ('nombre -> RUTA','nombre',1,'p_nombre','gramar.py',213),
]
