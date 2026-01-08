from datetime import datetime
from dotenv import dotenv_values
from gtfs import download_gtfs
from get_buses_positions import get_buses_positions
import os
import json


def save_positions_to_file(buses_positions, downloads_folder, file_name):
    file_with_path = os.path.join(downloads_folder, file_name)
    print(f"Writing buses_positions to file {file_with_path} ...")
    with open(file_with_path, "w") as file:
        file.write(json.dumps(buses_positions))
    print("File saved successfully!!!")


def get_buses_positions_summary(buses_positions):
    horario_ref = buses_positions.get("hr", "N/A")
    veiculos = buses_positions.get("l", [])  # 'l' contém a lista de linhas e veículos
    total_veiculos = sum([len(linha.get("vs", [])) for linha in veiculos])
    return horario_ref, total_veiculos


def main():
    config = dotenv_values(".env")
    download_gtfs(
        url=config.get("GTFS_URL"),
        login=config.get("LOGIN"),
        password=config.get("PASSWORD"),
        downloads_folder=config.get("DOWNLOADS_FOLDER"),
    )
    buses_positions = get_buses_positions(
        token=config.get("TOKEN"),
        base_url=config.get("API_BASE_URL"),
    )
    horario_ref, total_veiculos = get_buses_positions_summary(buses_positions)
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] Ref SPTrans: {horario_ref} | Veículos Ativos: {total_veiculos}"
    )
    save_positions_to_file(
        buses_positions,
        downloads_folder=config.get("DOWNLOADS_FOLDER"),
        file_name=f"buses_positions_{horario_ref}.json",
    )


if __name__ == "__main__":
    main()
