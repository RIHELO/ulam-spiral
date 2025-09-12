
How to use the programs

First install a virtual environment and install the requirements:

```
cat venv_activate_requirements.sh 

python3 -m venv /tmp/environment    
source /tmp/environment/bin/activate
pip3 install -r requirements.txt
```

To check the probability in a given range:
```
python3 calculate_prob_ulam_prime.py  --initial 1 --max 100000 > primes.txt
```

To sort by the highest probability:
```
sort -r primes.txt|head 
```

Plot Ulam spiral with different initial values
```
python3 plot_ulam.py --initial 41
python3 plot_ulam.py --initial 55661 
python3 plot_ulam.py --initial 27941 
python3 plot_ulam.py --initial 733939
```
Plot Prime Density vs Initial Values
```
python3 value_percentage.py
```

Plot functions with initial value
```
python3 fplot.py 41
python3 fplot.py 55661
python3 fplot.py 27941
python3 fplot.py 733939
```


