from __future__ import division
import argparse
import random
from pandas import DataFrame
from copy import deepcopy


def inputf():
    evidence_array_input = []
    query_array_input = []
    number_of_evidence,space,number_of_queries = raw_input()
    number_of_evidence = int(number_of_evidence)
    number_of_queries = int(number_of_queries)
    for i in range(0,number_of_evidence):
        input1,input2,input3 = raw_input()
        evidence_array_input.append([input1,input3])
    for i in range(0,number_of_queries):
        input1 = raw_input()
        query_array_input.append(input1)
    return(evidence_array_input,query_array_input)


def PriorSampling(evidence_array_input,query_array_input,number_of_samples):
    numerator_array = []
    output_array = []
    for i in range(0,len(evidence_array_input)):
        if evidence_array_input[i][1]=='t':
            evidence_array_input[i]=[evidence_array_input[i][0],1]
        else:
            evidence_array_input[i]=[evidence_array_input[i][0],0]
    
    #print(evidence_array_input) 
    master_output_array = []
    for j in range(0,10):
        denominator = 0
        numerator_array = []
        output_array = []
        prob=[]
        b=[]
        for i in range(number_of_samples):
            x=random.random()
            if x<=0.999:
                b.append(0)
            else:
                b.append(1)
        e=[]
        for i in range(number_of_samples):
            x=random.random()
            if x<=0.998:
                e.append(0)
            else:
                e.append(1)
        a=[]
        for i in range(number_of_samples):
            if b[i]==1 and e[i]==1:
                x=random.random()
                if x<=0.95:
                    a.append(1)
                else:
                    a.append(0)
            elif b[i]==1 and e[i]==0:
                x=random.random()
                if x<=0.94:
                    a.append(1)
                else:
                    a.append(0)
            elif b[i]==0 and e[i]==1:
                x=random.random()
                if x<=0.29:
                    a.append(1)
                else:
                    a.append(0)
            else:
                x=random.random()
                if x<=0.001:
                    a.append(1)
                else:
                    a.append(0)
        j=[]
        m=[]
        
        for i in range(number_of_samples):
            if a[i]==1:
                x=random.random()
                if x<=0.90:
                    j.append(1)
                else:
                    j.append(0)
            else:
                x=random.random()
                if x<=0.05:
                    j.append(1)
                else:
                    j.append(0)
        
        for i in range(number_of_samples):
            if a[i]==1:
                x=random.random()
                if x<=0.70:
                    m.append(1)
                else:
                    m.append(0)
            else:
                x=random.random()
                if x<=0.01:
                    m.append(1)
                else:
                    m.append(0)
        for i in range(number_of_samples):
            prob.append([b[i],e[i],a[i],j[i],m[i]])
        df = DataFrame(prob,columns = ['B','E','A','J','M'])
        for i in range(0,len(evidence_array_input)):
            df = df[df[evidence_array_input[i][0]]==evidence_array_input[i][1]]
        denominator = len(df)
        #print(df)
        for i in range(0,len(query_array_input)):
            df = df[df[query_array_input[i]]==1]
            numerator_array.append(len(df))
        if denominator ==0:
            if len(query_array_input) ==1:
                output_array.append(0)
            else:
                a = [0,0]
                output_array.append(a)
        else:   
            for i in range(0,len(numerator_array)):
                output_array.append(numerator_array[i]/denominator)
        if len(query_array_input) == 2 and denominator==0:
            master_output_array.append(output_array[0])
        else:
            master_output_array.append(output_array)
    #print(master_output_array)
    final_output_array = []
    
    for i in range(len(query_array_input)):
        summation = 0
        for j in range(10):
            summation = summation + master_output_array[j][i]
        final_output_array.append(summation/10)
    if len(query_array_input)==1:
        print(final_output_array)
    else:
        print(query_array_input[0],final_output_array[0])
        print(query_array_input[1],final_output_array[1])
    

