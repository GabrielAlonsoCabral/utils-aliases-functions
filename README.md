# Utils Aliases Functions
  Utils Aliases Functions helps you to replace manual tasks for functions in bash terminal globally. <br/>
  If you wish to use Javascript or another programming language instead the common SH Functions this is the correct repository.


  Developed by: <a href="https://www.github.com/gabrielAlonsoCabral">@GabrielAlonsoCabral</a>  
  <br/>

## Installation

```
# clone this repository
$ git clone https://github.com/GabrielAlonsoCabral/utils-aliases-functions.git .aliases
$ cd .aliases
```

<br/>

## Configure Your Environment

### AWS Credentials
1. Inside ```.credentials/``` Replace your ```aws.credentials.example.json``` by ```aws.credentials.json```
2. Replace profiles in JSON by your aws profiles



### MacOS
Add this code lines on your ```~/.zshrc```

```
export ALIASES_PATH="$HOME/.aliases"
export AWS_PATH="$HOME/.aws"        
export GH_NAME="ADD_YOUR_GITHUB_NAME"


function toggleAwsProfile {
    currentPath=$PWD;
    cd $ALIASES_PATH;
    node $ALIASES_PATH/functions/toggle-aws-profile.js;
    cd $currentPath;
}

function showAwsProfile {
    currentPath=$PWD;
    cd $ALIASES_PATH;
    node $ALIASES_PATH/functions/show-aws-profile.js;
    cd $currentPath;
}  

function commit (){
  /usr/bin/python $ALIASES_PATH/functions/commit.py "$@"
}
```
Enable Changes
```
$ source ~/.zshrc
```


### Linux
Add this code lines on your ```~/.bashrc```

```
export ALIASES_PATH="$HOME/.aliases"
export AWS_PATH="$HOME/.aws"    
export GH_NAME="ADD_YOUR_GITHUB_NAME"

function toggleAwsProfile {
    currentPath=$PWD;
    cd $ALIASES_PATH;
    node $ALIASES_PATH/functions/toggle-aws-profile.js;
    cd $currentPath;
}

function showAwsProfile {
    currentPath=$PWD;
    cd $ALIASES_PATH;
    node $ALIASES_PATH/functions/show-aws-profile.js;
    cd $currentPath;
}

function commit (){
  /usr/bin/python $ALIASES_PATH/functions/commit.py "$@"
}
```
Enable Changes
```
$ source ~/.bashrc
```

<br/>

## Usage

```
# Show your default AWS Profile 
$ showAwsProfile

# Toggle your default AWS Profile 
$ toggleAwsProfile
```
