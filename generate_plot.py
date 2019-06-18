# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:26:25 2019

@author: N.Chlis
"""

import numpy as np
import matplotlib.pyplot as plt

connected = True
connected = False

#%%

Ndatapoints = 10 #number of datapoints in the test set
Nmodels = 5 #number of models trained

#matrix containing the data
#rows: test set datapoints
#columns: models
#each elements corresponds to the score (e.g. accuracy) of a model on a dataset
X = np.zeros((Ndatapoints,Nmodels),dtype='float')#initialize to zeros

np.random.seed(1)#set random seed for repeatability

#now generate artificial data, for the sake of plotting
for m in range(Ndatapoints):
    for d in range(Nmodels):
        X[m,d] = np.random.uniform(low=0,high=1)

#%% generate a plot of boxplots whose medians are connected by a line
        
figure_size = 4
fig, ax = plt.subplots(figsize=(figure_size*Nmodels,figure_size))
box_data = X
md = np.median(box_data,axis=0)#median

#ax.boxplot plots each column as a separate boxplot
bplots = ax.boxplot(box_data)

xticks = np.arange(Nmodels)+1

if connected == True:
    #make the boxplots transparent
    for key in bplots.keys():
        #print(key)
        for b in bplots[key]:
            b.set_alpha(0.2)
    #add a line that connects the medians of all boxplots
    ax.plot(xticks,md,marker='o',c='black',lw=5,markersize=15,label='median')
    xlab = 'Timepoint '
else:
    xlab = 'Model '

ax.set_ylabel('Score (test set)',{'fontsize':16})
ax.set_xlabel('Model',{'fontsize':16})
ax.set_title('Model Performance',{'fontsize':16})
ax.set_ylim(0,1)

#generate the xtick labels
xtick_labels = []
for m in xticks:
    xtick_labels.append(xlab+str(m))
ax.set_xticklabels(xtick_labels,rotation = 30, ha='center',fontsize=10)

#save the figure to disk
if connected == True:
    plt.savefig('model_boxplots_connected.png',dpi=200,bbox_inches='tight')
else:
    plt.savefig('model_boxplots.png',dpi=200,bbox_inches='tight')

#%% redo the same plot without the boxplots
# only plot a line for the medians, along with error-bars for interquantile range

figure_size = 4
fig, ax = plt.subplots(figsize=(figure_size*Nmodels,figure_size))
box_data = X
xticks = np.arange(Nmodels)+1

md = np.median(box_data,axis=0)
yerr = np.zeros((2,Nmodels))
for m in range(Nmodels):
    #plt.errorbar needs the difference between the percentile and the median
    #lower errorbar: 25th percentile
    yerr[0,m]=md[m]-np.percentile(X[:,m],25)#lower errorbar
    #upper errorbar: 75th percentile
    yerr[1,m]=np.percentile(X[:,m],75)-md[m]

#plot the errorbars
ax.errorbar(xticks,md,yerr,capsize=10,fmt='none',c='black')
#fmt='none' to only plot the errorbars

#plot the (optional) connecting line
if connected == True:
    ax.plot(xticks,md,marker='o',c='black',lw=5,markersize=15,label='median')
    xlab = 'Timepoint '
else:
    ax.scatter(xticks,md,marker='o',c='black',s=200)
    xlab = 'Model '

ax.set_ylabel('Score (test set)',{'fontsize':16})
ax.set_xlabel('Model',{'fontsize':16})
ax.set_title('Model Performance',{'fontsize':16})
ax.set_ylim(0,1)

ax.set_xticks(xticks)
#generate the xtick labels
xtick_labels = []
for m in xticks:
    xtick_labels.append(xlab+str(m))
ax.set_xticklabels(xtick_labels,rotation = 30, ha='center',fontsize=10)

if connected == True:
    plt.savefig('model_errorbars_connected.png',dpi=200,bbox_inches='tight')
else:
    plt.savefig('model_errorbars.png',dpi=200,bbox_inches='tight')

















