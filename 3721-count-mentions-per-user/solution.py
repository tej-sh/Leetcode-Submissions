class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        def eventkey(event):
            ts=int(event[1])
            type=0 if event[0]=='OFFLINE' else 1
            return (ts,type)
        hjdsbfjfhd=sorted(events, key=eventkey)
        offline=[0]*numberOfUsers
        mention=[0]*numberOfUsers
        for event in hjdsbfjfhd:
            type,tstr,data=event
            ts=int(tstr)
            if type=='OFFLINE':
                id=int(data)
                ot=ts+60
                if offline[id]<ot:
                    offline[id]=ot
            else:
                mstriwiw=data
                t=mstriwiw.split()
                curmen=[]
                for i in t:
                    if i.startswith('id'):
                        ustr=i[2:]
                        uid=int(ustr)
                        curmen.append(uid)
                    elif i=='ALL':
                        curmen.extend(range(numberOfUsers))
                    elif i=="HERE":
                        for uid in range(numberOfUsers):
                            if offline[uid]<=ts:
                                curmen.append(uid)
                for uid in curmen:
                    mention[uid]+=1
        return mention
