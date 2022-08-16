def confusion():
    acc = (TP+TN)/(TP+TN+FP+FN)
    pre = (TP/(TP+FP))
    NPV = (TN/(TN+FN))
    rec = (TP/(TP+FN))
    spec = (TN/(TN+FP))
    print(
    f'''
    _______________________________________________
    True Positive = {TP} ---- False Positive = {FP}
    True Negative = {TN} ---- False Negative = {FN}
    
    Out of {TP+FN+FP+FN} predictions
    
        Accuracy = {acc:.2%}
       Precision = {pre:.2%}
             NPV = {NPV:.2%}
          Recall = {rec:.2%}
     Specificity = {spec:.2%}
    _______________________________________________
    '''
    )
