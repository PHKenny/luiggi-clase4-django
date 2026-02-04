from typing import Any, Self

from django.db import connection
from graphene import ID, ObjectType, String
from graphql import GraphQLResolveInfo
from layrz_sdk.entities import (
  Report,
  ReportCol,
  ReportDataType,
  ReportFormat,
  ReportHeader,
  ReportPage,
  ReportRow,
  TextAlignment,
)

from auth.utils.check_session import check_session
from luiggi.graphql.bases.mutation import BaseMutation
from luiggi.graphql.enums import Status
from luiggi.settings import BASE_DIR


class MovementsReport(BaseMutation):
  """Generates a XLSX report of movements."""

  class Arguments:
    api_token = String(required=True)
    category_id = ID(required=True)

  result = String(description='The URL to download the report.')

  def mutate(self: Self, info: GraphQLResolveInfo, **args: Any) -> dict[str, Any]:
    api_token = args.get('api_token')
    if not api_token:
      return {'status': Status.BAD_REQUEST}

    errors, _ = check_session(api_token=api_token)
    if errors:
      return errors

    with connection.cursor() as cur:
      cur.execute(
        """
          SELECT
            m.id,
            m.amount,
            m.when,
            c.name
          FROM movements_movement AS m
          INNER JOIN categories_category AS c ON c.id = m.category_id
          WHERE m.category_id = %(category_id)s
        """,
        {'category_id': args.get('category_id')},
      )
      raw_rows = cur.fetchall()

    rows: list[ReportRow] = []
    for row in raw_rows:
      rows.append(
        ReportRow(
          content=[
            ReportCol(
              content=str(row[0]),
              align=TextAlignment.CENTER,
            ),  # id
            ReportCol(
              content=row[1],
              data_type=ReportDataType.CURRENCY,
              currency_symbol='USD',
              align=TextAlignment.RIGHT,
            ),  # Amount
            ReportCol(
              content=row[2],
              data_type=ReportDataType.DATETIME,
              datetime_format='%Y-%m-%d %I:%M %p',
              align=TextAlignment.CENTER,
            ),  # When
            ReportCol(
              content=str(row[3]),
              align=TextAlignment.CENTER,
            ),  # Category
          ],
        )
      )

    headers: list[ReportHeader] = [
      ReportHeader(content='ID de transacción', color='#001e60'),
      ReportHeader(content='Cantidad', color='#001e60'),
      ReportHeader(content='¿Cuando fue?', color='#001e60'),
      ReportHeader(content='Categoría', color='#001e60'),
    ]

    page = ReportPage(
      name='Reporte de Movimientos',
      headers=headers,
      rows=rows,
    )

    report = Report(name='Reporte de Movimientos', pages=[page])

    filepath = report.export(export_format=ReportFormat.MICROSOFT_EXCEL, path=BASE_DIR)

    return {'status': Status.OK, 'result': str(filepath)}


class MovementsReportMutation(ObjectType):
  movements_report = MovementsReport.Field()
