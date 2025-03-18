import requests
import json
import argparse
import sys

def check_github_token(token):
    """
    Vérifie la validité d'un token GitHub et récupère les informations associées.
    """
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {token}"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Génère une exception si le statut HTTP est une erreur

        data = response.json()
        scopes = response.headers.get("X-OAuth-Scopes", "No scopes available")

        return {
            "platform": "GitHub",
            "valid": True,
            "username": data.get("login", "Unknown"),
            "user_id": data.get("id", "Unknown"),
            "scopes": scopes
        }

    except requests.exceptions.Timeout:
        return {"valid": False, "error": "⏳ La requête GitHub a dépassé le temps limite"}
    except requests.exceptions.ConnectionError:
        return {"valid": False, "error": "🌐 Erreur réseau, vérifie ta connexion Internet"}
    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            return {"valid": False, "error": "🚫 Token GitHub invalide"}
        return {"valid": False, "error": f"⚠️ Erreur HTTP GitHub : {response.status_code}"}
    except Exception as e:
        return {"valid": False, "error": f"❌ Erreur inattendue GitHub : {str(e)}"}

def check_gitlab_token(token):
    """
    Vérifie la validité d'un token GitLab et récupère les informations associées.
    """
    url = "https://gitlab.com/api/v4/user"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()

        data = response.json()
        scopes = response.headers.get("X-OAuth-Scopes", "No scopes available")

        return {
            "platform": "GitLab",
            "valid": True,
            "username": data.get("username", "Unknown"),
            "user_id": data.get("id", "Unknown"),
            "name": data.get("name", "Unknown"),
            "email": data.get("email", "Unknown"),
            "scopes": scopes
        }

    except requests.exceptions.Timeout:
        return {"valid": False, "error": "⏳ La requête GitLab a dépassé le temps limite"}
    except requests.exceptions.ConnectionError:
        return {"valid": False, "error": "🌐 Erreur réseau, vérifie ta connexion Internet"}
    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            return {"valid": False, "error": "🚫 Token GitLab invalide"}
        return {"valid": False, "error": f"⚠️ Erreur HTTP GitLab : {response.status_code}"}
    except Exception as e:
        return {"valid": False, "error": f"❌ Erreur inattendue GitLab : {str(e)}"}

def main():
    """
    Programme principal : Vérifie un token GitHub ou GitLab.
    """
    parser = argparse.ArgumentParser(description="Vérifie la validité d'un token API pour GitHub ou GitLab.")
    parser.add_argument("platform", choices=["github", "gitlab"], help="Plateforme à vérifier (GitHub ou GitLab)")
    parser.add_argument("token", nargs="?", help="Token API à vérifier")
    args = parser.parse_args()

    # Demande le token si non fourni en argument
    token = args.token
    if not token:
        print(f"🔑 Entre ton token {args.platform.capitalize()} :", end=" ", flush=True)
        token = sys.stdin.readline().strip()

    # Exécute la vérification en fonction de la plateforme choisie
    if args.platform == "github":
        result = check_github_token(token)
    else:
        result = check_gitlab_token(token)

    # Affiche le résultat en JSON formaté
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
