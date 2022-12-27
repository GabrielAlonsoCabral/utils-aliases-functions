# Utils Aliases Functions
  Utils Aliases Functions helps you to replace manual tasks for functions in bash terminal globally.
  If you wish to use Javascript or another programming language instead the common SH Functions this is the correct repository.
  

## INSTALLATION

```
# clone this repository
$ git clone https://github.com/GabrielAlonsoCabral/utils-aliases-functions.git
```

## CONFIGURE YOUR ENVIRONMENT 

```
# MacOS
    1. open your ```~/.zshrc```
    2. add this lines on your ```~/.zshrc```
        `
        export ALIASES_PATH="$HOME/.aliases"
        export AWS_PATH="$HOME/.aws"
        `

```

## GENERATE YOUR ENVS

```
# This script will create your .env
$ yarn generate:env
```

## UPDATE YOUR SECRET

```
# This script will update your .env and deploy it on AWS.
$ yarn update:env
```