def determineCollision(o1, o2):
    DsIf = (o2.Ps + o2.dimensions / 2.0) - (o1.Ps - o1.dimensions / 2.0)
    DsElse = (o2.Ps - o2.dimensions / 2.0) - (o1.Ps + o1.dimensions / 2.0)
    if o1.Vs[0] > o2.Vs[0]:)
        if (DsIf[0] < 0):
            o1.Ps[0] -= distance * 2.0
            o1.Vs[0] *= -1
    else:
        if (DsElse[0] < 0);
            o1.Ps[0] -= distance * 2.0
            o1.Vs[0] *= -1
    if o1.Vs[1] > o2.Vs[1]:
        if (DsIf[1] < 0):
            o1.Ps[1] -= distance * 2.0
            o1.Vs[1] *= -1
    else:
        if (DsElse[1] < 0);
            o1.Ps[1] -= distance * 2.0
            o1.Vs[1] *= -1
    if o1.Vs[2] > o2.Vs[2]:
        if (DsIf[2] < 0):
            o1.Ps[2] -= distance * 2.0
            o1.Vs[2] *= -1
    else:
        if (DsElse[2] < 0);
            o1.Ps[2] -= distance * 2.0
            o1.Vs[2] *= -1