def RejectionSampling(evidence_array_input,query_array_input,number_of_samples):
    numerator_array = []
    output_array = []
    for i in range(0,len(evidence_array_input)):
        if evidence_array_input[i][1]=='t':
            evidence_array_input[i]=[evidence_array_input[i][0],1]
        else:
            evidence_array_input[i]=[evidence_array_input[i][0],0]
    evidence_array_input_dict = dict(evidence_array_input)
    #print(evidence_array_input) 
    master_output_array = []
    for j in range(0,10):
        denominator = 0
        numerator_array = []
        output_array = []
        prob=[]
        b=[]
        e=[]
        a=[]
        j=[]
        m=[]
        master_sample_array = []
        counter = number_of_samples
        for i in range(number_of_samples):
            sample_array = [] 
            x=random.random()
            if x<=0.999:
                sample_array.append(0)
            else:
                sample_array.append(1)
            if 'B' in evidence_array_input_dict:
                if sample_array[-1]!=evidence_array_input_dict['B']:
                    continue
            x=random.random()
            if x<=0.998:
                sample_array.append(0)
            else:
                sample_array.append(1)
            if 'E' in evidence_array_input_dict:
                if sample_array[-1]!=evidence_array_input_dict['E']:
                    continue
            if sample_array[0]==1 and sample_array[1]==1:
                x=random.random()
                if x<=0.95:
                    sample_array.append(1)
                else:
                    sample_array.append(0) 
            elif sample_array[0]==1 and sample_array[1]==0:
                x=random.random()
                if x<=0.94:
                    sample_array.append(1)
                else:
                    sample_array.append(0)
            elif sample_array[0]==0 and sample_array[1]==1:
                x=random.random()
                if x<=0.29:
                    sample_array.append(1)
                else:
                    sample_array.append(0)
            else:
                x=random.random()
                if x<=0.001:
                    sample_array.append(1)
                else:
                    sample_array.append(0)
            if 'A' in evidence_array_input_dict:
                if sample_array[-1]!=evidence_array_input_dict['A']:
                    continue   
            if sample_array[2]==1:
                x=random.random()
                if x<=0.90:
                    sample_array.append(1)
                else:
                    sample_array.append(0)
            else:
                x=random.random()
                if x<=0.05:
                    sample_array.append(1)
                else:
                    sample_array.append(0)
            if 'J' in evidence_array_input_dict:
                if sample_array[-1]!=evidence_array_input_dict['J']:
                    continue
            if sample_array[2]==1:
                x=random.random()
                if x<=0.70:
                    sample_array.append(1)
                else:
                    sample_array.append(0)
            else:
                x=random.random()
                if x<=0.01:
                    sample_array.append(1)
                else:
                    sample_array.append(0)
            if 'M' in evidence_array_input_dict:
                if sample_array[-1]!=evidence_array_input_dict['J']:
                    continue
            master_sample_array.append(sample_array)
        #print(master_sample_array)
        df = DataFrame(master_sample_array,columns = ['B','E','A','J','M'])
        #print(df)
        '''for i in range(0,len(evidence_array_input)):
            df = df[df[evidence_array_input[i][0]]==evidence_array_input[i][1]]'''
        denominator = len(df)
        #print(df)
        for i in range(0,len(query_array_input)):
            df = df[df[query_array_input[i]]==1]
            numerator_array.append(len(df))
        if denominator ==0:
            if len(query_array_input) ==1:
                output_array.append(0)
            else:
                a = [0,0]
                output_array.append(a)
        else:   
            for i in range(0,len(numerator_array)):
                output_array.append(numerator_array[i]/denominator)
        if len(query_array_input) == 2 and denominator==0:
            master_output_array.append(output_array[0])
        else:
            master_output_array.append(output_array)
    #print(master_output_array)
    final_output_array = []
    for i in range(0,len(query_array_input)):
        summation = 0
        for j in range(0,10):
            summation = summation + master_output_array[j][i]
        final_output_array.append(summation/10)
    if len(query_array_input)==1:
        print(final_output_array)
    else:
        print(query_array_input[0],final_output_array[0])
        print(query_array_input[1],final_output_array[1])


