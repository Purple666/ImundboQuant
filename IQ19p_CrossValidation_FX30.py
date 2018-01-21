"""
MIT License

Copyright (c) [2016] [Mikael Furesjö]
Software = Python Scripts in the [Imundbo Quant v1.9] series

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

IMUNDBO QUANT v1.9 (Gridsearch script)
"""
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import time
import random

TrainLocation = r'C:\Users\UserTrader\Documents\ImundboQuant\InstrumentList\IQ19p_FX30\TrainingDataset_IQ19qFX30.xlsx'


trainData = pd.read_excel(TrainLocation)
print(trainData)

_featureToCheck = "Slump"
#_featureToCheck = "_Date"
#_featureToCheck = "_Diff_CtoL"
#_featureToCheck = "_Diff_CtoH"
#_featureToCheck = "_Low34_L"
#_featureToCheck = "_PastSCH05to34"
#_featureToCheck = "_DiffU34_L3"
#_featureToCheck = "_SMA3_C"
#_featureToCheck = "_SMA89vs144"
#_featureToCheck = "_DiffD34_C"
#_featureToCheck = "_Diff_CtoO"
#_featureToCheck = "_Diff_CtoC3"
#_featureToCheck = "_PastSCH13to34"
#_featureToCheck = "_SMA13_C"
#_featureToCheck = "_Low55_L"
#_featureToCheck = "_Low10_L"
#_featureToCheck = "_sign5Stoch144"
#_featureToCheck = "_PastSCH05to13"
#_featureToCheck = "_diffStochSign144"
#_featureToCheck = "_SMA55vs89"
#_featureToCheck = "_DiffD3_C"
#_featureToCheck = "Diff_RL3_RL13"

trainData = trainData.sort(_featureToCheck, ascending=False)
print(trainData)

countX = 0

while (countX < 1000000):
    
    units = 16
    max_feat_Rand = 12
    countX = countX + 1
    time.sleep(1)
    StartTime = time.time()  
    


