from paramiko import SSHClient, RSAKey, AutoAddPolicy
from scp import SCPClient

with SSHClient() as ssh:
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    key = RSAKey.from_private_key_file("../ot2_no_pp")
    ssh.connect("169.254.188.208", username="root", pkey=key, 
            #disabled_algorithms={'keys': ['rsa-sha2-256', 'rsa-sha2-512']},
            look_for_keys=False,
            #banner_timeout=200,
            )
    
    # with SCPClient(ssh.get_transport()) as scp:
        # scp.put()

