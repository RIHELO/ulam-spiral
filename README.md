
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
python3 calculate_prob_ulam_prime.py  --initial 41 --max 100000 > primes.txt
```

To sort by the highest probability:
```
sort -r primes.txt|head 
```

