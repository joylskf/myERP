from flask import Blueprint, render_template
from db import get_connection

partner_bp = Blueprint("partner", __name__)

@partner_bp.route("/partner")
def partner_list():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT partner_id, partner_name, is_customer, is_vendor
        FROM partner
        ORDER BY partner_id
    """)

    rows = cursor.fetchall()
    conn.close()

    return render_template(
        "master/partner.html",
        partners=rows
    )