def LikelihoodWeighting(evidence_array_input,query_array_input,number_of_samples):

    numerator_array = []
    output_array = []
    for i in range(0,len(evidence_array_input)):
        if evidence_array_input[i][1]=='t':
            evidence_array_input[i]=[evidence_array_input[i][0],1]
        else:
            evidence_array_input[i]=[evidence_array_input[i][0],0]
    evidence_array_input_dict = dict(evidence_array_input)
    #print(evidence_array_input) 
    master_output_array = []
    
    for j in range(0,10):
        denominator = 0
        numerator_array = []
        output_array = []
        prob=[]
        b=[]
        e=[]
        a=[]
        j=[]
        m=[]
        master_sample_array = []
        master_weight_positive = 0
        number_of_positive = 0
        master_weight_negative = 0
        number_of_negative = 0
        counter = number_of_samples
        for i in range(number_of_samples):
            sample_array = [] 
            sample_weight = 1
            if 'B' in evidence_array_input_dict:
                sample_array.append(evidence_array_input_dict['B'])
                if sample_array[-1] == 0:               
                    sample_weight = sample_weight*0.999
                else:
                    sample_weight = sample_weight*0.001
                    #print("sample_weight B",sample_weight)
            else:
                x=random.random()
                if x<=0.999:
                    sample_array.append(0)
                else:
                    sample_array.append(1)
            if 'E' in evidence_array_input_dict:
                sample_array.append(evidence_array_input_dict['E'])
                if sample_array[-1] == 0:               
                    sample_weight = sample_weight*0.998
                else:
                    sample_weight = sample_weight*0.002
                    #print("sample_weight E",sample_weight)
            else:
                x=random.random()
                if x<=0.998:
                    sample_array.append(0)
                else:
                    sample_array.append(1)
            if 'A' in evidence_array_input_dict:
                sample_array.append(evidence_array_input_dict['A'])
                if sample_array[0]==1 and sample_array[1]==1:
                    sample_weight = sample_weight*0.95
                elif sample_array[0]==1 and sample_array[1]==0:
                    sample_weight = sample_weight*0.94
                elif sample_array[0]==0 and sample_array[1]==1:
                    sample_weight = sample_weight*0.29
                else:
                    sample_weight = sample_weight*0.001
            else:
                if sample_array[0]==1 and sample_array[1]==1:
                    x=random.random()
                    if x<=0.95:
                        sample_array.append(1)
                    else:
                        sample_array.append(0) 
                elif sample_array[0]==1 and sample_array[1]==0:
                    x=random.random()
                    if x<=0.94:
                        sample_array.append(1)
                    else:
                        sample_array.append(0)
                elif sample_array[0]==0 and sample_array[1]==1:
                    x=random.random()
                    if x<=0.29:
                        sample_array.append(1)
                    else:
                        sample_array.append(0)
                else:
                    x=random.random()
                    if x<=0.001:
                        sample_array.append(1)
                    else:
                        sample_array.append(0)
            #print("sample_weight A",sample_weight)
            if 'J' in evidence_array_input_dict:
                sample_array.append(evidence_array_input_dict['J'])
                if sample_array[2]==1:
                    sample_weight = sample_weight*0.9
                else:
                    sample_weight = sample_weight*0.05
            else:           
                if sample_array[2]==1:
                    x=random.random()
                    if x<=0.90:
                        sample_array.append(1)
                    else:
                        sample_array.append(0)
                else:
                    x=random.random()
                    if x<=0.05:
                        sample_array.append(1)
                    else:
                        sample_array.append(0)
            #print("sample_weight J",sample_weight)
            if 'M' in evidence_array_input_dict:    
                sample_array.append(evidence_array_input_dict['M'])
                if sample_array[2]==1:
                    sample_weight = sample_weight*0.7
                else:
                    sample_weight = sample_weight*0.01
            else:               
                if sample_array[2]==1:
                    x=random.random()
                    if x<=0.70:
                        sample_array.append(1)
                    else:
                        sample_array.append(0)
                else:
                    x=random.random()
                    if x<=0.01:
                        sample_array.append(1)
                    else:
                        sample_array.append(0) 
            #print("sample_weight M",sample_weight)
            master_sample_array.append(sample_array)
            if 'B' in query_array_input:
                if sample_array[0]==1:
                    #master_weight_positive = master_weight_positive + sample_weight*0.001
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                else:
                    #master_weight_negative = master_weight_negative + sample_weight*0.999
                    number_of_negative = number_of_negative+1
                    master_weight_negative = master_weight_negative + sample_weight
            elif 'E' in query_array_input:
                if sample_array[1]==1:
                    #master_weight_positive = master_weight_positive + sample_weight*0.002
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                else:
                    #master_weight_negative = master_weight_negative + sample_weight*0.998
                    master_weight_negative = master_weight_negative + sample_weight
                    number_of_negative = number_of_negative+1
            elif 'A' in query_array_input:
                if sample_array[2]==1 and sample_array[0]==1 and sample_array[1]==1:
                    #master_weight_positive = master_weight_positive + sample_weight*0.95
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                elif sample_array[2]==1 and sample_array[0]==1 and sample_array[1]==0:
                    #master_weight_positive = master_weight_positive + sample_weight*0.94
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                elif sample_array[2]==1 and sample_array[0]==0 and sample_array[1]==1:
                    #master_weight_positive = master_weight_positive + sample_weight*0.29
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                elif sample_array[2]==1 and sample_array[0]==0 and sample_array[1]==0:
                    #master_weight_positive = master_weight_positive + sample_weight*0.001
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                elif sample_array[2]==0 and sample_array[0]==1 and sample_array[1]==1:
                    #master_weight_negative = master_weight_negative + sample_weight*0.05
                    master_weight_negative = master_weight_negative + sample_weight
                    number_of_negative = number_of_negative+1
                elif sample_array[2]==0 and sample_array[0]==1 and sample_array[1]==0:
                    #master_weight_negative = master_weight_negative + sample_weight*0.06
                    master_weight_negative = master_weight_negative + sample_weight
                    number_of_negative = number_of_negative+1
                elif sample_array[2]==0 and sample_array[0]==0 and sample_array[1]==1:
                    #master_weight_negative = master_weight_negative + sample_weight*0.71
                    master_weight_negative = master_weight_negative + sample_weight
                    number_of_negative = number_of_negative+1
                elif sample_array[2]==0 and sample_array[0]==0 and sample_array[1]==0:
                    #master_weight_negative = master_weight_negative + sample_weight*0.999
                    master_weight_negative = master_weight_negative + sample_weight
                    number_of_negative = number_of_negative+1
            elif 'J' in query_array_input:
                if sample_array[3]==1 and sample_array[2]==1:
                    #master_weight_positive = master_weight_positive + sample_weight*0.90
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                elif sample_array[3]==1 and sample_array[2]==0:
                    #master_weight_positive = master_weight_positive + sample_weight*0.05
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                elif sample_array[3]==0 and sample_array[2]==1:
                    #master_weight_negative = master_weight_negative + sample_weight*0.10
                    master_weight_negative = master_weight_negative + sample_weight
                    number_of_negative = number_of_negative+1
                elif sample_array[3]==0 and sample_array[2]==0:
                    #master_weight_negative = master_weight_negative + sample_weight*0.95
                    master_weight_negative = master_weight_negative + sample_weight
                    number_of_negative = number_of_negative+1
            elif 'M' in query_array_input:
                if sample_array[4]==1 and sample_array[2]==1:
                    #master_weight_positive = master_weight_positive + sample_weight*0.70
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                elif sample_array[4]==1 and sample_array[2]==0:
                    #master_weight_positive = master_weight_positive + sample_weight*0.01
                    master_weight_positive = master_weight_positive + sample_weight
                    number_of_positive =number_of_positive+1
                elif sample_array[4]==0 and sample_array[2]==1:
                    #master_weight_negative = master_weight_negative + sample_weight*0.30
                    master_weight_negative = master_weight_negative + sample_weight
                    number_of_negative = number_of_negative+1
                elif sample_array[4]==0 and sample_array[2]==0:
                    #master_weight_negative = master_weight_negative + sample_weight*0.99
                    master_weight_negative = master_weight_negative + sample_weight
                    number_of_negative = number_of_negative+1
            #print(master_weight_positive,master_weight_negative)
        #print(master_sample_array)
        df = DataFrame(master_sample_array,columns = ['B','E','A','J','M'])
        #print(df)
        #print(master_weight_positive,master_weight_negative)    
        #print(master_weight_positive/(master_weight_positive+master_weight_negative))
        master_output_array.append(master_weight_positive/(master_weight_positive+master_weight_negative))
    output = 0
    for i in range(0,len(master_output_array)):
        output = output+ master_output_array[i]
    print(output/10)
    
  


