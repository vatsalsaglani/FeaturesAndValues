This package is the **first** version of the _**FeaturesAndValues**_ package. The aim for developing this package is to input _features_, _number of features_, _value of every feature_, _etc..._ 

**For Example:** When you are given with number of features and value of each row as space separated string and are asked to train a Machine Learning algorithm on those values. Once the algorithm is trained on all the attributes the trained model can be used to predict the value of another set of inputs where we don't have the value of the last attribute or the classification attribute.

**Pre-requisites:** You need to have pandas, numpy and sklearn installed before hand to work with this package. To add this packages do:

```
python3 -m pip install -U pandas numpy sklearn
```

**Working with the package:**
_Given that you have some **n** observation with **f** features each exclusive of a classification feature. There will be **f+1** features including the classification feature. You are asked to predict the classification feature for other **m** observations, do:
```python
import FeaturesAndValues
#FeaturesAndValues(totalNumberOfObservations, totalNumberOfFeatursofEveryObservation, totalNumberOfUnknownObservations)
FeaturesAndValues(n, f+1, m)
``` 
**Note:** Note all the numbers must be integers.

**Further Addition:** Apart from the LR model later, I will be adding other models also.

****Made with :heart: by _Vatsal Saglani_****_(http://thevatsalsaglani.surge.sh)_
