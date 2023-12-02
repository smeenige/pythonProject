import csv
import requests
import sys
#from requests.auth import HTTPBasicAuth
from requests.sessions import Session

url = "https://prometheus-prod-10-prod-us-central-0.grafana.net/api/prom"
username = "325054"
password = "eyJrIjoiZmUyYzBjZjU2YmNjMGVhNTY0YTI2YWJlMDM2ZWQ0MjAyNDU5NDRhNCIsIm4iOiJncmFmYW5hY2xvdWQtc2l2YXJvc2lyZWRkeW1lZW5pZ2UtcHJvbSIsImlkIjo1OTg5NDJ9"

"""
A simple program to print the result of a Prometheus query as CSV.
"""

if len(sys.argv) != 2:
    print('Usage: {0} promql_query'.format(sys.argv[0]))
    sys.exit(1)
try:
    #response = requests.get('{0}/api/v1/query'.format(sys.argv[1]),auth=(username, password),params={'query': sys.argv[2]})
    session = Session()
    session.auth = (username,password)
    response = session.get('{0}/api/v1/query'.format(url),params={'query': sys.argv[1]})
    #response.raise_for_status()
    #print(response.url)
    #print(response.headers)
    #print(response.status_code)
    #print(response.ok)
    #print(response.reason)
    #print(response.json())
    response.raise_for_status()
    response_code = response.status_code
    if response_code == 200:
        results_data = response.json()
        status = results_data['status']
        if (status == 'success') and ('data' in results_data):
            if results_data['data']['result'] not in ("", [], None, 0, False):
                results = results_data['data']['result']
                # Build a list of all labelnames used.
                labelnames = set()
                for result in results:
                    labelnames.update(result['metric'].keys())
                #Conicalize
                labelnames.discard('__name__')
                #labelnames.discard('timestamp')
                labelnames = sorted(labelnames)
                writer = csv.writer(sys.stdout)
                # Write the header,
                writer.writerow(labelnames + ['timestamp','value'])
                # Write the samples.
                for result in results:
                    list_data = []
                    lv = []
                    for label in labelnames:
                        list_data.append(result['metric'].get(label, ''))
                    lv = (result['value'])
                    if len(lv) !=0:
                        #list_data.append(lv[1])
                        for i in range(len(lv)):
                            list_data.append(lv[i])
                    writer.writerow(list_data)
            else:
                #print("result object empty")
                pass
        else:
            #print("empty data results")
            pass
    else:
        #print("response status is error")
        pass
except requests.exceptions.Timeout as e:
    print("Status Code::",e.response.status_code)
    print("Reason::",e.response.reason)
    print("Message::",e.response.text)
    print("Response Status::",e.response.ok)
except requests.exceptions.HTTPError as e:
    print("Status Code::",e.response.status_code)
    print("Reason::",e.response.reason)
    print("Message::",e.response.text)
    print("Response Status::",e.response.ok)
except requests.exceptions.RequestException as e:
    print("Status Code::",e.response.status_code)
    print("Reason::",e.response.reason)
    print("Message::",e.response.text)
    print("Response Status::",e.response.ok)