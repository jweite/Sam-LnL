import json
import re
import ptvsd

# Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
#ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
#ptvsd.wait_for_attach()

def lambda_handler(event, context):
    if 'body' in event and isinstance(event['body'], str):
        event = json.loads(event['body'])

    spl = re.split(r'(\+)', event['formula'])
    a = float(spl[0])
    op = spl[1]
    b = float(spl[2])

    retVal = {}
    if op == '+':
       retVal['answer'] = a + b
    else:
       return {"statusCode": 500, "body": "Unknown operator in formula"}
 
    return {"statusCode": 200, "headers": { "Content-type": "application/json" }, "body": json.dumps(retVal)}


if __name__ == "__main__":
    result = lambda_handler({"formula" : '2 + 3'}, None)
    print('Result = ', result)
