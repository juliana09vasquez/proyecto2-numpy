import requests

class CustomException(Exception):
    pass

def download_csv(url, filename):
    """
    Downloads a CSV file from the given URL and saves it with the specified filename.

    Args:
        url (str): The URL of the CSV file to download.
        filename (str): The name of the file to save the downloaded CSV data.

    Raises:
        requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.
        requests.exceptions.RequestException: If an error occurs during the HTTP request.
        CustomException: If the response is not a valid CSV.

    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        status_code = response.status_code
        if status_code == requests.codes.ok:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print('Descarga finalizada')
    except requests.exceptions.HTTPError as e:
        print(f'HTTP Error occurred: {str(e)}')
    except requests.exceptions.RequestException as e:
        print(f'Request Error occurred: {str(e)}')
    except ValueError as e:
        print(f'Value Error occurred: {str(e)}')