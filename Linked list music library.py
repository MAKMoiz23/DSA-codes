import time
class FavNode():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class MySong:
    # you can add further functions / attributes
    def __init__(self, title = None, artist = None):
        self.title = title
        self.artist = artist

class JukeNode:
    # you can add further functions / attributes
    def __init__(self, mysong):
        self.mySong = mysong
        self.info = MySong()
        self.next = None
        self.previous = -1
        self.count = 0

class JukeBox:
    # you can add further functions / attributes
    def __init__(self):
        # initialize lists to store playlist and favorites
        self.playlist_head = None
        self.playlist_tail = None
        self.favt_head = None

    def InsertSong(self, title, artist):
        # create a node and add in the list
        jn = JukeNode(title)
        jn.info.title = title
        jn.info.artist = artist

        if self.playlist_head is None:
            self.playlist_head = jn
            self.playlist_tail = self.playlist_head
            return

        self.playlist_head.previous = jn  # to set previous value of pre existing head equals to node object created
        jn.next = self.playlist_head
        jn.previous = None
        self.playlist_head = jn

    def PlayList(self):
        itr = self.playlist_tail

        while itr:
            print(f'-Playing {itr.mySong}-', end='\n')
            time.sleep(0.4)
            itr = itr.previous

    def PlayFav(self):
        x = self.favt_head

        def rev(x):
            if x.next is None:
                return
            x = x.next
            rev(x)
            print(x.val, end=' ')

        rev(x)
        print(self.favt_head.val)

    def Search(self, e):
        if self.playlist_head.mySong == e:
            return self.playlist_head

        elif self.playlist_tail.mySong == e:
            return self.playlist_tail

        itr = self.playlist_head.next
        while itr:
            if itr.mySong == e:
                return itr
            itr = itr.next

        return None

    def PlaySong(self, title):
        x = self.Search(title)

        if x is None:
            return
        x.count += 1
        print(f'-Playing {x.mySong}-')

    def AddToFav(self, title):
        x=self.GetFav()
        a=self.Search(title)

        if title in x or a is None:
            return

        if a.count >= 3:
            t=a.mySong
            n=FavNode(t)
            n.next=self.favt_head
            self.favt_head=n
            return f'{t} has been added to favourites'
        return

    def GetFav(self):
        itr = self.favt_head
        arr = []
        while itr:
            arr.append(itr.val)
            itr = itr.next
        return arr

    def DeleteSong(self, title):
        if self.playlist_head.mySong == title and self.playlist_tail.mySong == title:
            print(f'{self.playlist_head.mySong} has been removed from playlist')
            self.playlist_head = None
            self.playlist_tail = None
            self.DeleteFromFav(title)
            return

        elif self.playlist_head.mySong == title:
            print(f'{self.playlist_head.mySong} has been removed from playlist')
            h = self.playlist_head
            self.playlist_head = self.playlist_head.next
            self.playlist_head.previous = None
            self.DeleteFromFav(title)
            del h
            return

        elif self.playlist_tail.mySong == title:
            print(f'{self.playlist_tail.mySong} has been removed from playlist')
            t = self.playlist_tail
            self.playlist_tail = self.playlist_tail.previous
            self.playlist_tail.next = None
            self.DeleteFromFav(title)
            del t
            return

        itr = self.playlist_head
        while itr:
            if itr.mySong == title:
                print(f'{itr.mySong} has been removed from playlist')
                self.DeleteFromFav(title)
                i_n = itr.next
                i_p = itr.previous
                i_p.next = i_n
                i_n.previous = i_p
                del itr
                break
            itr = itr.next
            if itr:
                continue
            raise Exception("No such value exists in the list!")

    def DeleteFromFav(self, title):
        if self.favt_head.val == title:
            self.favt_head = self.favt_head.next
            return

        itr = self.favt_head
        while itr.next:
            if itr.next.val == title:
                itr.next = itr.next.next
                return
            itr = itr.next
            if itr:
                continue
            raise Exception("No such value exists in the list!")

    def Sort(self):
        itr = self.playlist_head
        arr = []
        while itr:
            arr.append(itr.info)
            itr = itr.next

        def MergeSort(arr, l=0, r=0):
            if l >= r:
                return

            l = 0
            r = len(arr)
            mp = (l + r) // 2

            left = arr[:mp]
            right = arr[mp:]
            # print(left,right)
            # print(f'-->{arr}')
            MergeSort(left, l, mp)
            MergeSort(right, mp + 1, r)

            Merge(left, right, arr)
            # print(f'-*{arr}')

        def Merge(a, b, arr):
            len_a = len(a)
            len_b = len(b)
            i = j = k = 0

            while i < len_a and j < len_b:
                if ord(a[i].artist[0]) < ord(b[j].artist[0]):
                    arr[k] = a[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = b[j]
                    j += 1
                    k += 1

            while i < len_a:
                arr[k] = (a[i])
                i += 1
                k += 1

            while j < len_b:
                arr[k] = b[j]
                j += 1
                k += 1

        MergeSort(arr, 0, len(arr))
        return arr

def Main():
    j=JukeBox()
    j.InsertSong('Daemon', 'Imagine Dragons')
    j.InsertSong('Childhood', 'Rauf Faik')
    j.InsertSong('Hymn for the weekend', 'Coldplay')
    j.InsertSong('Stressed out', 'Twenty one pilots')
    j.PlaySong('Daemon')
    j.PlaySong('Daemon')
    j.PlaySong('Daemon')
    print(j.AddToFav('Daemon'))
    j.PlaySong('Childhood')
    j.PlaySong('Stressed out')
    j.PlaySong('Stressed out')
    j.PlaySong('Childhood')
    j.PlaySong('Childhood')
    print(j.AddToFav('Childhood'))
    j.PlaySong('Stressed out')
    j.PlaySong('Hymn for the weekend')
    print(j.AddToFav('Hymn for the weekend'))
    print(j.GetFav())
    j.DeleteSong('Daemon')
    j.PlayFav()
    # print(j.playlist_tail.mySong)
    # j.PlayList()
    # print(j.Sort())
    j.DeleteSong('Hymn for the weekend')
    # j.DeleteSong('Childhood')
    print(j.GetFav())
    # j.DeleteSong('Daemon')
    j.InsertSong('Jane Na Tu', 'Ali Khan')
    j.InsertSong('Gumaan', 'Young stunners')
    j.PlayList()
Main()