def Enumeration(evidence_array_input,query_array_input,list_of_nodes):

    
    def enumerateall(variables,evidence):
        if len(variables)==0:
            #print("length = 0")
            return 1
    
        else:
            #print(variables)
            return_evidence = deepcopy(evidence)
            y = variables.pop(0)
            #print(y.name)
            '''for i in range(0,len(evidence)):
                print(evidence[i][0].name)'''
            #print(evidence)
            for i in range(0,len(evidence)):
                #print(y.name,evidence[i][0].name)
                if y.name == evidence[i][0].name:
                    #print(y.name)
                    set_value = evidence[i][1]
                    #print('Set Value=',set_value)
                    if set_value == 't':
                        check_array = []
                        #print(y.CPT[y.CPT.columns[-2]])
                        if len(y.parents)==0:
                            #print(2)
                            return_value = y.CPT[y.CPT.columns[-2]]
                            #print(return_value)
                        elif len(y.parents)==2:
                            #print(evidence)
                            #print(y.parents)
                            for j in range(0,len(evidence)):
                                #print(evidence[j][0].name)
                                for k in range(0,len(y.parents)):
                                    if evidence[j][0].name == y.parents[k].name:
                                        check_array.append(evidence[j][1])
                            #print(check_array)
                            #print(y.CPT[y.CPT['B']==check_array[0]][y.CPT['E']==check_array[1]][[-2]])
                            return_value = y.CPT[y.CPT['B']==check_array[0]][y.CPT['E']==check_array[1]][[-2]]
                            #print(return_value)
                        else:
                            check_value = ''
                            #print(1)
                            for j in range(0,len(evidence)):
                                #print(evidence[j][0].name)
                                for k in range(0,len(y.parents)):
                                    if evidence[j][0].name == y.parents[k].name:
                                        check_value = evidence[j][1]
                            return_value = y.CPT[y.CPT['A']==check_value][[-2]]
                            #print(return_value)
                        return((return_value.values[0])*enumerateall(variables,evidence))
                    else:
                        #print("False Case")
                        check_array = []
                        if len(y.parents)==0:
                            #print("B is False")
                            return_value = y.CPT[y.CPT.columns[-1]]
                            #print(return_value)
                        elif len(y.parents)==2:
                            for j in range(0,len(evidence)):
                                #print(evidence[j][0].name)
                                for k in range(0,len(y.parents)):
                                    if evidence[j][0].name == y.parents[k].name:
                                        check_array.append(evidence[j][1])
                            return_value = y.CPT[y.CPT['B']==check_array[0]][y.CPT['E']==check_array[1]][[-1]]
                            #print(return_value)
                        else:
                            check_value = ''
                            for j in range(0,len(evidence)):
                                #print(evidence[j][0].name)
                                for k in range(0,len(y.parents)):
                                    if evidence[j][0].name == y.parents[k].name:
                                        check_value = evidence[j][1]
                            return_value = y.CPT[y.CPT['A']==check_value][[-1]]
                            #print(return_value)
                        #print(variables)
                        return((return_value.values[0])*enumerateall(variables,evidence))
            #print(y.CPT[y.CPT.columns[-2]],y.CPT[y.CPT.columns[-1]])
            evidence1 = deepcopy(evidence)
            evidence2 = deepcopy(evidence)
            variables1 = deepcopy(variables)
            variables2 = deepcopy(variables)
            evidence1.append([y,'t'])
            #print("Evidences",evidence,"Evidence1=",evidence1)
            evidence2.append([y,'f'])
            check_array = []
            #print(y.name)
            if len(y.parents)==0:
                return_value1 = y.CPT[y.CPT.columns[-2]]
                return_value2 = y.CPT[y.CPT.columns[-1]]
                #print(return_value1)
                #print(return_value2)
            elif len(y.parents)==2:
                for j in range(0,len(evidence)):
                    #print(evidence[j][0].name)
                    for k in range(0,len(y.parents)):
                        if evidence[j][0].name == y.parents[k].name:
                            check_array.append(evidence[j][1])
                return_value1 = y.CPT[y.CPT['B']==check_array[0]][y.CPT['E']==check_array[1]][[-2]]
                return_value2 = y.CPT[y.CPT['B']==check_array[0]][y.CPT['E']==check_array[1]][[-1]]
                #print(return_value1)
                #print(evidence1)
                #print(return_value2)
                #print(evidence2)
            else:
                check_value = ''
                for j in range(0,len(evidence)):
                    #print(evidence[j][0].name)
                    for k in range(0,len(y.parents)):
                        if evidence[j][0].name == y.parents[k].name:
                            check_value = evidence[j][1]
                return_value1 = y.CPT[y.CPT['A']==check_value][[-2]]
                return_value2 = y.CPT[y.CPT['A']==check_value][[-1]]
                #print(return_value1)
                #print(return_value2)
            #print('sumout',(return_value1)*enumerateall(variables,evidence1),(return_value2)*enumerateall(variables,evidence2))
            #print(variables)
            return(return_value1.values[0]*enumerateall(variables1,evidence1) + return_value2.values[0]*enumerateall(variables2,evidence2))
    
    def ask(query,evidence,bayesnet):
        Q = []
        types = ['t','f']
        variables = deepcopy(bayesnet)
        #print(variables)
        for i in range(0,len(types)):
            #print([query,types[i]])
            evidence.append([query,types[i]])
            a = enumerateall(variables,evidence)
            del evidence[-1]
            #print("Evidenceask",evidence)
            #print(a)
            Q.append(a)
            variables = deepcopy(bayesnet)
            #print(variables)
        #print(Q[0])
        #print(Q[1])
        value = Q[0]/(Q[0]+Q[1])
        #print(value)
        #print(1-value)
        #return(value)
        return(value)
    #query1 = query_array_input[0]
    evidence_array = evidence_array_input
    query_array=query_array_input
    #list_of_nodes=class1()
    probability_array = []
    final_probability = 1
    #probability = ask(query_array_input,evidence_array,list_of_nodes)
    evidence_array2 = deepcopy(evidence_array)
    for i in range(0,len(query_array)):
        query1 = query_array[i]
        probability = ask(query1,evidence_array,list_of_nodes)
        probability_array.append(probability[0])
        evidence_array = evidence_array2
        #evidence_array.append([query1,'t'])
    if len(query_array_input)==1:
        print(probability_array)
    else:
        print(query_array_input[0].name,probability_array[0])
        print(query_array_input[1].name,probability_array[1])
    for i in range(0,len(probability_array)):
        final_probability = final_probability*probability_array[i]
    #print(round(final_probability,7))
    #print(probability)
    
