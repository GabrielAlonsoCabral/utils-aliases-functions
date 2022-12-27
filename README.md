# Utils Aliases Functions
  Utils Aliases Functions helps you to replace manual tasks for functions in bash terminal globally. <br/>
  If you wish to use Javascript or another programming language instead the common SH Functions this is the correct repository.
  
  <br/>

## INSTALLATION

```
# clone this repository
$ git clone https://github.com/GabrielAlonsoCabral/utils-aliases-functions.git .aliases
$ cd .aliases
```

<br/>

## CONFIGURE YOUR ENVIRONMENT

### AWS Credentials
1. Inside ```.credentials/``` Replace your ```aws.credentials.example.json``` by ```aws.credentials.json```
2. Replace profiles in JSON by your aws profiles



### MacOS
add this code lines on your ```~/.zshrc```

```
export ALIASES_PATH="$HOME/.aliases"
export AWS_PATH="$HOME/.aws"        

function swapProfile {
    node $ALIASES_PATH/swap-aws-profile.js;
}
```

### Linux
add this code lines on your ```~/.bashrc```

```
export ALIASES_PATH="$HOME/.aliases"
export AWS_PATH="$HOME/.aws"     

function swapProfile {
    node $ALIASES_PATH/swap-aws-profile.js;
}   
```