import json
from optparse import OptionParser
#from datetime import datetime, timezone
#from dateutil.relativedelta import relativedelta


parser = OptionParser()
(options, args) = parser.parse_args()

PAYLOADS = args
assert len(args) > 0, "must specify payload file(s)"

def get_actions(payload_f):
    f = open(payload_f)
    content = json.loads(f.read())
    return content['actions']

def assemble_tx(payload_f, actions):
    f = open(payload_f)
    content = json.loads(f.read())
    content['actions'] = actions
    return content

actions = []
payload_f = ""
for payload_f in PAYLOADS: 
    actions.extend(get_actions(payload_f))

print(actions)

tx = assemble_tx(payload_f, actions)

f = open("tx.json", "w")
json.dump(tx, f, indent=4)
f.close()
print("the output is in: tx.json")