def input_Bayes_network():
    a = [['t','t',0.95,0.05],['t','f',0.94,0.06],['f','t',0.29,0.71],['f','f',0.001,0.999]]
    e = [[0.002,0.998]]
    b = [[0.001,0.999]]
    j = [['t',0.9,0.1],['f',0.05,0.95]]
    m = [['t',0.7,0.3],['f',0.01,0.99]]
    a_dataframe = DataFrame(a,columns = ['B','E','P(A|B,E)','P(~A|B,E)'])
    e_dataframe = DataFrame(e,columns = ['P(E)','P(~E)'])
    b_dataframe = DataFrame(b,columns = ['P(B)','P(~B)'])
    j_dataframe = DataFrame(j,columns = ['A','P(J|A)','P(~J|A)'])
    m_dataframe = DataFrame(m,columns = ['A','P(M|A)','P(~M|A)'])
    return(b_dataframe,e_dataframe,a_dataframe,j_dataframe,m_dataframe)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',action='store',nargs=1)
    parser.add_argument('count',action='store',type=int,nargs='?')
    x=parser.parse_args()
    number_of_samples= x.count
        
    class node(object):
        def __init__(self):
            self.name = ''
            self.parents = []
            self.children = []
            self.CPT = [[]]
    b_dataframe,e_dataframe,a_dataframe,j_dataframe,m_dataframe = input_Bayes_network()
    A = node()
    A.name = 'A'
    B = node()
    B.name = 'B'
    E = node()
    E.name = 'E'
    J = node()
    J.name = 'J'
    M = node()
    M.name = 'M'
    B.children.append(A)
    B.CPT = b_dataframe
    E.children.append(A)
    E.CPT = e_dataframe
    A.parents.append(B)
    A.parents.append(E)
    A.children.append(J)
    A.children.append(M)
    A.CPT = a_dataframe
    J.parents.append(A)
    J.CPT = j_dataframe
    M.parents.append(A)
    M.CPT = m_dataframe
    list_of_nodes = [B,E,A,J,M]
    evidence_array = []
    query_array = []
    if x.mode==['e']:
        evidence_array_input,query_array_input=inputf()
        for i in range(0,len(evidence_array_input)):
            for j in range(0,len(list_of_nodes)):
                if evidence_array_input[i][0]==list_of_nodes[j].name:
                    evidence_array.append([list_of_nodes[j],evidence_array_input[i][1]])
    #print(evidence_array)
        for i in range(0,len(query_array_input)):
            for j in range(0,len(list_of_nodes)):
                if query_array_input[i]==list_of_nodes[j].name:
                    query_array.append(list_of_nodes[j]) 
        Enumeration(evidence_array,query_array,list_of_nodes)
        #print('success')
    elif x.mode==['p']:
        evidence_array_input,query_array_input=inputf()
        PriorSampling(evidence_array_input,query_array_input,number_of_samples)        
    elif x.mode==['r']:
        evidence_array_input,query_array_input=inputf()
        RejectionSampling(evidence_array_input,query_array_input,number_of_samples)
    elif x.mode==['l']:
        evidence_array_input,query_array_input=inputf()
        LikelihoodWeighting(evidence_array_input,query_array_input,number_of_samples)
    else:
        print("Wrong mode provided")
