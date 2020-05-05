import MIDI as mi

fname = open("15_jazz-funk_116_fill_4-4.txt","r")
c = fname.read()
print(c)
c1=c.replace(' ','')
c1=c1.replace('\n','')
c1=bytes.fromhex(c1)
#print(c1)
#print(len(c1))
vec=mi.midi2score(c1)

for i in range(6,len(vec[1])-1):
	print(str(mi.Notenum2percussion.get(vec[1][i][4]))+' \tstart time:'+str(vec[1][i][1]))

fname = open("15_rock_100_beat_4-4.txt","r")
c = fname.read()
print(c)
c1=c.replace(' ','')
c1=c1.replace('\n','')
c1=bytes.fromhex(c1)
#print(c1)
#print(len(c1))
vec=mi.midi2score(c1)

for i in range(6,len(vec[1])-1):
	print(str(mi.Notenum2percussion.get(vec[1][i][4]))+' \tstart time:'+str(vec[1][i][1]))

