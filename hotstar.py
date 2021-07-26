#!/usr/bin/env python
#IMPORTING LIBRARIES

#DEVELOPED BY SURAJ
import requests
import sys
#declaring class
class generateURL(object):

    def __init__(self):

        self._url = raw_input("Enter the hotstar URL to open in hsplayer:")

        self._path_parameter = str(self._url).split('/')

        self._id = self._path_parameter[len(self._path_parameter)-1]

    def getMethod(self):

        url_part1='http://getcdn.hotstar.com/AVS/besc?action=GetCDN&asJson=Y&channel=TABLET&id='

        url_part2='&type=VOD'

        final_url = url_part1 + str(self._id) + url_part2



        try:

             response=requests.get(final_url)

             status = response.status_code

             if status == 200 :

                  data = response.json()
  
                  src = data["resultObj"]["src"]

                  print("Open https://www.hlsplayer.net/ and paste the below url in the box")

                  print(src)

             else:
 
                  print("Please recheck the URL")


        except Exception as e:

              print("Error occured is :" ,e)

              print("Please recheck the URL")



initiate = generateURL()

initiate.getMethod()

        

        

        
