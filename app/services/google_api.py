from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"
DRIVE_VERSION = 'v3'
SHEETS_VERSION = 'v4'
ROW_COUNT = 100
COLUMN_COUNT = 10


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = {
        'properties': {
            'title': f'Отчет на {now_date_time}',
            'locale': 'ru_RU'},
        'sheets': [
            {
                'properties': {
                    'sheetType': 'GRID',
                    'sheetId': 0,
                    'title': 'Рейтинг проектов по скорости сбора средств',
                    'gridProperties': {
                        'rowCount': ROW_COUNT,
                        'columnCount': COLUMN_COUNT
                    }
                }
            }
        ]
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    return response['spreadsheetId']


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email,

    }
    service = await wrapper_services.discover('drive', DRIVE_VERSION)
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id",
            sendNotificationEmail=False,
        )
    )


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list,
        wrapper_services: Aiogoogle
):
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', SHEETS_VERSION)
    table_values = [
        ['Отчет от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    for project in projects:
        table_values.append([
            project.name,
            str(project.close_date - project.create_date),
            project.description
        ])

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=f"A1:C{len(table_values)}",
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
