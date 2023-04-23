import logging
import requests


logging.basicConfig(level=logging.INFO)


def xml_file(url: str, file_path: str) -> None:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            logging.info(f"XML file downloaded successfully from {url} and saved to {file_path}.")
        else:
            logging.error(f"Failed to download XML file from {url}. Error code: {response.status_code}")
    except Exception as e:
        logging.error(f"An error occurred while downloading XML file from {url}: {e}")


if __name__ == '__main__':
    url = 'https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100'
    file_path = 'data.xml'
    xml_file(url, file_path)

