# trolog-server

# Installation 

``` 
git clone https://github.com/jbshep/trolog-server
cd trolog-server
virtualenv -p python3 env
cp sample.env .env
# Modify .env with your own secret key.
source .env
pip install -r requirements.txt
```

## Run
    
``` 
source .env
./run-server.sh
``` 

(may need to `chmod u+x run-server.sh` one time first)
