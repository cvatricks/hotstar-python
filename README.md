Ubuntu Hotstar users are facing a issue where they could not play the videos as hotstar does not support plugins to play on Ubuntu browsers.
However third party website https://hsplayer.net is capable of playing a processed URL.
Python script in this repository prints a processed URL that can be used in HLSPLAYER

For eg :
python hotstar.py
Enter the hotstar URL to open in hsplayer:http://www.hotstar.com/movies/baahubali-2-the-conclusion/1000118379
Open https://www.hlsplayer.net/ and paste the below url in the box
https://staragvod3-vh.akamaihd.net/i/videos/worldwide/movies/malayalam/1000118379/1000118379_,180,400,800,1300,2000,6000,_STAR.mp4.csmil/master.m3u8?subtitle_identifier=1000118379&hdnea=st=1504061125~exp=1504061725~acl=/*~hmac=20449c180aa6078a89bbb5d926d7feb0c12e732734c7d8ffdd6b8880216341b9
