import requests
response = requests.get("https://problemasaite20.daniilsergejev.repl.co")
print(response.status_code,"\n Ja redzat skaitli 200, tad viss ir kārtībā un vietne darbojas, varat droši doties uz to.\n Ja redzat 404, vietne nedarbojas.")