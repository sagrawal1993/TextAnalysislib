#list of X and Y will be given
def prec_recall(Y_given, Y_predicted):
    if len(Y_given)!=len(Y_predicted):
        return (-1.0,-1.0)
    precision = 0.0
    recall = 0.0
    for i in range(len(Y_given)):
        a = Y_given[i]
        b = Y_predicted[i]
        common = set(a).intersection(set(b))
        if len(b)!=0:
            prec = len(common)/len(b)
        else:
            prec = 0

        if len(a)!=0:
            reca = len(common)/len(a)
        else:
            reca = 1

        precision +=prec
        recall += reca

    precision/=len(Y_given)
    recall/=len(Y_given)
    mesure = {}
    mesure['precision'] = precision
    mesure['recall'] = recall
    return mesure