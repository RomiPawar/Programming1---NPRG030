class Element:
    def __init__(self, x, next):
        self.x = x
        self.next = next

def PrintLSS( p ):
    print( "LSS:", end=" " )
    while p!=None:
        print( p.x, end=" " )
        p = p.next
    print(".")

def ReadLSS():
    """Reads LSS"""
    first = None
    last = None
    r = input()
    while r!="":
        line = r.split()
        if len(line)==0:
            break
        for s in line:
            p = Element(int(s),None)
            if first==None:
                first = p
            else:
                last.next = p
            last = p
        r = input()
    return first

#################################################

def IntersectionDestruct(a,b):
    """ the destructive intersection of two ordered lists
    * does not create any new elements, the resulting list will be composed of the elements of the original lists,
    * the result is a SET, so the values are not repeated """
    #q = None
    p = a
    prev = None
    while p is not None and b is not None:
        if p.x == b.x:
            prev = p
            p = p.next
            b = b.next

        elif p.x < b.x:
            if prev is not None:
                prev.next = p.next
            p = p.next
        else:
            b = b.next
            
            if prev is not None:
                prev.next = None
    return a

#################################################

PrintLSS( IntersectionDestruct( ReadLSS(), ReadLSS() ) )
