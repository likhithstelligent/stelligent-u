import subprocess
import json
mfatoken = input("Please enter mfa token: ")
result = subprocess.check_output(f'aws sts get-session-token --no-verify-ssl --serial-number arn:aws:iam::324320755747:mfa/lambadi.l.labs --token-code {mfatoken}', shell=True)
mfaout = json.loads(result.decode())
access_key = mfaout["Credentials"]["AccessKeyId"]
secret_key = mfaout["Credentials"]["SecretAccessKey"]
session_token = mfaout["Credentials"]["SessionToken"]
subprocess.check_output(f'aws configure set aws_access_key_id {access_key} --profile temp', shell=True)
subprocess.check_output(f'aws configure set aws_secret_access_key {secret_key} --profile temp', shell=True)
subprocess.check_output(f'aws configure set aws_session_token {session_token} --profile temp', shell=True)