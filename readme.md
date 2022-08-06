# Mantel Group Technical Interview Submission

This is my submission for the technical excercise assigned as part
of the Mantel Groups Future Associates Program interview process.

This program takes in a .log file containing network log data in the following form:

```
72.44.32.10 - - [09/Jul/2018:15:48:07 +0200] "GET / HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0" junk extra
```

and outputs the top 3 most visited IP's, the most visited URL's and the number of unique IP adresses.

## How to run this program
To run this program, use the following command in the directory containing main.py

```
python3 main.py
```