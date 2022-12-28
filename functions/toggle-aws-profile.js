const {relative, join} = require("path")
const fs = require("fs").promises;
const execSync = require('child_process').execSync;

const ALIASES_PATH = execSync('printenv ALIASES_PATH',{encoding:'utf8'})
const AWS_PATH = execSync('printenv AWS_PATH',{encoding:'utf8'})
const AWS_RELATIVE_PATH = relative(ALIASES_PATH, AWS_PATH).replace("\n","")

const JSON_CREDENTIALS_PATH =join(__dirname,'..','.credentials','aws.credentials.json')

async function toggleAWSProfile(){
    const credentialsText = await fs.readFile(JSON_CREDENTIALS_PATH, {encoding:'utf-8'});
    const credentialsJson = JSON.parse(credentialsText)
    const newCredentials ={};

    let resultString=""
        
    Object.keys(credentialsJson).forEach((profile,index)=>{
        const credential = credentialsJson[profile]

            const profileAlias = credential.is_default ? `[${profile}]` : '[default]';
            resultString+=`${index===0?'':'\n'}${profileAlias}\naws_access_key_id=${credential.aws_access_key_id}\naws_secret_access_key=${credential.aws_secret_access_key}\n`
            credential.is_default = !credential.is_default;   
            
            newCredentials[profile]=credential
    })


    await fs.writeFile(join(AWS_RELATIVE_PATH,'credentials'),resultString)        
    await fs.writeFile(JSON_CREDENTIALS_PATH, JSON.stringify(newCredentials));
}

toggleAWSProfile()