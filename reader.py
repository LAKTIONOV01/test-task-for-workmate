import argparse
from collections import defaultdict


def parse_csv_manual(file_paths: str):
    departments = defaultdict(list)
    for file_path in file_paths:
        try:
            with open(file_path) as file:
                lines = file.readlines()
                header = lines[0].strip().split(",")
                for line in lines[1:]:
                    row = line.strip().split(",")
                    if len(row) != len(header):
                        print(f"[!] Строка пропущена (разный размер): {row}")
                        continue

                    data = dict(zip(header, row))
                    try:
                        department: str = data['department']
                        name: str = data['name']
                        hours: int = int(data['hours_worked'])
                        rate: int = int(data['hourly_rate'])
                        payout: int = hours * rate
                        departments[department].append({
                            'name': name,
                            'hours': hours,
                            'rate': rate,
                            'payout': payout
                        })
                    except (ValueError, KeyError):
                        print(f" Пропущена строка с ошибкой: {row}")
        except FileNotFoundError:
            print(f"[!] Файл не найден: {file_path}")
    return departments


def generate_report_text(departments) -> str:
    lines = []
    for dept, employees in departments.items():
        lines.append(f"\n{dept}")
        lines.append("    " + "name".ljust(20) + "hours".ljust(8) + "rate".ljust(8) + "payout")
        lines.append("    " + "-" * 50)
        total_hours: int = 0
        total_payout: int = 0

        for e in employees:
            lines.append(
                "    " + f"{e['name']:<20}{e['hours']:<8}{e['rate']:<8}${e['payout']}"
            )
            total_hours += e["hours"]
            total_payout += e["payout"]

        lines.append("    " + "-" * 50)
        lines.append(
            "    " + f"{'':<20}{total_hours:<8}{'':<8}${total_payout}"
        )

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', help='Файлы с данными сотрудников')
    parser.add_argument('--report', required=True, choices=['payout'], help='Тип отчета')
    args = parser.parse_args()

    if args.report == 'payout':
        data = parse_csv_manual(args.files)
        generate_report_text(data)


if __name__ == '__main__':
    main()
