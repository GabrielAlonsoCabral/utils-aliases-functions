const {join} = require("path")
const fs = require("fs").promises;

const JSON_CREDENTIALS_PATH =join(__dirname,'..','.credentials','aws.credentials.json')

async function showAWSProfile(){
    const credentialsText = await fs.readFile(JSON_CREDENTIALS_PATH, {encoding:'utf-8'});
    const credentialsJson = JSON.parse(credentialsText)
    let DEFAULT_PROFILE="";

    Object.keys(credentialsJson).find(profile=>{
        const values = credentialsJson[profile];
        if(values.is_default){
            DEFAULT_PROFILE=profile
        }
    })
    console.log(DEFAULT_PROFILE)    
    return DEFAULT_PROFILE
}

showAWSProfile()