####---------------------------------------------------------------------------   
#### This part optimized 2016-10-10
    try: 
        units = random.randrange(17,25,1)
        #unitsHalf = units/2
        min_samples_leaf_Rand = 50 #random.randrange(20, 200, 1)# [100],
        
        #_delare2 = 0.5
        _delare1 = random.randrange(618, 850, 1)
        _delare2 = round(_delare1/1000.0001,8)
        max_feat_Rand = int(round(units * _delare2,0))
        max_leaf_nodes_Rand = 10000 #random.randrange(10000, 12000, 1)# [10000 rätt],
        min_samples_split_Rand = 150 #random.randrange(30, 300, 1)# [150 rätt],
        max_depth_Rand = 50 #random.randrange(30, 300, 1)#[150 rätt]    
        n_estimators_Rand = 50 #random.randrange(100, 250, 1)# [150 rätt]
 
    
        FEATURES = (random.sample([
                                '_PastSCH05to08',
                                '_PastSCH05to13',
                                '_PastSCH05to21',
                                '_PastSCH05to34',
                                '_PastSCH08to13',
                                '_PastSCH08to21',
                                '_PastSCH08to34',
                                '_PastSCH13to21',
                                '_PastSCH13to34',
                                '_PastSCH21to34',
                                '_Diff_CtoH',
                                '_Diff_CtoH1',
                                '_Diff_CtoH2',
                                '_Diff_CtoH3',
                                '_Diff_CtoH4',
                                '_Diff_CtoH5',
                                '_Diff_CtoH6',
                                '_Diff_CtoH7',
                                '_Diff_CtoH8',
                                '_Diff_CtoH9',
                                '_Diff_CtoH10',
                                '_Diff_CtoH11',
                                '_Diff_CtoH12',
                                '_Diff_CtoH13',
                                '_Diff_CtoH14',
                                '_Diff_CtoH15',
                                '_Diff_CtoH16',
                                '_Diff_CtoH17',
                                '_Diff_CtoH18',
                                '_Diff_CtoH19',
                                '_Diff_CtoH20',
                                '_Diff_CtoH21',
                                '_Diff_CtoH22',
                                '_Diff_CtoH23',
                                '_Diff_CtoH24',
                                '_Diff_CtoH25',
                                '_Diff_CtoL',
                                '_Diff_CtoL1',
                                '_Diff_CtoL2',
                                '_Diff_CtoL3',
                                '_Diff_CtoL4',
                                '_Diff_CtoL5',
                                '_Diff_CtoL6',
                                '_Diff_CtoL7',
                                '_Diff_CtoL8',
                                '_Diff_CtoL9',
                                '_Diff_CtoL10',
                                '_Diff_CtoL11',
                                '_Diff_CtoL12',
                                '_Diff_CtoL13',
                                '_Diff_CtoL14',
                                '_Diff_CtoL15',
                                '_Diff_CtoL16',
                                '_Diff_CtoL17',
                                '_Diff_CtoL18',
                                '_Diff_CtoL19',
                                '_Diff_CtoL20',
                                '_Diff_CtoL21',
                                '_Diff_CtoL22',
                                '_Diff_CtoL23',
                                '_Diff_CtoL24',
                                '_Diff_CtoL25',
                                '_Diff_CtoO',
                                '_Diff_CtoO1',
                                '_Diff_CtoO2',
                                '_Diff_CtoO3',
                                '_Diff_CtoO4',
                                '_Diff_CtoO5',
                                '_Diff_CtoO6',
                                '_Diff_CtoO7',
                                '_Diff_CtoO8',
                                '_Diff_CtoO9',
                                '_Diff_CtoC1',
                                '_Diff_CtoC2',
                                '_Diff_CtoC3',
                                '_Diff_CtoC4',
                                '_Diff_CtoC5',
                                '_Diff_CtoC6',
                                '_Diff_CtoC7',
                                '_Diff_CtoC8',
                                '_Diff_CtoC9',
                                '_SMA_H3',
                                '_SMA_L3',
                                '_BBU3',
                                '_BBD3',
                                '_DiffU3_C',
                                '_DiffU3_L3',
                                '_DiffD3_C',
                                '_DiffD3_H3',
                                '_BBU5',
                                '_BBD5',
                                '_DiffU5_C',
                                '_DiffU5_L3',
                                '_DiffD5_C',
                                '_DiffD5_H3',
                                '_BBU8',
                                '_BBD8',
                                '_DiffU8_C',
                                '_DiffU8_L3',
                                '_DiffD8_C',
                                '_DiffD8_H3',
                                '_BBU13',
                                '_BBD13',
                                '_DiffU13_C',
                                '_DiffU13_L3',
                                '_DiffD13_C',
                                '_DiffD13_H3',
                                '_BBU21',
                                '_BBD21',
                                '_DiffU21_C',
                                '_DiffU21_L3',
                                '_DiffD21_C',
                                '_DiffD21_H3',
                                '_BBU34',
                                '_BBD34',
                                '_DiffU34_C',
                                '_DiffU34_L3',
                                '_DiffD34_C',
                                '_DiffD34_H3',
                                '_BBU55',
                                '_BBD55',
                                '_DiffU55_C',
                                '_DiffU55_L3',
                                '_DiffD55_C',
                                '_DiffD55_H3',
                                '_BBU89',
                                '_BBD89',
                                '_DiffU89_C',
                                '_DiffU89_L3',
                                '_DiffD89_C',
                                '_DiffD89_H3',
                                '_BBU100',
                                '_BBD100',
                                '_DiffU100_C',
                                '_DiffU100_L3',
                                '_DiffD100_C',
                                '_DiffD100_H3',
                                '_BBU144',
                                '_BBD144',
                                '_DiffU144_C',
                                '_DiffU144_L3',
                                '_DiffD144_C',
                                '_DiffD144_H3',
                                '_BBU200',
                                '_BBD200',
                                '_DiffU200_C',
                                '_DiffU200_L3',
                                '_DiffD200_C',
                                '_DiffD200_H3',
                                '_BBU233',
                                '_BBD233',
                                '_DiffU233_C',
                                '_DiffU233_L3',
                                '_DiffD233_C',
                                '_DiffD233_H3',
                                '_BBU300',
                                '_BBD300',
                                '_DiffU300_C',
                                '_DiffU300_L3',
                                '_DiffD300_C',
                                '_DiffD300_H3',
                                '_BBU377',
                                '_BBD377',
                                '_DiffU377_C',
                                '_DiffU377_L3',
                                '_DiffD377_C',
                                '_DiffD377_H3',
                                '_dateDayOfYear',
                                '_dateWeekOfYear',
                                '_dateMonthOfYear',
                                '_dateDayOfMonth',
                                '_dateDayOfWeek',
                                '_EvNo5',
                                '_EvNo10',
                                '_EvNo20',
                                '_EvNo30',
                                '_EvNo40',
                                '_EvNo50',
                                '_EvNo60',
                                '_EvNo70',
                                '_EvNo80',
                                '_EvNo90',
                                '_EvNo100',
                                '_EvNo200',
                                '_EvNo300',
                                '_EvNo400',
                                '_EvNo500',
                                '_EvNo600',
                                '_EvNo700',
                                '_EvNo800',
                                '_EvNo900',
                                '_EvNo1000',
                                '_EvNo2000',
                                '_EvNo3000',
                                '_EvNo4000',
                                '_EvNo5000',
                                '_EvNo10000',
                                '_Perc3_H',
                                '_Perc5_H',
                                '_Perc8_H',
                                '_Perc13_H',
                                '_Perc21_H',
                                '_Perc34_H',
                                '_Perc55_H',
                                '_Perc89_H',
                                '_Perc100_H',
                                '_Perc144_H',
                                '_Perc200_H',
                                '_Perc233_H',
                                '_Perc377_H',
                                '_Perc3_L',
                                '_Perc5_L',
                                '_Perc8_L',
                                '_Perc13_L',
                                '_Perc21_L',
                                '_Perc34_L',
                                '_Perc55_L',
                                '_Perc89_L',
                                '_Perc100_L',
                                '_Perc144_L',
                                '_Perc200_L',
                                '_Perc233_L',
                                '_Perc377_L',
                                '_Perc3_H80',
                                '_Perc5_H80',
                                '_Perc8_H80',
                                '_Perc13_H80',
                                '_Perc21_H80',
                                '_Perc34_H80',
                                '_Perc55_H80',
                                '_Perc89_H80',
                                '_Perc100_H80',
                                '_Perc144_H80',
                                '_Perc200_H80',
                                '_Perc233_H80',
                                '_Perc377_H80',
                                '_Perc3_L20',
                                '_Perc5_L20',
                                '_Perc8_L20',
                                '_Perc13_L20',
                                '_Perc21_L20',
                                '_Perc34_L20',
                                '_Perc55_L20',
                                '_Perc89_L20',
                                '_Perc100_L20',
                                '_Perc144_L20',
                                '_Perc200_L20',
                                '_Perc233_L20',
                                '_Perc377_L20',
                                '_Perc3_M50',
                                '_Perc5_M50',
                                '_Perc8_M50',
                                '_Perc13_M50',
                                '_Perc21_M50',
                                '_Perc34_M50',
                                '_Perc55_M50',
                                '_Perc89_M50',
                                '_Perc100_M50',
                                '_Perc144_M50',
                                '_Perc200_M50',
                                '_Perc233_M50',
                                '_Perc377_M50',
                                'RL3',
                                'RL5',
                                'RL8',
                                'RL13',
                                'RL21',
                                'RL34',
                                'RL55',
                                'RL89',
                                'RL100',
                                'RL144',
                                'RL200',
                                'RL233',
                                'RL377',
                                'Diff_C_RL3',
                                'Diff_C_RL5',
                                'Diff_C_RL8',
                                'Diff_C_RL13',
                                'Diff_C_RL21',
                                'Diff_C_RL34',
                                'Diff_C_RL55',
                                'Diff_C_RL89',
                                'Diff_C_RL100',
                                'Diff_C_RL144',
                                'Diff_C_RL200',
                                'Diff_C_RL233',
                                'Diff_C_RL377',
                                'Diff_RL3_RL5',
                                'Diff_RL3_RL8',
                                'Diff_RL3_RL13',
                                'Diff_RL3_RL21',
                                'Diff_RL3_RL34',
                                'Diff_RL5_RL8',
                                'Diff_RL5_RL13',
                                'Diff_RL5_RL21',
                                'Diff_RL5_RL34',
                                'Diff_RL5_RL55',
                                'Diff_RL8_RL13',
                                'Diff_RL8_RL21',
                                'Diff_RL8_RL34',
                                'Diff_RL8_RL55',
                                'Diff_RL8_RL89',
                                'Diff_RL13_RL21',
                                'Diff_RL13_RL34',
                                'Diff_RL13_RL55',
                                'Diff_RL13_RL139',
                                'Diff_RL13_RL100',
                                'Diff_RL21_RL34',
                                'Diff_RL21_RL55',
                                'Diff_RL21_RL89',
                                'Diff_RL21_RL100',
                                'Diff_RL21_RL144',
                                'Diff_RL34_RL55',
                                'Diff_RL34_RL89',
                                'Diff_RL34_RL100',
                                'Diff_RL34_RL144',
                                'Diff_RL34_RL200',
                                'Diff_RL55_RL89',
                                'Diff_RL55_RL100',
                                'Diff_RL55_RL144',
                                'Diff_RL55_RL200',
                                'Diff_RL55_RL233',
                                'Diff_RL89_RL100',
                                'Diff_RL89_RL144',
                                'Diff_RL89_RL200',
                                'Diff_RL89_RL233',
                                'Diff_RL89_RL377',
                                'Diff_RL100_RL144',
                                'Diff_RL100_RL200',
                                'Diff_RL100_RL233',
                                'Diff_RL100_RL377',
                                'Diff_RL144_RL200',
                                'Diff_RL144_RL233',
                                'Diff_RL144_RL377',
                                'Diff_RL200_RL233',
                                'Diff_RL200_RL377',
                                'Diff_RL233_RL377',
                                '_SMA3_C',
                                '_SMA5_C',
                                '_SMA8_C',
                                '_SMA13_C',
                                '_SMA21_C',
                                '_SMA34_C',
                                '_SMA55_C',
                                '_SMA89_C',
                                '_SMA144_C',
                                '_SMA233_C',
                                '_SMA377_C',
                                '_SMA100_C',
                                '_SMA200_C',
                                '_SMA300_C',
                                '_SMA3vs5',
                                '_SMA3vs8',
                                '_SMA3vs13',
                                '_SMA3vs21',
                                '_SMA3vs34',
                                '_SMA5vs8',
                                '_SMA5vs13',
                                '_SMA5vs21',
                                '_SMA5vs34',
                                '_SMA5vs55',
                                '_SMA8vs13',
                                '_SMA8vs21',
                                '_SMA8vs34',
                                '_SMA8vs55',
                                '_SMA8vs89',
                                '_SMA13vs21',
                                '_SMA13vs34',
                                '_SMA13vs55',
                                '_SMA13vs89',
                                '_SMA13vs144',
                                '_SMA21vs34',
                                '_SMA21vs55',
                                '_SMA21vs89',
                                '_SMA21vs144',
                                '_SMA21vs233',
                                '_SMA34vs55',
                                '_SMA34vs89',
                                '_SMA34vs144',
                                '_SMA34vs233',
                                '_SMA34vs377',
                                '_SMA55vs89',
                                '_SMA55vs144',
                                '_SMA55vs233',
                                '_SMA55vs377',
                                '_SMA89vs144',
                                '_SMA89vs233',
                                '_SMA89vs377',
                                '_SMA144vs233',
                                '_SMA144vs377',
                                '_SMA233vs377',
                                '_STD3_C',
                                '_STD3sign',
                                '_STD3vsSign',
                                '_STD5_C',
                                '_STD5sign',
                                '_STD5vsSign',
                                '_STD8_C',
                                '_STD8sign',
                                '_STD8vsSign',
                                '_STD13_C',
                                '_STD13sign',
                                '_STD13vsSign',
                                '_STD21_C',
                                '_STD21sign',
                                '_STD21vsSign',
                                '_STD34_C',
                                '_STD34sign',
                                '_STD34vsSign',
                                '_STD55_C',
                                '_STD55sign',
                                '_STD55vsSign',
                                '_STD89_C',
                                '_STD89sign',
                                '_STD89vsSign',
                                '_STD144_C',
                                '_STD144sign',
                                '_STD144vsSign',
                                '_STD233_C',
                                '_STD233sign',
                                '_STD233vsSign',
                                '_STD377_C',
                                '_STD377sign',
                                '_STD377vsSign',
                                '_STD100_C',
                                '_STD100sign',
                                '_STD100vsSign',
                                '_STD200_C',
                                '_STD200sign',
                                '_STD200vsSign',
                                '_STD300_C',
                                '_STD300sign',
                                '_STD300vsSign',
                                '_stoch5',
                                '_sign5Stoch5',
                                '_diffStochSign5',
                                '_stoch5Level',
                                '_stoch14',
                                '_stoch8',
                                '_sign5Stoch8',
                                '_diffStochSign8',
                                '_stoch8Level',
                                '_stoch14',
                                '_sign5Stoch8',
                                '_diffStochSign14',
                                '_stoch14Level',
                                '_stoch21',
                                '_sign5Stoch21',
                                '_diffStochSign21',
                                '_stoch21Level',
                                '_stoch34',
                                '_sign5Stoch34',
                                '_diffStochSign34',
                                '_stoch34Level',
                                '_stoch55',
                                '_sign5Stoch55',
                                '_diffStochSign55',
                                '_stoch55Level',
                                '_stoch89',
                                '_sign5Stoch89',
                                '_diffStochSign89',
                                '_stoch89Level',
                                '_stoch144',
                                '_sign5Stoch144',
                                '_diffStochSign144',
                                '_stoch144Level',
                                '_stoch233',
                                '_sign5Stoch233',
                                '_diffStochSign233',
                                '_stoch233Level',
                                '_stoch377',
                                '_sign5Stoch377',
                                '_diffStochSign377',
                                '_stoch377Level',
                                '_stoch100',
                                '_sign5Stoch100',
                                '_diffStochSign100',
                                '_stoch100Level',
                                '_stoch200',
                                '_sign5Stoch200',
                                '_diffStochSign200',
                                '_stoch200Level',
                                '_stoch300',
                                '_sign5Stoch300',
                                '_diffStochSign300',
                                '_stoch300Level',
                                '_Low3_L',
                                '_Low4_L',
                                '_Low5_L',
                                '_Low6_L',
                                '_Low7_L',
                                '_Low8_L',
                                '_Low9_L',
                                '_Low10_L',
                                '_Low11_L',
                                '_Low12_L',
                                '_Low13_L',
                                '_Low14_L',
                                '_Low15_L',
                                '_Low17_L',
                                '_Low19_L',
                                '_Low21_L',
                                '_Low23_L',
                                '_Low25_L',
                                '_Low34_L',
                                '_Low55_L',
                                '_Low89_L',
                                '_Low144_L',
                                '_Low233_L',
                                '_Low377_L',
                                '_High3_H',
                                '_High4_H',
                                '_High5_H',
                                '_High6_H',
                                '_High7_H',
                                '_High8_H',
                                '_High9_H',
                                '_High10_H',
                                '_High11_H',
                                '_High12_H',
                                '_High13_H',
                                '_High14_H',
                                '_High15_H',
                                '_High17_H',
                                '_High19_H',
                                '_High21_H',
                                '_High23_H',
                                '_High25_H',
                                '_High34_H',
                                '_High55_H',
                                '_High89_H',
                                '_High144_H',
                                '_High233_H',
                                '_High377_H'
                                ],  units))                               
    ####---------------------------------------------------------------------------  
    
        _Horizont = ''.join(random.sample([
                                        'Tgt_SCH05to08',
                                        'Tgt_SCH05to13',
                                        'Tgt_SCH05to21',
                                        'Tgt_SCH05to34',
                                        'Tgt_SCH08to13',
                                        'Tgt_SCH08to21',
                                        'Tgt_SCH08to34',
                                        'Tgt_SCH13to21',
                                        'Tgt_SCH13to34',
                                        'Tgt_SCH21to34'
                                      ],1))
    
        _Horizontxxx = ''.join(random.sample([
                                        'Tgt_SCH05to08'                                      
                                      ],1))
    
    
   
    
    
        X = np.array(trainData[FEATURES].values) # making a np array from the pd dataset
        y = trainData[_Horizont].values # put in relevant target class
        
      
        _CV = 180 #USE 60 to slit in to seperate 3M periods or 180 to 1M periods
      
        logreg = RandomForestClassifier(n_estimators = n_estimators_Rand,
                                        max_depth = max_depth_Rand,
                                        warm_start='False',
                                        max_features=max_feat_Rand,
                                        min_samples_leaf=min_samples_leaf_Rand,
                                        bootstrap='True',
                                        max_leaf_nodes=max_leaf_nodes_Rand,
                                        min_samples_split=min_samples_split_Rand,
                                        random_state=42,
                                        n_jobs=1)

    except Exception as e:
        print(str(e))
        #pass    
    
    try:        
        from sklearn.model_selection import cross_val_score
        scores = cross_val_score(logreg, X, y, cv=_CV)
        
        _minScore = round(np.amin(scores),6)
        _maxScore = round(np.amax(scores),6)
        _meanScore = round(np.mean(scores),6)
        _stdScore = round(np.std(scores),6)
        _SharpMin = round(_minScore/_stdScore,6)
        _SharpMean = round(_meanScore/_stdScore,6)
        
        EndTime = time.time()
        TotalTime = round((EndTime - StartTime)/60,2)
        
        
        
        print(str(_minScore) + str("   ")+ str(TotalTime))

        _fileNameOfResults = str('IQ19p_')+str(_CV)+str(_featureToCheck)+str('.txt')   # put in path and filename for results       

        appendFile = open(_fileNameOfResults, 'a') # put in path and filename for results
        appendFile.write('\n' + str(_minScore)+

                        str(',Time:,')  +
                        str(TotalTime) + 

                        str(',CV:,')  +
                        str(_CV) + 
                        
                        str(',Sort:,')  +
                        str(_featureToCheck) + 
                        
                        str(',_maxScore:,')  +
                        str(_maxScore) +    

                        str(',_meanScore:,')  +
                        str(_meanScore) +    

                        str(',_stdScore:,')  +
                        str(_stdScore) +    

                        str(',_SharpMin:,')  +
                        str(_SharpMin) +                            

                        str(',_SharpMean:,')  +
                        str(_SharpMean) +    

    
                        str(',No Features:,')  +
                        str(units) +
                        str(',Min Leaf:,')  +
                        str(min_samples_leaf_Rand) +   
                        str(',Max Feat:,')  +
                        str(max_feat_Rand ) +    
                        str(',Leafs Nodes:,')  +
                        str(max_leaf_nodes_Rand) +
                        str(',Sample Split:,')  +
                        str(min_samples_split_Rand) +
                        str(',Depth of the tree:,')  +
                        str(max_depth_Rand) +
                        str(',No of trees:,') + 
                        str(n_estimators_Rand) +                     
                        str(',Features: ,') + 
                        str(FEATURES))
     
        appendFile.close()
        FEATURES = []
    except Exception as e:
        print(str(e))           
