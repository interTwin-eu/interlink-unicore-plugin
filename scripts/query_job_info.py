"""
 This script should be executed by end-user to view unicore job details
"""
import pyunicore.credentials as uc_credentials
import pyunicore.client as uc_client
import json
import sys

if len(sys.argv) < 2:
        print ("Job id is missing")
        print ("Usage: python job_details.py <UNICORE_JOB_ID>")
        quit()

job_id=sys.argv[1]


print("job_id:",job_id)

#unicore site url
# In case of HDFML it should be "https://zam2125.zam.kfa-juelich.de:9112/HDFML/rest/core"
base_url = "https://<HOST>:<PORT>/<SITE_NAME>/rest/core"


# Configure your Judoor username and password below
credential = uc_credentials.UsernamePassword("<JUDOOR_USERNAME>", "<JUDOOR_PASSWORD>")

client = uc_client.Client(credential, base_url)

job = uc_client.Job(security=credential,job_url=base_url+"/jobs/"+job_id)

print("Job status: ",job.status)
print("#################################################")
print(json.dumps(job.properties, indent=2))

print("#################################################")
work_dir = job.working_dir
stderr = work_dir.stat("/stderr")
print(json.dumps(stderr.properties, indent = 2))
content_err = stderr.raw().read()
print("job output: ", content_err)
print("#################################################")
stdout = work_dir.stat("/stdout")
print(json.dumps(stdout.properties, indent = 2))
content_out = stdout.raw().read()
print("job output: ", content_out)
