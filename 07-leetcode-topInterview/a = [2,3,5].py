a =[
  {
    "creationTimestamp": "2022-08-10T23:03:21.769-07:00",
    "description": "Testing the on-demand capacity reservations",
    "id": "2681608464150111558",
    "kind": "compute#reservation",
    "name": "test-reservation",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/sap-cp-cf-zz79-test/zones/us-central1-a/reservations/test-reservation",
    "shareSettings": {
      "shareType": "LOCAL"
    },
    "specificReservation": {
      "assuredCount": "2",
      "count": "2",
      "inUseCount": "0",
      "instanceProperties": {
        "machineType": "e2-medium",
        "minCpuPlatform": "Any CPU Platform"
      }
    },
    "specificReservationRequired": "false",
    "status": "READY",
    "zone": "https://www.googleapis.com/compute/v1/projects/sap-cp-cf-zz79-test/zones/us-central1-a"
  }
]

for i in a:
    col1 = i['id']
    col2 = i['zone'].split("/")[-1]
    col3 = i['specificReservation']['instanceProperties']['machineType']
    col4 = i['specificReservation']['count']
    col5 = int(col4) -  int(i['specificReservation']['inUseCount'])
    col6 = i['status']
    col7 = i['creationTimestamp']


    print(col1)
    print(col2)
    print(col3)
    print(col4)
    print(col5)
    print(col6)
    print(col7)
