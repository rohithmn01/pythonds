from msilib.schema import AdminExecuteSequence
from platform import python_branch


def twoSum2(lis,t):
    for i,v in enumerate(lis):
        for j,g in enumerate(lis):
            if i == j:
                continue
            if v + g == t:
                print(i)
                print(j)
                break
        break

twoSum2([2,3,4],6)


'''
My name is Rohith, i have a total of around 8 years of experience in IT industry primarily working as linux admin, 
sytem engineer and currently working as Senior DevOps Engineer at SAP Labs Bangalore from last 4 years.
Currently i work for a team where we provision/monitor/update/maintain SAP Cloud Platform which is basically a PaaS
solution hosted on almost all IaaS providers (GCP/AWS/Azure).
We as a team work on various cutting-edge tools like 
- Terraform for infrastructure provisioning, 
- Jenkins and concourse for Continious Integration and Deployment (CI/CD)
- InfluxDB/Grafana for monitoring
- We use Managed Kubernetes service from GCP which is GKE, for one of our project which is basically to provide 
Continious Deployment tool as a service to all cnetral teams at SAP.

And apart from this i love coding in python and deliver sessions internally on opensource tools and technologies.
Leaving this tech stack aside, i love playing Badminton.

'''




